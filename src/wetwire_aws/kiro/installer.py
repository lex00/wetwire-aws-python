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
