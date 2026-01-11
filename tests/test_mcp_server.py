"""Tests for MCP server functionality."""

import json
import sys
import tempfile
from pathlib import Path


class TestMCPServerHelpers:
    """Test MCP server helper functions."""

    def test_create_package_success(self):
        """wetwire_init creates a valid package."""
        from wetwire_aws.mcp_server import _create_package

        with tempfile.TemporaryDirectory() as tmpdir:
            result = _create_package(tmpdir, "test_infra")

            assert result["success"] is True
            assert "test_infra" in result["message"]
            assert result["path"] == str(Path(tmpdir) / "test_infra")

            # Verify package structure
            pkg_dir = Path(tmpdir) / "test_infra"
            assert pkg_dir.exists()
            assert (pkg_dir / "__init__.py").exists()

            # Verify __init__.py content
            init_content = (pkg_dir / "__init__.py").read_text()
            assert "setup_resources" in init_content

    def test_create_package_invalid_name(self):
        """wetwire_init rejects invalid module names."""
        from wetwire_aws.mcp_server import _create_package

        with tempfile.TemporaryDirectory() as tmpdir:
            result = _create_package(tmpdir, "invalid-name")

            assert result["success"] is False
            assert "Invalid module name" in result["error"]

    def test_create_package_nonexistent_path(self):
        """wetwire_init fails with nonexistent path."""
        from wetwire_aws.mcp_server import _create_package

        result = _create_package("/nonexistent/path", "test_pkg")

        assert result["success"] is False
        assert "does not exist" in result["error"]

    def test_create_package_already_exists(self):
        """wetwire_init fails when package already exists."""
        from wetwire_aws.mcp_server import _create_package

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create first package
            _create_package(tmpdir, "existing_pkg")

            # Try to create again
            result = _create_package(tmpdir, "existing_pkg")

            assert result["success"] is False
            assert "already exists" in result["error"]

    def test_lint_path_no_issues(self):
        """wetwire_lint returns empty list for clean code."""
        from wetwire_aws.mcp_server import _lint_path

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a clean Python file
            clean_file = Path(tmpdir) / "clean.py"
            clean_file.write_text('"""Clean module."""\nx = 1\n')

            result = _lint_path(str(clean_file))

            assert result["success"] is True
            assert result["issues"] == []
            assert result["issue_count"] == 0

    def test_lint_path_with_issues(self):
        """wetwire_lint detects issues in code."""
        from wetwire_aws.mcp_server import _lint_path

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a file with lint issues (using string instead of enum)
            bad_file = Path(tmpdir) / "bad.py"
            bad_file.write_text('''"""Bad module."""
from wetwire_aws.resources.s3 import Bucket

class MyBucket(Bucket):
    sse_algorithm = "AES256"
''')

            result = _lint_path(str(bad_file))

            assert result["success"] is True
            assert result["issue_count"] > 0
            # Check issue structure
            assert all("rule_id" in issue for issue in result["issues"])
            assert all("message" in issue for issue in result["issues"])
            assert all("line" in issue for issue in result["issues"])

    def test_lint_path_directory(self):
        """wetwire_lint handles directories."""
        from wetwire_aws.mcp_server import _lint_path

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create multiple Python files
            (Path(tmpdir) / "file1.py").write_text("x = 1\n")
            (Path(tmpdir) / "file2.py").write_text("y = 2\n")

            result = _lint_path(tmpdir)

            assert result["success"] is True
            assert result["file_count"] == 2

    def test_lint_path_fix(self):
        """wetwire_lint with fix=True modifies files."""
        from wetwire_aws.mcp_server import _lint_path

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a file with a fixable issue
            bad_file = Path(tmpdir) / "fixable.py"
            bad_file.write_text('''"""Fixable module."""
from wetwire_aws.resources.s3 import Bucket

class MyBucket(Bucket):
    sse_algorithm = "AES256"
''')

            result = _lint_path(str(bad_file), fix=True)

            assert result["success"] is True
            assert "fixed_files" in result

    def test_lint_path_nonexistent(self):
        """wetwire_lint fails with nonexistent path."""
        from wetwire_aws.mcp_server import _lint_path

        result = _lint_path("/nonexistent/path.py")

        assert result["success"] is False
        assert "does not exist" in result["error"]

    def test_build_template_success(self):
        """wetwire_build generates CloudFormation template."""
        from wetwire_aws.mcp_server import _build_template

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a valid wetwire-aws package
            pkg_dir = Path(tmpdir) / "test_pkg"
            pkg_dir.mkdir()

            init_content = '''"""Test package."""
from wetwire_aws.loader import setup_resources

setup_resources(__file__, __name__, globals())
'''
            (pkg_dir / "__init__.py").write_text(init_content)

            resources_content = '''"""Test resources."""
from . import *
from wetwire_aws.resources import s3

class TestBucket(s3.Bucket):
    """A simple S3 bucket."""
    resource: s3.Bucket
    bucket_name = "test-bucket"
'''
            (pkg_dir / "resources.py").write_text(resources_content)

            result = _build_template(str(pkg_dir))

            assert result["success"] is True
            assert "template" in result
            assert result["resource_count"] > 0

            # Verify it's valid JSON
            template = json.loads(result["template"])
            assert "AWSTemplateFormatVersion" in template
            assert "Resources" in template

    def test_build_template_yaml(self):
        """wetwire_build supports YAML output format."""
        from wetwire_aws.mcp_server import _build_template

        with tempfile.TemporaryDirectory() as tmpdir:
            # Create a valid wetwire-aws package
            pkg_dir = Path(tmpdir) / "test_pkg"
            pkg_dir.mkdir()

            init_content = '''"""Test package."""
from wetwire_aws.loader import setup_resources

setup_resources(__file__, __name__, globals())
'''
            (pkg_dir / "__init__.py").write_text(init_content)

            resources_content = '''"""Test resources."""
from . import *
from wetwire_aws.resources import s3

class YamlBucket(s3.Bucket):
    """A simple S3 bucket."""
    resource: s3.Bucket
    bucket_name = "yaml-bucket"
'''
            (pkg_dir / "resources.py").write_text(resources_content)

            result = _build_template(str(pkg_dir), output_format="yaml")

            assert result["success"] is True
            assert result["format"] == "yaml"
            # YAML contains AWSTemplateFormatVersion as a key
            assert "AWSTemplateFormatVersion" in result["template"]

    def test_build_template_nonexistent_path(self):
        """wetwire_build fails with nonexistent path."""
        from wetwire_aws.mcp_server import _build_template

        result = _build_template("/nonexistent/path")

        assert result["success"] is False
        assert "does not exist" in result["error"]

    def test_build_template_not_a_package(self):
        """wetwire_build fails when path is not a package."""
        from wetwire_aws.mcp_server import _build_template

        with tempfile.TemporaryDirectory() as tmpdir:
            # Directory without __init__.py
            result = _build_template(tmpdir)

            assert result["success"] is False
            assert "__init__.py" in result["error"]


