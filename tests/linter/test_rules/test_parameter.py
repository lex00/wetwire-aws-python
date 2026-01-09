"""Tests for WAW001: parameter type string literals."""

import pytest

from wetwire_aws.linter import (
    StringShouldBeParameterType,
    fix_code,
    lint_code,
)


class TestStringShouldBeParameterType:
    """Tests for WAW001: parameter type string literals."""

    @pytest.mark.parametrize(
        "type_str,expected_constant",
        [
            ("String", "STRING"),
            ("Number", "NUMBER"),
            ("List<Number>", "LIST_NUMBER"),
            ("CommaDelimitedList", "COMMA_DELIMITED_LIST"),
        ],
    )
    def test_detects_parameter_type(self, type_str, expected_constant):
        """Should detect type = 'Type' and suggest constant."""
        code = f'''type = "{type_str}"'''
        issues = lint_code(code, rules=[StringShouldBeParameterType()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW001"
        assert expected_constant in issues[0].suggestion

    def test_detects_type_in_kwargs(self):
        """Should detect type in keyword arguments."""
        code = '''param = Parameter(type="String", description="Test")'''
        issues = lint_code(code, rules=[StringShouldBeParameterType()])
        assert len(issues) == 1
        assert "STRING" in issues[0].suggestion

    def test_ignores_non_parameter_types(self):
        """Should not flag arbitrary string assignments to type."""
        code = '''type = "CustomType"'''
        issues = lint_code(code, rules=[StringShouldBeParameterType()])
        assert len(issues) == 0

    def test_fix_replaces_string(self):
        """Should replace 'String' with STRING."""
        code = '''type = "String"'''
        fixed = fix_code(code, rules=[StringShouldBeParameterType()], add_imports=False)
        assert "STRING" in fixed
        assert '"String"' not in fixed
