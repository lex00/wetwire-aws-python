"""Tests for stub generation."""

import re
from pathlib import Path


class TestStubConfig:
    """Tests for AWS_STUB_CONFIG."""

    def test_core_exports_does_not_include_all_services(self):
        """Core exports should only include essential types, not all 263 services."""
        from wetwire_aws.stubs import AWS_CORE_EXPORTS

        # Core exports should be a reasonable size (not 263+ services)
        assert len(AWS_CORE_EXPORTS) < 100

        # Should include essential types
        assert "wetwire_aws" in AWS_CORE_EXPORTS
        assert "CloudFormationResource" in AWS_CORE_EXPORTS
        assert "Parameter" in AWS_CORE_EXPORTS
        assert "Output" in AWS_CORE_EXPORTS

        # Should NOT include service modules
        assert "s3" not in AWS_CORE_EXPORTS
        assert "ec2" not in AWS_CORE_EXPORTS
        assert "lambda_" not in AWS_CORE_EXPORTS
        assert "serverless" not in AWS_CORE_EXPORTS

    def test_extra_header_does_not_import_all_services(self):
        """Extra header lines should not import all 263 service modules."""
        from wetwire_aws.stubs import AWS_STUB_CONFIG

        # Count service module imports in header
        header_text = "\n".join(AWS_STUB_CONFIG.extra_header_lines)

        # Should not contain bulk service imports
        assert "from wetwire_aws.resources import (" not in header_text

        # Check we're not importing all services
        service_count = len(
            re.findall(r"\b(s3|ec2|lambda_|iam|dynamodb)\b", header_text)
        )
        assert service_count < 10  # A few references is fine, but not 263

    def test_stub_config_expand_star_imports_minimal(self):
        """expand_star_imports should not include all service modules."""
        from wetwire_aws.stubs import AWS_STUB_CONFIG

        # Get the wetwire_aws star import expansion
        star_imports = AWS_STUB_CONFIG.expand_star_imports.get("wetwire_aws", [])

        # Should not include all 263 service modules
        assert len(star_imports) < 150  # Core types + reasonable overhead

        # Should include essential types
        assert "wetwire_aws" in star_imports
        assert "Parameter" in star_imports


class TestGeneratedStubs:
    """Tests for generated stub files."""

    def test_generated_stub_is_not_bloated(self, tmp_path: Path):
        """Generated stub should be reasonably sized."""
        # Create a minimal test package
        pkg_dir = tmp_path / "test_pkg"
        pkg_dir.mkdir()

        init_content = '''"""Test package."""
from wetwire_aws.loader import setup_params, setup_resources

setup_params(globals())

from .params import *  # noqa: F403, F401

setup_resources(__file__, __name__, globals())
'''
        (pkg_dir / "__init__.py").write_text(init_content)

        params_content = '''"""Parameters."""
from . import *  # noqa: F403

class MyParam(Parameter):
    type = STRING
    default = "test"
'''
        (pkg_dir / "params.py").write_text(params_content)

        resources_content = '''"""Resources."""
from . import *  # noqa: F403

class MyBucket(s3.Bucket):
    resource: s3.Bucket
    bucket_name = "my-bucket"
'''
        (pkg_dir / "main.py").write_text(resources_content)

        # Import the package to trigger stub generation
        import sys

        sys.path.insert(0, str(tmp_path))
        try:
            import test_pkg  # noqa: F401
        finally:
            sys.path.remove(str(tmp_path))
            if "test_pkg" in sys.modules:
                del sys.modules["test_pkg"]

        # Check the generated stub
        stub_file = pkg_dir / "__init__.pyi"
        if stub_file.exists():
            stub_content = stub_file.read_text()
            stub_lines = stub_content.count("\n")

            # Stub should not be bloated (less than 200 lines for a simple package)
            assert stub_lines < 200, f"Stub is too large: {stub_lines} lines"

            # Should not contain bulk service imports
            assert stub_content.count("from wetwire_aws.resources import") <= 1

    def test_stub_has_no_duplicate_imports(self, tmp_path: Path):
        """Generated stub should not have duplicate import statements."""
        # Create a minimal test package
        pkg_dir = tmp_path / "test_pkg2"
        pkg_dir.mkdir()

        init_content = '''"""Test package."""
from wetwire_aws.loader import setup_params, setup_resources

setup_params(globals())

setup_resources(__file__, __name__, globals())
'''
        (pkg_dir / "__init__.py").write_text(init_content)

        # Import the package to trigger stub generation
        import sys

        sys.path.insert(0, str(tmp_path))
        try:
            import test_pkg2  # noqa: F401
        finally:
            sys.path.remove(str(tmp_path))
            if "test_pkg2" in sys.modules:
                del sys.modules["test_pkg2"]

        # Check the generated stub
        stub_file = pkg_dir / "__init__.pyi"
        if stub_file.exists():
            stub_content = stub_file.read_text()

            # Count actual import statements (not comments or __all__)
            import_lines = [
                line
                for line in stub_content.split("\n")
                if line.strip().startswith("from wetwire_aws.loader import")
            ]

            # Should have at most one import from wetwire_aws.loader
            assert len(import_lines) <= 1, (
                f"Duplicate loader imports found: {import_lines}"
            )