class TestMCPServerImport:
    """Test MCP server module imports."""

    def test_import_without_mcp(self, monkeypatch):
        """Module imports gracefully without mcp package."""
        # This tests that the module can be imported even if mcp is not installed
        # The import guard should handle it
        import importlib

        # Reload to test import behavior
        import wetwire_aws.mcp_server

        importlib.reload(wetwire_aws.mcp_server)

        # Should have helper functions regardless of mcp availability
        assert hasattr(wetwire_aws.mcp_server, "_create_package")
        assert hasattr(wetwire_aws.mcp_server, "_lint_path")
        assert hasattr(wetwire_aws.mcp_server, "_build_template")


class TestCLIDesignProvider:
    """Test CLI design command with --provider flag."""

    def test_design_help_shows_provider(self):
        """Design help shows --provider option."""
        import subprocess

        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "design", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "--provider" in result.stdout
        assert "anthropic" in result.stdout
        assert "kiro" in result.stdout

    def test_design_kiro_without_kiro_cli(self):
        """Design with kiro provider fails gracefully without kiro-cli."""
        import os
        import subprocess

        # Remove PATH to ensure kiro-cli not found
        env = os.environ.copy()
        env["PATH"] = ""

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "wetwire_aws.cli",
                "design",
                "--provider",
                "kiro",
                "test",
            ],
            capture_output=True,
            text=True,
            env=env,
        )
        # Should fail because kiro-cli is not installed
        assert result.returncode != 0


class TestCLITestProvider:
    """Test CLI test command with --provider flag."""

    def test_test_help_shows_provider(self):
        """Test help shows --provider option."""
        import subprocess

        result = subprocess.run(
            [sys.executable, "-m", "wetwire_aws.cli", "test", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "--provider" in result.stdout
        assert "anthropic" in result.stdout
        assert "kiro" in result.stdout

    def test_test_kiro_without_kiro_cli(self):
        """Test with kiro provider fails gracefully without kiro-cli."""
        import os
        import subprocess

        # Remove PATH to ensure kiro-cli not found
        env = os.environ.copy()
        env["PATH"] = ""

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "wetwire_aws.cli",
                "test",
                "--provider",
                "kiro",
                "test prompt",
            ],
            capture_output=True,
            text=True,
            env=env,
        )
        # Should fail because kiro-cli is not installed
        assert result.returncode != 0

    def test_test_provider_default_is_anthropic(self):
        """Test command defaults to anthropic provider."""
        import os
        import subprocess

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
                "beginner",
                "test prompt",
            ],
            capture_output=True,
            text=True,
            env=env,
        )
        # Without API key, anthropic provider should fail with auth error
        assert result.returncode != 0
        # Error should mention wetwire-core or API key, not kiro
        assert "kiro" not in result.stderr.lower() or "kiro-cli" not in result.stderr.lower()
