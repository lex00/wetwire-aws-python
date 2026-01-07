"""Tests for CLI functionality."""

import subprocess
import sys


class TestCLI:
    """Test CLI commands."""

    def test_help(self):
        """CLI shows help message."""
        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "Generate CloudFormation templates" in result.stdout

    def test_version(self):
        """CLI shows version."""
        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "--version"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "wetwire-aws" in result.stdout

    def test_build_no_resources(self):
        """Build fails gracefully when no resources registered."""
        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "build"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0
        assert "No resources registered" in result.stderr

    def test_list_no_resources(self):
        """List shows message when no resources registered."""
        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "list"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "No resources registered" in result.stderr

    def test_validate_no_resources(self):
        """Validate fails when no resources registered."""
        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "validate"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0
        assert "No resources registered" in result.stderr

    def test_design_help(self):
        """Design command shows help."""
        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "design", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "wetwire-aws design" in result.stdout
        assert "--output" in result.stdout

    def test_test_help(self):
        """Test command shows help."""
        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "test", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "wetwire-aws test" in result.stdout
        assert "--persona" in result.stdout

    def test_test_invalid_persona(self):
        """Test command fails with invalid persona."""
        import os

        # Clear API key to avoid actual API calls
        env = os.environ.copy()
        env.pop("ANTHROPIC_API_KEY", None)

        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "test", "--persona", "invalid", "test prompt"],
            capture_output=True,
            text=True,
            env=env,
        )
        assert result.returncode != 0
        assert "Unknown persona" in result.stderr
