"""Kiro CLI configuration installer.

This module handles auto-installation of Kiro CLI configurations:
- Agent config (~/.kiro/agents/wetwire-runner.json)
- MCP config (.kiro/mcp.json in project directory)
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any

# Embedded agent configuration
AGENT_CONFIG: dict[str, Any] = {
    "name": "wetwire-runner",
    "description": "Infrastructure code generator using wetwire-aws",
    "allowedTools": ["fs_read", "fs_write", "bash", "mcp:wetwire-aws-mcp"],
    "context": {
        "patterns": """wetwire-aws Syntax Principles:

1. RESOURCE DECLARATION - Resources are Python classes inheriting from generated types:
   class MyBucket(s3.Bucket):
       bucket_name = "my-data"

2. DIRECT REFERENCES - Reference other resources by class name:
   class MyFunction(lambda_.Function):
       role = MyRole.Arn  # GetAtt via attribute access
       environment = MyEnv

3. NESTED TYPES - Extract nested configs to separate classes:
   class MyEnv(lambda_.Environment):
       variables = MyVariables

4. TYPE-SAFE CONSTANTS - Use typed enums instead of strings:
   runtime = lambda_.Runtime.PYTHON3_12  # Not "python3.12"

Key Lint Rules (WAW001-WAW020):
- WAW001-004: Use typed constants (parameters, pseudo-params, enums, intrinsics)
- WAW006: No-parens references (use MyRole.Arn not MyRole().Arn)
- WAW013: Use wrapper classes, not inline constructors
- WAW019-020: Avoid explicit Ref() and GetAtt() - use direct references""",
        "workflow": """Design Workflow:
