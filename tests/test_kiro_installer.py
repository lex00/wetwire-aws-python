"""Tests for Kiro CLI installer."""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch


class TestKiroInstaller:
    """Test Kiro configuration installer."""

    def test_get_agent_config_path(self):
        """Agent config path is in ~/.kiro/agents."""
        from wetwire_aws.kiro.installer import get_agent_config_path

        path = get_agent_config_path()
        assert path.parent.name == "agents"
        assert path.parent.parent.name == ".kiro"
        assert path.name == "wetwire-runner.json"

    def test_get_mcp_config_path_default(self):
        """MCP config path defaults to current directory."""
        from wetwire_aws.kiro.installer import get_mcp_config_path

        path = get_mcp_config_path()
        assert path.name == "mcp.json"
        assert path.parent.name == ".kiro"

    def test_get_mcp_config_path_custom_dir(self):
        """MCP config path respects custom directory."""
        from wetwire_aws.kiro.installer import get_mcp_config_path

        with tempfile.TemporaryDirectory() as tmpdir:
            path = get_mcp_config_path(Path(tmpdir))
            assert str(tmpdir) in str(path)
            assert path.name == "mcp.json"

    def test_check_kiro_installed_not_found(self):
        """check_kiro_installed returns False when kiro-cli not in PATH."""
        from wetwire_aws.kiro.installer import check_kiro_installed

        with patch("shutil.which", return_value=None):
            assert check_kiro_installed() is False

    def test_check_kiro_installed_found(self):
        """check_kiro_installed returns True when kiro-cli in PATH."""
        from wetwire_aws.kiro.installer import check_kiro_installed

        with patch("shutil.which", return_value="/usr/local/bin/kiro-cli"):
            assert check_kiro_installed() is True

    def test_install_agent_config_creates_file(self):
        """install_agent_config creates the agent config file."""
        from wetwire_aws.kiro.installer import install_agent_config

        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / ".kiro" / "agents" / "wetwire-runner.json"

            with patch(
                "wetwire_aws.kiro.installer.get_agent_config_path",
                return_value=config_path,
            ):
                result = install_agent_config()

            assert result is True
            assert config_path.exists()

            # Verify content
            content = json.loads(config_path.read_text())
            assert content["name"] == "wetwire-runner"
            assert content["model"] == "claude-sonnet-4"
            assert "tools" in content
            assert "mcpServers" in content
            assert "wetwire-aws-mcp" in content["mcpServers"]

    def test_install_agent_config_skips_existing(self):
        """install_agent_config skips if file exists."""
        from wetwire_aws.kiro.installer import install_agent_config

        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / ".kiro" / "agents" / "wetwire-runner.json"
            config_path.parent.mkdir(parents=True)
            config_path.write_text('{"existing": true}')

            with patch(
                "wetwire_aws.kiro.installer.get_agent_config_path",
                return_value=config_path,
            ):
                result = install_agent_config()

            assert result is False
            # Original content preserved
            content = json.loads(config_path.read_text())
            assert content == {"existing": True}

    def test_install_agent_config_force_overwrites(self):
        """install_agent_config with force=True overwrites existing."""
        from wetwire_aws.kiro.installer import install_agent_config

        with tempfile.TemporaryDirectory() as tmpdir:
            config_path = Path(tmpdir) / ".kiro" / "agents" / "wetwire-runner.json"
            config_path.parent.mkdir(parents=True)
            config_path.write_text('{"existing": true}')

            with patch(
                "wetwire_aws.kiro.installer.get_agent_config_path",
                return_value=config_path,
            ):
                result = install_agent_config(force=True)

            assert result is True
            # New content written
            content = json.loads(config_path.read_text())
            assert content["name"] == "wetwire-runner"

    def test_install_mcp_config_creates_file(self):
        """install_mcp_config creates the MCP config file."""
        from wetwire_aws.kiro.installer import install_mcp_config

        with tempfile.TemporaryDirectory() as tmpdir:
            project_dir = Path(tmpdir)
            result = install_mcp_config(project_dir=project_dir)

            assert result is True
            config_path = project_dir / ".kiro" / "mcp.json"
            assert config_path.exists()

            # Verify content
            content = json.loads(config_path.read_text())
            assert "mcpServers" in content
            assert "wetwire-aws-mcp" in content["mcpServers"]
            # Either uses absolute path (if found) or uv run fallback
            mcp_server = content["mcpServers"]["wetwire-aws-mcp"]
            assert "command" in mcp_server
            # If absolute path found, no args; otherwise uses uv run
            if mcp_server["command"] != "uv":
                assert "wetwire-aws-mcp" in mcp_server["command"]
            else:
                assert mcp_server["args"] == ["run", "wetwire-aws-mcp"]

    def test_install_mcp_config_merges_existing(self):
        """install_mcp_config merges with existing config."""
        from wetwire_aws.kiro.installer import install_mcp_config

        with tempfile.TemporaryDirectory() as tmpdir:
            project_dir = Path(tmpdir)
            config_path = project_dir / ".kiro" / "mcp.json"
            config_path.parent.mkdir(parents=True)

            # Create existing config with another server
            existing_config = {
                "mcpServers": {
                    "other-server": {"command": "other-cmd"},
                }
            }
            config_path.write_text(json.dumps(existing_config))

            result = install_mcp_config(project_dir=project_dir)

            assert result is True
            content = json.loads(config_path.read_text())
            # Both servers present
            assert "other-server" in content["mcpServers"]
            assert "wetwire-aws-mcp" in content["mcpServers"]

    def test_install_mcp_config_skips_if_already_configured(self):
        """install_mcp_config skips if wetwire-aws-mcp already configured."""
        from wetwire_aws.kiro.installer import install_mcp_config

        with tempfile.TemporaryDirectory() as tmpdir:
            project_dir = Path(tmpdir)
            config_path = project_dir / ".kiro" / "mcp.json"
            config_path.parent.mkdir(parents=True)

            # Create existing config with wetwire-aws-mcp
            existing_config = {
                "mcpServers": {
                    "wetwire-aws-mcp": {"command": "custom-command"},
                }
            }
            config_path.write_text(json.dumps(existing_config))

            result = install_mcp_config(project_dir=project_dir)

            assert result is False
            # Original command preserved
            content = json.loads(config_path.read_text())
            assert content["mcpServers"]["wetwire-aws-mcp"]["command"] == "custom-command"

    def test_install_kiro_configs_both(self):
        """install_kiro_configs installs both agent and MCP configs."""
        from wetwire_aws.kiro.installer import install_kiro_configs

        with tempfile.TemporaryDirectory() as tmpdir:
            project_dir = Path(tmpdir)
            agent_path = Path(tmpdir) / ".kiro" / "agents" / "wetwire-runner.json"

            with patch(
                "wetwire_aws.kiro.installer.get_agent_config_path",
                return_value=agent_path,
            ):
                results = install_kiro_configs(project_dir=project_dir)

            assert results["agent"] is True
            assert results["mcp"] is True
            assert agent_path.exists()
            assert (project_dir / ".kiro" / "mcp.json").exists()

    def test_launch_kiro_fails_without_kiro_cli(self):
        """launch_kiro fails when kiro-cli not installed."""
        from wetwire_aws.kiro.installer import launch_kiro

        with patch("wetwire_aws.kiro.installer.check_kiro_installed", return_value=False):
            exit_code = launch_kiro(prompt="test")

        assert exit_code == 1


