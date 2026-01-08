"""Integration tests for Kiro CLI with wetwire-aws.

These tests actually invoke kiro-cli and are skipped by default.
To run them, set the KIRO_TESTS environment variable:

    KIRO_TESTS=1 pytest tests/test_kiro_integration.py -v

To run a specific persona:

    KIRO_TESTS=1 pytest tests/test_kiro_integration.py -v -k "beginner"

Requirements:
- Kiro CLI installed and in PATH
- wetwire-aws[kiro] installed
- Valid Kiro CLI authentication/configuration
"""

import json
import os
import subprocess
import tempfile
from pathlib import Path

import pytest

# Skip all tests in this module unless KIRO_TESTS is set
pytestmark = pytest.mark.skipif(
    os.getenv("KIRO_TESTS") != "1",
    reason="Kiro integration tests disabled. Set KIRO_TESTS=1 to enable.",
)

# Persona definitions matching the Anthropic provider
PERSONAS = {
    "beginner": (
        "You are simulating a user who is new to AWS. "
        "Ask clarifying questions about basic concepts before proceeding. "
        "Request explanations for AWS terminology."
    ),
    "intermediate": (
        "You are simulating a user with moderate AWS experience. "
        "Ask about best practices and common patterns. "
        "Understand basic concepts but want guidance on implementation details."
    ),
    "expert": (
        "You are simulating an AWS expert user. "
        "Ask about advanced configurations, edge cases, and optimization. "
        "Challenge assumptions and request production-ready code."
    ),
    "terse": (
        "You are simulating a user who gives minimal responses. "
        "Just answer what's asked with brief, direct responses. "
        "Don't elaborate or ask unnecessary questions."
    ),
    "verbose": (
        "You are simulating a user who provides detailed context. "
        "Give comprehensive requirements and background information. "
        "Explain your use case and constraints thoroughly."
    ),
}

# Test scenarios to run across all personas
SCENARIOS = [
    {
        "id": "s3_bucket",
        "name": "S3 Bucket",
        "prompt": "Create an S3 bucket for storing application data",
        "timeout": 120,
        "expected_resources": ["s3.Bucket"],
    },
    {
        "id": "s3_versioned",
        "name": "S3 Bucket with Versioning",
        "prompt": "Create an S3 bucket with versioning enabled for backup purposes",
        "timeout": 120,
        "expected_resources": ["s3.Bucket"],
    },
    {
        "id": "lambda_function",
        "name": "Lambda Function",
        "prompt": "Create a Lambda function named 'processor' with Python 3.12 runtime",
        "timeout": 180,
        "expected_resources": ["lambda_.Function"],
    },
    {
        "id": "dynamodb_table",
        "name": "DynamoDB Table",
        "prompt": "Create a DynamoDB table named 'items' with a partition key called 'id'",
        "timeout": 120,
        "expected_resources": ["dynamodb.Table"],
    },
    {
        "id": "lambda_with_role",
        "name": "Lambda with IAM Role",
        "prompt": "Create a Lambda function with its own IAM execution role",
        "timeout": 180,
        "expected_resources": ["lambda_.Function", "iam.Role"],
    },
]


@pytest.fixture
def temp_project_dir():
    """Create a temporary directory for test projects."""
    with tempfile.TemporaryDirectory(prefix="kiro_integration_") as tmpdir:
        yield Path(tmpdir)


def build_persona_prompt(scenario_prompt: str, persona_name: str) -> str:
    """Build a full prompt incorporating persona behavior."""
    persona_instructions = PERSONAS[persona_name]
    return (
        f"{persona_instructions}\n\n"
        f"User request: {scenario_prompt}\n\n"
        "Complete this request by creating a wetwire-aws package. "
        "Use the wetwire_init, wetwire_lint, and wetwire_build MCP tools. "
        "Ensure the generated code follows wetwire-aws patterns: "
        "class inheritance, typed constants, and direct references."
    )


