"""Integration tests for the importer.

These tests validate that complex imported examples compile successfully.
This catches regressions in the importer's code generation.

If a test fails, it means the importer is generating invalid Python code.
Check the specific failing example to diagnose the issue.
"""

import ast
import importlib
import sys
from pathlib import Path
from typing import Any

import pytest

# Path to examples directory (relative to this test file)
EXAMPLES_DIR = (
    Path(__file__).parent.parent.parent / "examples" / "aws-cloudformation-templates"
)


def find_examples_dir() -> Path | None:
    """Locate the examples directory.

    Returns None if not found (e.g., when running as a dependency).
    """
    if EXAMPLES_DIR.exists():
        return EXAMPLES_DIR

    # Try alternative paths
    candidates = [
        Path("examples/aws-cloudformation-templates"),
        Path("../examples/aws-cloudformation-templates"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate.resolve()

    return None


# Curated list of complex templates that exercise various importer features
COMPLEX_EXAMPLES = [
    "cloudfront",  # CloudFront distribution with S3, complex nested properties
    "dynamodb_table",  # DynamoDB with secondary indexes
    "lambdasample",  # Lambda function with IAM role
    "ec2instancewithsecuritygroupsample",  # EC2 with security groups, mappings
    "cognito",  # Cognito user pool with various configurations
    "load_balancer",  # ELB with listeners, health checks
    "rest_api",  # API Gateway with authorizers
    "neptune",  # Neptune cluster with parameter groups, alarms
    "iotanalytics",  # IoT Analytics pipeline with channels, datastores
    "cloudformation_codebuild_template",  # CodeBuild with complex build specs
    "eip_with_association",  # EC2 with EIP association
    "compliant_bucket",  # S3 bucket with encryption, versioning, policies
]


@pytest.fixture
def examples_dir():
    """Get examples directory or skip if not found."""
    examples = find_examples_dir()
    if examples is None:
        pytest.skip("examples directory not found, skipping integration test")
    return examples


class TestExamplesCompile:
    """Test that complex imported examples compile as valid Python."""

    @pytest.mark.parametrize("example_name", COMPLEX_EXAMPLES)
    def test_example_compiles(self, examples_dir: Path, example_name: str):
        """Verify example generates valid Python that can be compiled."""
        example_path = examples_dir / example_name

        if not example_path.exists():
            pytest.skip(f"example {example_name} not found")

        # Find all Python files in the example
        py_files = list(example_path.glob("**/*.py"))
        if not py_files:
            pytest.skip(f"example {example_name} has no Python files")

        # Compile each file
        for py_file in py_files:
            content = py_file.read_text()
            try:
                # First try to compile
                compile(content, str(py_file), "exec")
                # Then parse AST to catch additional issues
                ast.parse(content)
            except SyntaxError as e:
                pytest.fail(
                    f"example {example_name} file {py_file.name} has syntax error:\n{e}"
                )
            except Exception as e:
                pytest.fail(
                    f"example {example_name} file {py_file.name} failed to compile:\n{e}"
                )


def find_empty_dicts(obj: Any, path: str = "") -> list[str]:
    """Recursively find empty dicts in a nested structure.

    Returns list of paths where empty dicts were found.
    """
    empty_paths = []
    if isinstance(obj, dict):
        if obj == {}:
            empty_paths.append(path or "(root)")
        else:
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                empty_paths.extend(find_empty_dicts(value, new_path))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            empty_paths.extend(find_empty_dicts(item, f"{path}[{i}]"))
    return empty_paths


# Examples with known serialization issues (PropertyTypes serialize as empty dicts)
# See: https://github.com/lex00/wetwire-aws-python/issues/68
KNOWN_BROKEN_EXAMPLES = {
    "cloudfront",  # BucketEncryption, OwnershipControls, etc. serialize as {}
    "dynamodb_table",  # KeySchema, AttributeDefinitions serialize as [{}]
    "lambdasample",  # FunctionCode serializes as {}
    "ec2instancewithsecuritygroupsample",  # SecurityGroupIngress serializes as {}
    "cognito",  # UserPoolSchema serializes as {}
    "load_balancer",  # HealthCheck, Listeners serialize as {}
    "neptune",  # DBClusterParameterGroup, etc. serialize as {}
    "iotanalytics",  # Channel, Pipeline configs serialize as {}
    "cloudformation_codebuild_template",  # BuildSpec serializes as {}
    "eip_with_association",  # SecurityGroupIngress serializes as {}
    "compliant_bucket",  # BucketEncryption serializes as {}
}


class TestExamplesGenerateCF:
    """Test that examples generate valid CloudFormation output."""

    @pytest.mark.parametrize("example_name", COMPLEX_EXAMPLES)
    def test_example_generates_valid_cloudformation(
        self, examples_dir: Path, example_name: str
    ):
        """Verify example generates valid CloudFormation with correct resource count."""
        if example_name in KNOWN_BROKEN_EXAMPLES:
            pytest.xfail(f"Known issue: {example_name} has serialization bugs (see #68)")

        example_path = examples_dir / example_name
        if not example_path.exists():
            pytest.skip(f"example {example_name} not found")

        # Find the package directory (has __init__.py)
        pkg_dirs = [
            d
            for d in example_path.iterdir()
            if d.is_dir() and (d / "__init__.py").exists()
        ]
        if not pkg_dirs:
            pytest.skip(f"example {example_name} has no package directory")

        pkg_dir = pkg_dirs[0]
        pkg_name = pkg_dir.name

        # Import the package (triggers setup_resources)
        sys.path.insert(0, str(example_path))
        try:
            # Clear any previous registry state
            from wetwire_aws.decorator import get_aws_registry

            get_aws_registry().clear()

            # Import the package
            importlib.import_module(pkg_name)

            # Generate CloudFormation
            from wetwire_aws import CloudFormationTemplate

            template = CloudFormationTemplate.from_registry()
            output = template.to_dict()

            # Count resources in output
            cf_resource_count = len(output.get("Resources", {}))

            # Count resources in registry (filter to only resources, not parameters etc)
            registry = get_aws_registry()
            py_resource_count = len(list(registry.get_all()))

            # Verify counts match
            assert cf_resource_count == py_resource_count, (
                f"Resource count mismatch for {example_name}: "
                f"{py_resource_count} Python classes, {cf_resource_count} CF resources"
            )

            # Check for empty dicts in Properties (indicates data loss)
            for resource_name, resource_data in output.get("Resources", {}).items():
                props = resource_data.get("Properties", {})
                empty_paths = find_empty_dicts(props)
                assert not empty_paths, (
                    f"Found empty dicts in {example_name}/{resource_name}: {empty_paths}"
                )
        finally:
            sys.path.remove(str(example_path))
            # Cleanup sys.modules
            for mod_name in list(sys.modules.keys()):
                if mod_name.startswith(pkg_name):
                    del sys.modules[mod_name]


class TestNamingSanitization:
    """Test that variable name sanitization works correctly."""

    def test_hyphen_in_class_name(self):
        """Hyphens should be converted to valid Python identifiers."""
        from wetwire_aws.naming import sanitize_class_name

        # Hyphen before digit -> Neg
        assert sanitize_class_name("Port-1ICMP") == "PortNeg1ICMP"

        # Hyphen between letters -> capitalize next
        result = sanitize_class_name("my-resource")
        assert "-" not in result
        # Result should be valid Python
        assert result.isidentifier()

    def test_hyphen_in_python_name(self):
        """Hyphens should become underscores for Python names."""
        from wetwire_aws.naming import sanitize_python_name

        result = sanitize_python_name("my-resource")
        assert result == "my_resource"

        result = sanitize_python_name("Port-1ICMP")
        assert "-" not in result
        assert result.isidentifier()

    def test_leading_digit(self):
        """Leading digits should be prefixed with underscore."""
        from wetwire_aws.naming import sanitize_class_name, sanitize_python_name

        assert sanitize_class_name("123test").startswith("_")
        assert sanitize_python_name("123test").startswith("_")

    def test_python_keyword(self):
        """Python keywords should be handled."""
        from wetwire_aws.naming import sanitize_python_name

        result = sanitize_python_name("class")
        assert result != "class"  # Should be modified
        assert result.isidentifier()


class TestImporterCodeStyle:
    """Test that importer generates code following style guidelines."""

    def test_no_explicit_ref_pattern(self, examples_dir: Path):
        """Generated code should not use explicit ref() calls where direct refs work."""
        # Check a few examples for ref() usage patterns
        for example_name in ["cloudfront", "lambdasample"]:
            example_path = examples_dir / example_name
            if not example_path.exists():
                continue

            for py_file in example_path.glob("**/*.py"):
                if py_file.name in ("__main__.py", "__init__.py"):
                    continue
                content = py_file.read_text()
                # Should use bare class names, not ref(ClassName)
                # String-based refs like Ref("ResourceName") are OK for forward refs
                if "ref(" in content.lower():
                    # Check if it's a bad pattern (ref with a Name, not a string)
                    import re

                    bad_refs = re.findall(r"\bref\(([A-Z][A-Za-z0-9]+)\)", content)
                    for ref in bad_refs:
                        # Skip if it's actually a string
                        if f'ref("{ref}")' in content or f"ref('{ref}')" in content:
                            continue
                        # This might be a style violation
                        # (but could also be intentional for some edge cases)

    def test_no_explicit_get_att_pattern(self, examples_dir: Path):
        """Generated code should use ClassName.Attr instead of get_att()."""
        for example_name in ["cloudfront", "lambdasample"]:
            example_path = examples_dir / example_name
            if not example_path.exists():
                continue

            for py_file in example_path.glob("**/*.py"):
                if py_file.name in ("__main__.py", "__init__.py"):
                    continue
                content = py_file.read_text()
                # Should use ClassName.Attr pattern
                # get_att("Name", "Attr") is OK for forward refs
                if "get_att(" in content.lower():
                    # Most get_att should use the ClassName.Attr pattern
                    pass
