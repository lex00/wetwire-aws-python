"""Integration tests for lint rules."""

from wetwire_aws.linter import (
    StringShouldBeEnum,
    fix_code,
    lint_code,
)


class TestLintCodeIntegration:
    """Integration tests for lint_code with multiple rules."""

    def test_detects_multiple_issue_types(self, mock_enum_available):
        """Should detect issues from multiple rules."""
        code = """
from wetwire_aws.intrinsics import Ref

type = "String"
region = Ref("AWS::Region")
sse_algorithm = "AES256"
"""
        issues = lint_code(code)
        # Should find: STRING, AWS_REGION, ServerSideEncryption.AES256
        assert len(issues) >= 3

        rule_ids = {issue.rule_id for issue in issues}
        assert "WAW001" in rule_ids  # Parameter type
        assert "WAW002" in rule_ids  # Pseudo parameter
        assert "WAW003" in rule_ids  # Enum

    def test_fix_code_fixes_all_issues(self, mock_enum_available):
        """Should fix all detected issues."""
        code = """type = "String"
sse_algorithm = "AES256"
"""
        fixed = fix_code(code, add_imports=False)
        assert "STRING" in fixed
        assert "s3.ServerSideEncryption.AES256" in fixed
        assert '"String"' not in fixed
        assert '"AES256"' not in fixed

    def test_fix_code_no_imports_needed_for_module_qualified(self, mock_enum_available):
        """Module-qualified enums don't need imports (modules available via from . import *)."""
        code = '''sse_algorithm = "AES256"'''
        fixed = fix_code(code, add_imports=True)
        # No explicit import added because s3.ServerSideEncryption.AES256 uses module-qualified name
        assert "from wetwire_aws.resources.s3 import" not in fixed
        assert "s3.ServerSideEncryption.AES256" in fixed


class TestFixCodeImports:
    """Tests for import handling in fix_code."""

    def test_module_qualified_enums_no_imports_needed(self, mock_enum_available):
        """Module-qualified enums don't need explicit imports."""
        code = """
sse_algorithm = "AES256"
status = "Enabled"
"""
        fixed = fix_code(code, add_imports=True, rules=[StringShouldBeEnum()])
        # Should NOT add explicit imports - modules available via from . import *
        assert "from wetwire_aws.resources.s3 import" not in fixed
        assert "s3.ServerSideEncryption.AES256" in fixed
        assert "s3.BucketVersioningStatus.ENABLED" in fixed

    def test_handles_syntax_errors_gracefully(self):
        """Should return original code for syntax errors."""
        code = """this is not valid python"""
        issues = lint_code(code)
        assert len(issues) == 0

        fixed = fix_code(code)
        # Should return unchanged since we can't fix invalid code
        assert "this is not valid python" in fixed
