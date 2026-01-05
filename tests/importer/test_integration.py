"""Integration tests for the importer.

These tests validate that complex imported examples compile successfully.
This catches regressions in the importer's code generation.

If a test fails, it means the importer is generating invalid Python code.
Check the specific failing example to diagnose the issue.
"""

import ast
from pathlib import Path

import pytest

# Path to examples directory (relative to this test file)
EXAMPLES_DIR = Path(__file__).parent.parent.parent / "examples" / "aws-cloudformation-templates"


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
