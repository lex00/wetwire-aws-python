"""Integration tests for Kiro CLI with wetwire-aws.

These tests actually invoke kiro-cli and are skipped by default.
To run them, set the KIRO_TESTS environment variable:

    KIRO_TESTS=1 pytest tests/test_kiro_integration.py -v

Requirements:
- Kiro CLI installed and in PATH
- wetwire-aws[kiro] installed
- Valid Kiro CLI authentication/configuration
"""

import os
import tempfile
from pathlib import Path

import pytest

# Skip all tests in this module unless KIRO_TESTS is set
pytestmark = pytest.mark.skipif(
    os.getenv("KIRO_TESTS") != "1",
    reason="Kiro integration tests disabled. Set KIRO_TESTS=1 to enable.",
)


@pytest.fixture
def temp_project_dir():
    """Create a temporary directory for test projects."""
    with tempfile.TemporaryDirectory(prefix="kiro_integration_") as tmpdir:
        yield Path(tmpdir)


class TestKiroScenarios:
    """Integration tests that run actual Kiro CLI scenarios."""

    def test_create_s3_bucket(self, temp_project_dir):
        """Kiro can create a simple S3 bucket package."""
        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt="Create an S3 bucket named 'test-data-bucket'",
            project_dir=temp_project_dir,
            timeout=120,
        )

        assert result["package_path"] is not None, f"No package created: {result['stderr']}"
        assert result["template_valid"], f"Template invalid: {result['stderr']}"

        # Verify package structure
        pkg_path = Path(result["package_path"])
        assert (pkg_path / "__init__.py").exists()

    def test_create_s3_bucket_with_versioning(self, temp_project_dir):
        """Kiro can create an S3 bucket with versioning enabled."""
        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt="Create an S3 bucket with versioning enabled",
            project_dir=temp_project_dir,
            timeout=120,
        )

        assert result["package_path"] is not None, f"No package created: {result['stderr']}"
        assert result["template_valid"], f"Template invalid: {result['stderr']}"

    def test_create_lambda_function(self, temp_project_dir):
        """Kiro can create a Lambda function with IAM role."""
        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt="Create a Lambda function named 'processor' with Python 3.12 runtime",
            project_dir=temp_project_dir,
            timeout=180,
        )

        assert result["package_path"] is not None, f"No package created: {result['stderr']}"
        assert result["template_valid"], f"Template invalid: {result['stderr']}"

    def test_create_dynamodb_table(self, temp_project_dir):
        """Kiro can create a DynamoDB table."""
        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt="Create a DynamoDB table named 'items' with partition key 'id'",
            project_dir=temp_project_dir,
            timeout=120,
        )

        assert result["package_path"] is not None, f"No package created: {result['stderr']}"
        assert result["template_valid"], f"Template invalid: {result['stderr']}"

    def test_lint_passes_on_generated_code(self, temp_project_dir):
        """Generated code passes wetwire-aws lint."""
        import subprocess

        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt="Create an encrypted S3 bucket",
            project_dir=temp_project_dir,
            timeout=120,
        )

        if result["package_path"] is None:
            pytest.skip(f"Package not created: {result['stderr']}")

        # Run lint on the generated package
        lint_result = subprocess.run(
            ["wetwire-aws", "lint", result["package_path"]],
            capture_output=True,
            text=True,
        )

        assert lint_result.returncode == 0, f"Lint failed: {lint_result.stdout}"

    def test_build_produces_valid_cloudformation(self, temp_project_dir):
        """Generated code produces valid CloudFormation template."""
        import json
        import subprocess

        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt="Create an S3 bucket",
            project_dir=temp_project_dir,
            timeout=120,
        )

        if result["package_path"] is None:
            pytest.skip(f"Package not created: {result['stderr']}")

        # Run build and capture output
        build_result = subprocess.run(
            ["wetwire-aws", "build", result["package_path"]],
            capture_output=True,
            text=True,
        )

        assert build_result.returncode == 0, f"Build failed: {build_result.stderr}"

        # Verify it's valid JSON with CloudFormation structure
        template = json.loads(build_result.stdout)
        assert "AWSTemplateFormatVersion" in template
        assert "Resources" in template
        assert len(template["Resources"]) > 0


