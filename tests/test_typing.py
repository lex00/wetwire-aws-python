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
    """Tests for type checking of dynamic attributes using ty."""

    def test_resource_arn_attribute_resolves(self):
        """Type checker should resolve .Arn attribute on resources.

        This tests that ResourceMeta.__getattr__ is visible to type checkers,
        enabling patterns like MyBucket.Arn to resolve to AttrRef.
        """
        test_code = '''
from wetwire_aws.base import CloudFormationResource

class MyBucket(CloudFormationResource):
    _resource_type = "AWS::S3::Bucket"

# This should resolve without type errors
arn = MyBucket.Arn
'''
        project_root = Path(__file__).parent.parent

        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.py', delete=False
        ) as f:
            f.write(test_code)
            test_file = f.name

        try:
            # Run ty on the test file with --project to resolve imports
            result = subprocess.run(
                [sys.executable, "-m", "ty", "check", test_file, "--project", str(project_root)],
                capture_output=True,
                text=True,
            )

            # Check for Arn-related errors in output
            if "Arn" in result.stdout or "Arn" in result.stderr:
                raise AssertionError(
                    f"Type checker cannot resolve .Arn attribute:\n{result.stdout}\n{result.stderr}"
                )

            # ty exits 0 on success, non-zero on errors
            assert result.returncode == 0 or "All checks passed" in result.stdout, (
                f"Type checker failed:\n{result.stdout}\n{result.stderr}"
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
        project_root = Path(__file__).parent.parent

        with tempfile.NamedTemporaryFile(
            mode='w', suffix='.py', delete=False
        ) as f:
            f.write(test_code)
            test_file = f.name

        try:
            result = subprocess.run(
                [sys.executable, "-m", "ty", "check", test_file, "--project", str(project_root)],
                capture_output=True,
                text=True,
            )

            if "Arn" in result.stdout or "Arn" in result.stderr:
                raise AssertionError(
                    f"Type checker cannot resolve .Arn on s3.Bucket subclass:\n{result.stdout}\n{result.stderr}"
                )

            assert result.returncode == 0 or "All checks passed" in result.stdout, (
                f"Type checker failed:\n{result.stdout}\n{result.stderr}"
            )
        finally:
            Path(test_file).unlink()