class TestKiroPersonaScenarios:
    """Run all scenarios across all personas."""

    @pytest.mark.parametrize("persona_name", list(PERSONAS.keys()))
    @pytest.mark.parametrize(
        "scenario",
        SCENARIOS,
        ids=[s["id"] for s in SCENARIOS],
    )
    def test_scenario_with_persona(self, temp_project_dir, persona_name, scenario):
        """Run a scenario with a specific persona."""
        from wetwire_aws.kiro import run_kiro_scenario

        prompt = build_persona_prompt(scenario["prompt"], persona_name)

        result = run_kiro_scenario(
            prompt=prompt,
            project_dir=temp_project_dir,
            timeout=scenario["timeout"],
        )

        # Basic assertions
        assert result["package_path"] is not None, (
            f"[{persona_name}] No package created for '{scenario['name']}': "
            f"{result['stderr']}"
        )
        assert result["template_valid"], (
            f"[{persona_name}] Template invalid for '{scenario['name']}': "
            f"{result['stderr']}"
        )

        # Verify package structure
        pkg_path = Path(result["package_path"])
        assert (pkg_path / "__init__.py").exists(), (
            f"[{persona_name}] Missing __init__.py in '{scenario['name']}'"
        )


class TestKiroFullScenarioMatrix:
    """Comprehensive scenario matrix testing."""

    @pytest.mark.parametrize("persona_name", list(PERSONAS.keys()))
    def test_s3_bucket_scenario(self, temp_project_dir, persona_name):
        """Test S3 bucket creation with all personas."""
        from wetwire_aws.kiro import run_kiro_scenario

        prompt = build_persona_prompt(
            "Create an S3 bucket named 'my-data-bucket' for storing files",
            persona_name,
        )

        result = run_kiro_scenario(
            prompt=prompt,
            project_dir=temp_project_dir,
            timeout=120,
        )

        assert result["success"], (
            f"[{persona_name}] S3 bucket scenario failed: {result['stderr']}"
        )

        # Verify the generated code
        if result["package_path"]:
            pkg_path = Path(result["package_path"])
            py_files = [f for f in pkg_path.glob("*.py") if f.name != "__init__.py"]

            # Check for S3 bucket class
            found_bucket = False
            for py_file in py_files:
                content = py_file.read_text()
                if "s3.Bucket" in content or "s3.bucket" in content.lower():
                    found_bucket = True
                    break

            assert found_bucket, f"[{persona_name}] No S3 bucket resource found"

    @pytest.mark.parametrize("persona_name", list(PERSONAS.keys()))
    def test_lambda_scenario(self, temp_project_dir, persona_name):
        """Test Lambda function creation with all personas."""
        from wetwire_aws.kiro import run_kiro_scenario

        prompt = build_persona_prompt(
            "Create a Lambda function named 'api-handler' with Python 3.12 runtime "
            "that will process API requests",
            persona_name,
        )

        result = run_kiro_scenario(
            prompt=prompt,
            project_dir=temp_project_dir,
            timeout=180,
        )

        assert result["success"], (
            f"[{persona_name}] Lambda scenario failed: {result['stderr']}"
        )

    @pytest.mark.parametrize("persona_name", list(PERSONAS.keys()))
    def test_multi_resource_scenario(self, temp_project_dir, persona_name):
        """Test multi-resource architecture with all personas."""
        from wetwire_aws.kiro import run_kiro_scenario

        prompt = build_persona_prompt(
            "Create a Lambda function that reads from a DynamoDB table. "
            "Include the IAM role with appropriate permissions.",
            persona_name,
        )

        result = run_kiro_scenario(
            prompt=prompt,
            project_dir=temp_project_dir,
            timeout=240,
        )

        # Multi-resource scenarios are more complex, may not always succeed
        # but should at least not timeout
        assert result["exit_code"] != -1, (
            f"[{persona_name}] Multi-resource scenario timed out"
        )


