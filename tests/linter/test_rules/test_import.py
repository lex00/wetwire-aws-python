"""Tests for import-related rules.

Rules:
    WAW007: Use flat imports with module-qualified names
    WAW008: Remove verbose imports
    WAW018: Remove redundant relative imports
"""

from wetwire_aws.linter import (
    ExplicitResourceImport,
    fix_code,
    lint_code,
)
from wetwire_aws.linter.rules import (
    RedundantRelativeImport,
    VerboseInitImports,
)


class TestExplicitResourceImport:
    """Tests for WAW007: explicit resource imports."""

    def test_detects_lambda_runtime_import(self):
        """Should detect from wetwire_aws.resources.lambda_ import Runtime."""
        code = '''from wetwire_aws.resources.lambda_ import Runtime'''
        issues = lint_code(code, rules=[ExplicitResourceImport()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW007"
        assert "Remove explicit resource import" in issues[0].message

    def test_detects_s3_enum_import(self):
        """Should detect from wetwire_aws.resources.s3 import ServerSideEncryption."""
        code = '''from wetwire_aws.resources.s3 import ServerSideEncryption'''
        issues = lint_code(code, rules=[ExplicitResourceImport()])
        assert len(issues) == 1
        assert "Remove explicit resource import" in issues[0].message

    def test_detects_multiple_imports_same_line(self):
        """Should detect one issue per import line (not per imported name)."""
        code = '''from wetwire_aws.resources.lambda_ import Runtime, Architecture'''
        issues = lint_code(code, rules=[ExplicitResourceImport()])
        # Now only 1 issue per import line
        assert len(issues) == 1

    def test_ignores_non_resource_imports(self):
        """Should not flag imports from wetwire_aws (not wetwire_aws.resources)."""
        code = """
from wetwire_aws import wetwire_aws
from wetwire_aws.intrinsics import Sub
"""
        issues = lint_code(code, rules=[ExplicitResourceImport()])
        assert len(issues) == 0

    def test_fix_removes_import_line(self):
        """Should remove the explicit import line."""
        code = '''from wetwire_aws.resources.lambda_ import Runtime'''
        fixed = fix_code(code, rules=[ExplicitResourceImport()], add_imports=False)
        assert "from wetwire_aws.resources.lambda_" not in fixed

    def test_qualifies_usages_of_imported_names(self):
        """Should qualify usages like Runtime.PYTHON3_12 -> lambda_.Runtime.PYTHON3_12."""
        code = """from wetwire_aws.resources.lambda_ import Runtime
runtime = Runtime.PYTHON3_12
"""
        issues = lint_code(code, rules=[ExplicitResourceImport()])
        # Should have 2 issues: 1 for import, 1 for usage
        assert len(issues) == 2
        # Filter for usage issues (ones that have a non-empty suggestion)
        usage_issues = [
            i for i in issues if i.suggestion and "lambda_.Runtime" in i.suggestion
        ]
        assert len(usage_issues) == 1
        assert usage_issues[0].suggestion == "lambda_.Runtime.PYTHON3_12"

    def test_fix_qualifies_and_removes_import(self):
        """Should both remove import and qualify usages."""
        code = """from wetwire_aws.resources.lambda_ import Runtime
runtime = Runtime.PYTHON3_12
"""
        fixed = fix_code(code, rules=[ExplicitResourceImport()], add_imports=False)
        assert "from wetwire_aws.resources.lambda_" not in fixed
        assert "lambda_.Runtime.PYTHON3_12" in fixed

    def test_detects_redundant_module_imports_in_init(self):
        """Should detect redundant module imports in __init__.py with setup_resources."""
        code = """from wetwire_aws.loader import setup_resources
from wetwire_aws.resources import ec2, lambda_
setup_resources(__file__, __name__, globals())
"""
        issues = lint_code(code, rules=[ExplicitResourceImport()])
        assert len(issues) == 1
        assert "setup_resources()" in issues[0].message


class TestVerboseInitImports:
    """Tests for WAW008: verbose imports in __init__.py."""

    def test_detects_verbose_wetwire_import(self):
        """Should detect verbose multi-line wetwire_aws imports."""
        code = """from wetwire_aws.loader import setup_resources
from wetwire_aws import (
    Sub,
    Join,
    Ref,
)
setup_resources(__file__, __name__, globals())
"""
        issues = lint_code(code, rules=[VerboseInitImports()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW008"
        assert "setup_params()" in issues[0].message

    def test_detects_all_block(self):
        """Should detect __all__ = [...] blocks."""
        code = """from wetwire_aws.loader import setup_resources
__all__ = [
    "MyBucket",
    "MyRole",
]
setup_resources(__file__, __name__, globals())
"""
        issues = lint_code(code, rules=[VerboseInitImports()])
        assert len(issues) == 1
        assert "__all__" in issues[0].message

    def test_ignores_non_init_files(self):
        """Should not flag verbose imports in non-__init__ files."""
        code = """from wetwire_aws import (
    Sub,
    Join,
)
"""
        issues = lint_code(code, rules=[VerboseInitImports()])
        # No setup_resources means not an __init__ file
        assert len(issues) == 0


class TestRedundantRelativeImport:
    """Tests for WAW018: redundant relative imports."""

    def test_detects_redundant_import_with_star(self):
        """Should detect redundant import when from . import * exists."""
        code = """from . import *
from .network import MyVPC
"""
        issues = lint_code(code, rules=[RedundantRelativeImport()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW018"
        assert "MyVPC" in issues[0].message

    def test_ignores_when_no_star_import(self):
        """Should not flag when no star import exists."""
        code = """from .network import MyVPC
from .storage import MyBucket
"""
        issues = lint_code(code, rules=[RedundantRelativeImport()])
        assert len(issues) == 0

    def test_detects_multiple_redundant_imports(self):
        """Should detect all redundant imports."""
        code = """from . import *
from .network import MyVPC
from .storage import MyBucket
"""
        issues = lint_code(code, rules=[RedundantRelativeImport()])
        assert len(issues) == 2