1. EXPLORE - Understand requirements and clarify with user
2. PLAN - Design resource architecture
3. IMPLEMENT - Write Python classes inheriting from AWS types
4. LINT - Run wetwire_lint to check code patterns
5. BUILD - Run wetwire_build to generate CloudFormation template
6. ITERATE - Fix any issues and rebuild""",
    },
}


def get_agent_config_path() -> Path:
    """Get the path to the agent config file."""
    return Path.home() / ".kiro" / "agents" / "wetwire-runner.json"


def get_mcp_config_path(project_dir: Path | None = None) -> Path:
    """Get the path to the MCP config file."""
    if project_dir is None:
        project_dir = Path.cwd()
    return project_dir / ".kiro" / "mcp.json"


def check_kiro_installed() -> bool:
    """Check if Kiro CLI is installed and available."""
    return shutil.which("kiro-cli") is not None


def install_agent_config(force: bool = False) -> bool:
    """Install the wetwire-runner agent config.

    Args:
        force: Overwrite existing config if True.

    Returns:
        True if config was installed, False if skipped.
    """
    config_path = get_agent_config_path()

    if config_path.exists() and not force:
        return False

    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(AGENT_CONFIG, indent=2))
    return True


def install_mcp_config(project_dir: Path | None = None, force: bool = False) -> bool:
    """Install the MCP server config in project directory.

    Args:
        project_dir: Project directory. Defaults to current directory.
        force: Overwrite existing config if True.

    Returns:
        True if config was installed, False if skipped.
    """
    config_path = get_mcp_config_path(project_dir)

    # Load existing config or create new one
    if config_path.exists():
        if not force:
            # Check if wetwire-aws-mcp is already configured
            existing = json.loads(config_path.read_text())
            if "wetwire-aws-mcp" in existing.get("mcpServers", {}):
                return False
            # Merge with existing
            mcp_config = existing
        else:
            mcp_config = {"mcpServers": {}}
    else:
        mcp_config = {"mcpServers": {}}

    # Add wetwire-aws-mcp server
    mcp_config["mcpServers"]["wetwire-aws-mcp"] = {
        "command": "wetwire-aws-mcp",
    }

    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(json.dumps(mcp_config, indent=2))
    return True


def install_kiro_configs(
    project_dir: Path | None = None, force: bool = False, verbose: bool = False
) -> dict[str, bool]:
    """Install all Kiro configurations.

    Args:
        project_dir: Project directory for MCP config. Defaults to cwd.
        force: Overwrite existing configs if True.
        verbose: Print status messages.

    Returns:
        Dict with 'agent' and 'mcp' keys indicating what was installed.
    """
    results = {
        "agent": install_agent_config(force=force),
        "mcp": install_mcp_config(project_dir=project_dir, force=force),
    }

    if verbose:
        if results["agent"]:
            print(f"Installed agent config: {get_agent_config_path()}", file=sys.stderr)
        if results["mcp"]:
            print(
                f"Installed MCP config: {get_mcp_config_path(project_dir)}",
                file=sys.stderr,
            )

    return results


def launch_kiro(prompt: str | None = None, project_dir: Path | None = None) -> int:
    """Launch Kiro CLI with the wetwire-runner agent.

    Args:
        prompt: Optional initial prompt for the conversation.
        project_dir: Project directory. Defaults to current directory.

    Returns:
        Exit code from kiro-cli.
    """
    if not check_kiro_installed():
        print(
            "Error: Kiro CLI not found. Install from https://kiro.dev/docs/cli/",
            file=sys.stderr,
        )
        return 1

    # Ensure configs are installed
    install_kiro_configs(project_dir=project_dir, verbose=True)

    # Build command
    cmd = ["kiro-cli", "chat", "--agent", "wetwire-runner"]
    if prompt:
        cmd.extend(["--message", prompt])

    # Launch Kiro
    try:
        result = subprocess.run(cmd, cwd=project_dir)
        return result.returncode
    except FileNotFoundError:
        print("Error: Failed to launch kiro-cli.", file=sys.stderr)
        return 1


def run_kiro_scenario(
    prompt: str,
    project_dir: Path | None = None,
    timeout: int = 300,
    auto_exit: bool = True,
) -> dict[str, Any]:
    """Run a Kiro CLI scenario non-interactively for testing.

    This function runs kiro-cli with a prompt and captures output,
    suitable for automated testing and CI pipelines.

    Args:
        prompt: The infrastructure prompt to send to Kiro.
        project_dir: Project directory. Defaults to temp directory.
        timeout: Maximum time in seconds to wait (default: 300).
        auto_exit: If True, append instruction to exit after completion.

    Returns:
        Dict with keys:
            - success: bool - Whether the scenario completed successfully
            - exit_code: int - Process exit code
            - stdout: str - Captured stdout
            - stderr: str - Captured stderr
            - package_path: str | None - Path to created package if any
            - template_valid: bool - Whether build produced valid template
    """
    import tempfile

    if not check_kiro_installed():
        return {
            "success": False,
            "exit_code": 1,
            "stdout": "",
            "stderr": "Kiro CLI not found",
            "package_path": None,
            "template_valid": False,
        }

    # Use temp directory if not specified
    if project_dir is None:
        temp_dir = tempfile.mkdtemp(prefix="kiro_test_")
        project_dir = Path(temp_dir)
    else:
        project_dir = Path(project_dir)
        project_dir.mkdir(parents=True, exist_ok=True)

    # Ensure configs are installed
    install_kiro_configs(project_dir=project_dir, verbose=False)

    # Build the full prompt with auto-exit instruction
    full_prompt = prompt
    if auto_exit:
        full_prompt = (
            f"{prompt}\n\n"
            "After successfully creating the package and running lint and build, "
            "output 'SCENARIO_COMPLETE' and exit."
        )

    # Build command for non-interactive execution
    cmd = [
        "kiro-cli",
        "chat",
        "--agent", "wetwire-runner",
        "--message", full_prompt,
        "--no-interactive",  # Run without interactive prompts
    ]

    # Run kiro-cli
    try:
        result = subprocess.run(
            cmd,
            cwd=project_dir,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "exit_code": -1,
            "stdout": "",
            "stderr": f"Timeout after {timeout} seconds",
            "package_path": None,
            "template_valid": False,
        }
    except FileNotFoundError:
        return {
            "success": False,
            "exit_code": 1,
            "stdout": "",
            "stderr": "Failed to launch kiro-cli",
            "package_path": None,
            "template_valid": False,
        }

    # Find created package (look for directories with __init__.py)
    package_path = None
    for item in project_dir.iterdir():
        if item.is_dir() and (item / "__init__.py").exists():
            # Skip .kiro directory
            if item.name != ".kiro":
                package_path = str(item)
                break

    # Check if template is valid by running build
    template_valid = False
    if package_path:
        try:
            build_result = subprocess.run(
                ["wetwire-aws", "build", package_path],
                capture_output=True,
                text=True,
                timeout=30,
            )
            template_valid = build_result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

    return {
        "success": result.returncode == 0 and template_valid,
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "package_path": package_path,
        "template_valid": template_valid,
    }