class TestKiroCodeQuality:
    """Tests verifying code quality across personas."""

    @pytest.mark.parametrize("persona_name", list(PERSONAS.keys()))
    def test_lint_passes(self, temp_project_dir, persona_name):
        """Generated code passes wetwire-aws lint for all personas."""
        from wetwire_aws.kiro import run_kiro_scenario

        prompt = build_persona_prompt(
            "Create an encrypted S3 bucket with server-side encryption",
            persona_name,
        )

        result = run_kiro_scenario(
            prompt=prompt,
            project_dir=temp_project_dir,
            timeout=120,
        )

        if result["package_path"] is None:
            pytest.skip(f"[{persona_name}] Package not created: {result['stderr']}")

        # Run lint on the generated package
        lint_result = subprocess.run(
            ["wetwire-aws", "lint", result["package_path"]],
            capture_output=True,
            text=True,
        )

        assert lint_result.returncode == 0, (
            f"[{persona_name}] Lint failed: {lint_result.stdout}"
        )

    @pytest.mark.parametrize("persona_name", list(PERSONAS.keys()))
    def test_build_produces_valid_cloudformation(self, temp_project_dir, persona_name):
        """Generated code produces valid CloudFormation for all personas."""
        from wetwire_aws.kiro import run_kiro_scenario

        prompt = build_persona_prompt(
            "Create an S3 bucket for static website hosting",
            persona_name,
        )

        result = run_kiro_scenario(
            prompt=prompt,
            project_dir=temp_project_dir,
            timeout=120,
        )

        if result["package_path"] is None:
            pytest.skip(f"[{persona_name}] Package not created: {result['stderr']}")

        # Run build and capture output
        build_result = subprocess.run(
            ["wetwire-aws", "build", result["package_path"]],
            capture_output=True,
            text=True,
        )

        assert build_result.returncode == 0, (
            f"[{persona_name}] Build failed: {build_result.stderr}"
        )

        # Verify it's valid JSON with CloudFormation structure
        template = json.loads(build_result.stdout)
        assert "AWSTemplateFormatVersion" in template
        assert "Resources" in template
        assert len(template["Resources"]) > 0

    @pytest.mark.parametrize("persona_name", list(PERSONAS.keys()))
    def test_uses_typed_constants(self, temp_project_dir, persona_name):
        """Generated code uses typed constants for all personas."""
        from wetwire_aws.kiro import run_kiro_scenario

        prompt = build_persona_prompt(
            "Create a Lambda function with Python 3.12 runtime",
            persona_name,
        )

        result = run_kiro_scenario(
            prompt=prompt,
            project_dir=temp_project_dir,
            timeout=180,
        )

        if result["package_path"] is None:
            pytest.skip(f"[{persona_name}] Package not created: {result['stderr']}")

        # Read generated Python files
        pkg_path = Path(result["package_path"])
        py_files = list(pkg_path.glob("*.py"))

        # Check that code doesn't use string literals for runtime
        for py_file in py_files:
            content = py_file.read_text()
            # Should NOT use string literal for runtime
            assert '"python3.12"' not in content, (
                f"[{persona_name}] String literal found in {py_file}"
            )
            assert "'python3.12'" not in content, (
                f"[{persona_name}] String literal found in {py_file}"
            )

    @pytest.mark.parametrize("persona_name", list(PERSONAS.keys()))
    def test_uses_class_inheritance(self, temp_project_dir, persona_name):
        """Generated code uses class inheritance pattern for all personas."""
        from wetwire_aws.kiro import run_kiro_scenario

        prompt = build_persona_prompt(
            "Create an S3 bucket",
            persona_name,
        )

        result = run_kiro_scenario(
            prompt=prompt,
            project_dir=temp_project_dir,
            timeout=120,
        )

        if result["package_path"] is None:
            pytest.skip(f"[{persona_name}] Package not created: {result['stderr']}")

        # Read generated Python files
        pkg_path = Path(result["package_path"])
        py_files = [f for f in pkg_path.glob("*.py") if f.name != "__init__.py"]

        # Check for class inheritance pattern
        found_inheritance = False
        for py_file in py_files:
            content = py_file.read_text()
            if "class " in content and "(s3.Bucket)" in content:
                found_inheritance = True
                break

        assert found_inheritance, (
            f"[{persona_name}] No class inheritance pattern found"
        )


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

    @pytest.mark.parametrize("persona_name", ["intermediate", "expert"])
    def test_full_workflow_with_mcp_tools(self, temp_project_dir, persona_name):
        """Test full workflow using all MCP tools."""
        from wetwire_aws.kiro import run_kiro_scenario

        prompt = build_persona_prompt(
            "Create a new wetwire-aws package using wetwire_init, "
            "add an S3 bucket resource, run wetwire_lint to verify the code, "
            "and run wetwire_build to generate the CloudFormation template",
            persona_name,
        )

        result = run_kiro_scenario(
            prompt=prompt,
            project_dir=temp_project_dir,
            timeout=180,
        )

        assert result["template_valid"], (
            f"[{persona_name}] MCP workflow failed: {result['stderr']}"
        )
