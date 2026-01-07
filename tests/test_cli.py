"""Tests for CLI functionality."""

import subprocess
import sys
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent


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
            [
                sys.executable,
                "-m",
                "wetwire_aws.cli",
                "test",
                "--persona",
                "invalid",
                "test prompt",
            ],
            capture_output=True,
            text=True,
            env=env,
        )
        assert result.returncode != 0
        # Either "Unknown persona" (if wetwire-core installed) or "wetwire-core required"
        assert (
            "Unknown persona" in result.stderr
            or "wetwire-core required" in result.stderr
        )


class TestBuildWithPath:
    """Test build command with path support."""

    @staticmethod
    def create_test_package(parent_dir: Path, name: str = "test_pkg") -> Path:
        """Create a minimal valid wetwire-aws package for testing."""
        pkg_dir = parent_dir / name
        pkg_dir.mkdir(parents=True, exist_ok=True)

        init_content = '''"""Test package."""
from wetwire_aws.loader import setup_resources

setup_resources(__file__, __name__, globals())
'''
        (pkg_dir / "__init__.py").write_text(init_content)

        resources_content = '''"""Test resources."""
from . import *
from wetwire_aws.resources import s3

class TestBucket(s3.Bucket):
    """A simple S3 bucket for testing."""
    resource: s3.Bucket  # Required for auto-decoration
    bucket_name = "test-bucket-name"
'''
        (pkg_dir / "resources.py").write_text(resources_content)

        return pkg_dir

    def test_build_with_relative_path(self):
        """Build accepts a relative path to a package."""
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create package in tmpdir
            self.create_test_package(Path(tmpdir))

            # Run from tmpdir so relative path works
            result = subprocess.run(
                [sys.executable, "-m", "wetwire_aws.cli", "build", "test_pkg"],
                capture_output=True,
                text=True,
                cwd=tmpdir,
            )
            assert result.returncode == 0, f"stderr: {result.stderr}"
            assert "AWSTemplateFormatVersion" in result.stdout
            assert "TestBucket" in result.stdout

    def test_build_with_absolute_path(self):
        """Build accepts an absolute path to a package."""
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            pkg_path = self.create_test_package(Path(tmpdir))

            result = subprocess.run(
                [sys.executable, "-m", "wetwire_aws.cli", "build", str(pkg_path)],
                capture_output=True,
                text=True,
            )
            assert result.returncode == 0, f"stderr: {result.stderr}"
            assert "AWSTemplateFormatVersion" in result.stdout
            assert "TestBucket" in result.stdout

    def test_build_with_nonexistent_path(self):
        """Build fails gracefully with non-existent path."""
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "wetwire_aws.cli",
                "build",
                "/nonexistent/path/to/package",
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0
        assert (
            "not found" in result.stderr.lower()
            or "does not exist" in result.stderr.lower()
        )

    def test_build_path_from_different_directory(self):
        """Build with path works from any directory."""
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            pkg_path = self.create_test_package(Path(tmpdir))

            # Create another temp dir to run from
            with tempfile.TemporaryDirectory() as run_dir:
                result = subprocess.run(
                    [sys.executable, "-m", "wetwire_aws.cli", "build", str(pkg_path)],
                    capture_output=True,
                    text=True,
                    cwd=run_dir,  # Run from a different directory
                )
                assert result.returncode == 0, f"stderr: {result.stderr}"
                assert "AWSTemplateFormatVersion" in result.stdout

    def test_build_help_shows_path_option(self):
        """Build help shows path as positional argument."""
        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "build", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        # Should show PATH as positional argument
        assert "PATH" in result.stdout or "path" in result.stdout.lower()

    def test_build_path_not_a_package(self):
        """Build fails gracefully when path exists but is not a package."""
        import tempfile

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create directory without __init__.py
            not_pkg = Path(tmpdir) / "not_a_package"
            not_pkg.mkdir()

            result = subprocess.run(
                [sys.executable, "-m", "wetwire_aws.cli", "build", str(not_pkg)],
                capture_output=True,
                text=True,
            )
            assert result.returncode != 0
            assert (
                "not a Python package" in result.stderr
                or "__init__.py" in result.stderr
            )
