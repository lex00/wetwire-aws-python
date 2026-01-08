"""Tests for type checking support.

These tests verify that IDEs and type checkers can properly resolve
dynamic attributes like .Arn on CloudFormationResource subclasses.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

# Path to wetwire_aws source
WETWIRE_AWS_SRC = Path(__file__).parent.parent / "src" / "wetwire_aws"


class TestStubFiles:
    """Tests for .pyi stub file existence and content."""

    def test_base_pyi_exists(self):
        """base.pyi stub file should exist for IDE support."""
        stub_file = WETWIRE_AWS_SRC / "base.pyi"
        assert stub_file.exists(), (
            f"base.pyi stub file should exist at {stub_file}"
        )

    def test_base_pyi_declares_resource_meta_getattr(self):
        """base.pyi should declare __getattr__ on ResourceMeta metaclass."""
        stub_file = WETWIRE_AWS_SRC / "base.pyi"
        content = stub_file.read_text()

        assert "class ResourceMeta" in content, (
            "base.pyi should declare ResourceMeta class"
        )
        assert "__getattr__" in content, (
            "base.pyi should declare __getattr__ for IDE attribute resolution"
        )
        assert "AttrRef" in content, (
            "base.pyi should reference AttrRef as the return type"
        )

    def test_base_pyi_declares_cloudformation_resource(self):
        """base.pyi should declare CloudFormationResource with metaclass."""
        stub_file = WETWIRE_AWS_SRC / "base.pyi"
        content = stub_file.read_text()

        assert "CloudFormationResource" in content, (
            "base.pyi should declare CloudFormationResource"
        )


class TestTypingSupport:
    """Tests for type checking of dynamic attributes."""

    def test_resource_arn_attribute_resolves(self):
        """Type checker should resolve .Arn attribute on resources.

        This tests that ResourceMeta.__getattr__ is visible to type checkers,
        enabling patterns like MyBucket.Arn to resolve to AttrRef.
        """
        # Create a test file that uses the .Arn pattern
        test_code = '''
from wetwire_aws.base import CloudFormationResource

class MyBucket(CloudFormationResource):
    _resource_type = "AWS::S3::Bucket"

# This should resolve without type errors
arn = MyBucket.Arn
'''

        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.py', delete=False
        ) as f:
            f.write(test_code)
            test_file = f.name

        try:
            # Run pyright on the test file
            result = subprocess.run(
                [sys.executable, "-m", "pyright", test_file, "--outputjson"],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent.parent,
            )

            # Check for "Arn" related errors
            import json
            try:
                output = json.loads(result.stdout)
                diagnostics = output.get("generalDiagnostics", [])

                # Filter for errors about "Arn" attribute
                arn_errors = [
                    d for d in diagnostics
                    if "Arn" in d.get("message", "")
                ]

                assert len(arn_errors) == 0, (
                    f"Type checker cannot resolve .Arn attribute: {arn_errors}"
                )
            except json.JSONDecodeError:
                # If pyright output isn't JSON, check stderr for errors
                if "Cannot access attribute \"Arn\"" in result.stdout:
                    raise AssertionError(
                        f"Type checker cannot resolve .Arn: {result.stdout}"
                    )
        finally:
            Path(test_file).unlink()

    def test_service_resource_arn_attribute_resolves(self):
        """Type checker should resolve .Arn on service resources like s3.Bucket.

        This tests the full inheritance chain:
        UserBucket -> s3.Bucket -> CloudFormationResource -> ResourceMeta
        """
        test_code = '''
from wetwire_aws.resources import s3

class MyBucket(s3.Bucket):
    bucket_name = "my-bucket"

# This should resolve without type errors
arn = MyBucket.Arn
'''

        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.py', delete=False
        ) as f:
            f.write(test_code)
            test_file = f.name

        try:
            result = subprocess.run(
                [sys.executable, "-m", "pyright", test_file, "--outputjson"],
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent.parent,
            )

            import json
            try:
                output = json.loads(result.stdout)
                diagnostics = output.get("generalDiagnostics", [])

                arn_errors = [
                    d for d in diagnostics
                    if "Arn" in d.get("message", "")
                ]

                assert len(arn_errors) == 0, (
                    f"Type checker cannot resolve .Arn on s3.Bucket subclass: {arn_errors}"
                )
            except json.JSONDecodeError:
                if "Cannot access attribute \"Arn\"" in result.stdout:
                    raise AssertionError(
                        f"Type checker cannot resolve .Arn: {result.stdout}"
                    )
        finally:
            Path(test_file).unlink()