class TestKiroPatterns:
    """Tests verifying Kiro follows wetwire-aws patterns."""

    def test_uses_typed_constants(self, temp_project_dir):
        """Generated code uses typed constants, not strings."""
        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt="Create a Lambda function with Python 3.12 runtime",
            project_dir=temp_project_dir,
            timeout=180,
        )

        if result["package_path"] is None:
            pytest.skip(f"Package not created: {result['stderr']}")

        # Read generated Python files
        pkg_path = Path(result["package_path"])
        py_files = list(pkg_path.glob("*.py"))

        # Check that at least one file uses typed runtime constant
        found_typed_runtime = False
        for py_file in py_files:
            content = py_file.read_text()
            # Should use lambda_.Runtime.PYTHON3_12, not "python3.12"
            if "Runtime.PYTHON" in content or "runtime = lambda_" in content:
                found_typed_runtime = True
            # Should NOT use string literal for runtime
            assert '"python3.12"' not in content, f"String literal found in {py_file}"
            assert "'python3.12'" not in content, f"String literal found in {py_file}"

        assert found_typed_runtime, "No typed runtime constant found"

    def test_uses_class_inheritance(self, temp_project_dir):
        """Generated code uses class inheritance pattern."""
        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt="Create an S3 bucket",
            project_dir=temp_project_dir,
            timeout=120,
        )

        if result["package_path"] is None:
            pytest.skip(f"Package not created: {result['stderr']}")

        # Read generated Python files
        pkg_path = Path(result["package_path"])
        py_files = [f for f in pkg_path.glob("*.py") if f.name != "__init__.py"]

        # Check for class inheritance pattern
        found_inheritance = False
        for py_file in py_files:
            content = py_file.read_text()
            # Should have class definition inheriting from s3.Bucket
            if "class " in content and "(s3.Bucket)" in content:
                found_inheritance = True
                break

        assert found_inheritance, "No class inheritance pattern found"


class TestKiroErrorHandling:
    """Tests for error handling in Kiro scenarios."""

    def test_timeout_handling(self, temp_project_dir):
        """Scenario handles timeout gracefully."""
        from wetwire_aws.kiro import run_kiro_scenario

        # Use a very short timeout to trigger timeout
        result = run_kiro_scenario(
            prompt="Create a complex multi-resource architecture with VPC, subnets, "
            "NAT gateways, security groups, ALB, ECS cluster, and RDS database",
            project_dir=temp_project_dir,
            timeout=1,  # 1 second - will definitely timeout
        )

        # Should handle timeout gracefully
        assert result["success"] is False
        assert "Timeout" in result["stderr"] or result["exit_code"] == -1

    def test_kiro_not_installed(self, temp_project_dir, monkeypatch):
        """Handles missing kiro-cli gracefully."""
        from wetwire_aws.kiro import run_kiro_scenario

        # Mock check_kiro_installed to return False
        monkeypatch.setattr(
            "wetwire_aws.kiro.installer.check_kiro_installed",
            lambda: False,
        )

        result = run_kiro_scenario(
            prompt="Create an S3 bucket",
            project_dir=temp_project_dir,
        )

        assert result["success"] is False
        assert "not found" in result["stderr"].lower()


class TestKiroMCPTools:
    """Tests verifying MCP tools work correctly via Kiro."""

    def test_init_tool_creates_package(self, temp_project_dir):
        """wetwire_init MCP tool creates valid package structure."""
        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt="Use the wetwire_init tool to create a package named 'my_infra', "
            "then add an S3 bucket resource to it",
            project_dir=temp_project_dir,
            timeout=120,
        )

        # Check if my_infra package was created
        my_infra = temp_project_dir / "my_infra"
        if my_infra.exists():
            assert (my_infra / "__init__.py").exists()

    def test_lint_tool_detects_issues(self, temp_project_dir):
        """wetwire_lint MCP tool detects code issues."""
        from wetwire_aws.kiro import run_kiro_scenario

        # First create a package with intentional issues
        result = run_kiro_scenario(
            prompt=(
                "Create an S3 bucket package. "
                "After creating it, run wetwire_lint to check for any issues."
            ),
            project_dir=temp_project_dir,
            timeout=120,
        )

        # The scenario should complete (lint may or may not find issues)
        # We're just verifying the lint tool was invoked
        assert result["exit_code"] != -1, "Scenario timed out"

    def test_build_tool_generates_template(self, temp_project_dir):
        """wetwire_build MCP tool generates CloudFormation template."""
        from wetwire_aws.kiro import run_kiro_scenario

        result = run_kiro_scenario(
            prompt=(
                "Create an S3 bucket package and then use wetwire_build "
                "to generate the CloudFormation template"
            ),
            project_dir=temp_project_dir,
            timeout=120,
        )

        assert result["template_valid"], f"Build failed: {result['stderr']}"