class TestAgentConfig:
    """Test agent configuration content."""

    def test_agent_config_structure(self):
        """Agent config has required fields."""
        from wetwire_aws.kiro.installer import AGENT_CONFIG

        assert AGENT_CONFIG["name"] == "wetwire-runner"
        assert "description" in AGENT_CONFIG
        assert AGENT_CONFIG["model"] == "claude-sonnet-4"
        assert "tools" in AGENT_CONFIG
        assert "mcpServers" in AGENT_CONFIG
        assert "prompt" in AGENT_CONFIG

    def test_agent_config_tools(self):
        """Agent config has correct tools setting."""
        from wetwire_aws.kiro.installer import AGENT_CONFIG

        # Uses wildcard for all tools
        assert AGENT_CONFIG["tools"] == ["*"]

    def test_agent_config_prompt_patterns(self):
        """Agent config prompt includes syntax patterns."""
        from wetwire_aws.kiro.installer import AGENT_CONFIG

        prompt = AGENT_CONFIG["prompt"]
        assert "RESOURCE DECLARATION" in prompt
        assert "DIRECT REFERENCES" in prompt
        assert "TYPE-SAFE CONSTANTS" in prompt

    def test_agent_config_prompt_workflow(self):
        """Agent config prompt includes workflow."""
        from wetwire_aws.kiro.installer import AGENT_CONFIG

        prompt = AGENT_CONFIG["prompt"]
        # Updated to match current prompt structure
        assert "Design Workflow" in prompt
        assert "wetwire_init" in prompt
        assert "wetwire_lint" in prompt
        assert "wetwire_build" in prompt
