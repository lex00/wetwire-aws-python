"""Tests for WAW006: ref()/get_att() should use no-parens style."""

from wetwire_aws.linter import (
    RefShouldBeNoParens,
    fix_code,
    lint_code,
)


class TestRefShouldBeNoParens:
    """Tests for WAW006: ref()/get_att() should use no-parens style."""

    def test_detects_ref_with_class_name(self):
        """Should detect ref(VPC) -> VPC."""
        code = '''vpc_id = ref(VPC)'''
        issues = lint_code(code, rules=[RefShouldBeNoParens()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW006"
        assert issues[0].suggestion == "VPC"

    def test_ignores_ref_with_string(self):
        """Should ignore ref("VPC") - string literals are forward references."""
        code = '''vpc_id = ref("VPC")'''
        issues = lint_code(code, rules=[RefShouldBeNoParens()])
        # String literals are forward references and should not be flagged
        assert len(issues) == 0

    def test_detects_get_att_with_class_and_string(self):
        """Should detect get_att(MyRole, "Arn") -> MyRole.Arn."""
        code = '''role_arn = get_att(MyRole, "Arn")'''
        issues = lint_code(code, rules=[RefShouldBeNoParens()])
        assert len(issues) == 1
        assert issues[0].suggestion == "MyRole.Arn"

    def test_ignores_get_att_with_string_target(self):
        """Should ignore get_att("MyRole", "Arn") - string literals are forward references."""
        code = '''role_arn = get_att("MyRole", "Arn")'''
        issues = lint_code(code, rules=[RefShouldBeNoParens()])
        # String literals are forward references and should not be flagged
        assert len(issues) == 0

    def test_detects_get_att_with_constant(self):
        """Should detect get_att(MyRole, ARN) -> MyRole.ARN."""
        code = '''role_arn = get_att(MyRole, ARN)'''
        issues = lint_code(code, rules=[RefShouldBeNoParens()])
        assert len(issues) == 1
        assert issues[0].suggestion == "MyRole.ARN"

    def test_detects_multiple_refs(self):
        """Should detect multiple ref() calls."""
        code = """
vpc_id = ref(VPC)
subnet_id = ref(Subnet)
"""
        issues = lint_code(code, rules=[RefShouldBeNoParens()])
        assert len(issues) == 2

    def test_fix_replaces_ref(self):
        """Should replace ref(VPC) with VPC."""
        code = '''vpc_id = ref(VPC)'''
        fixed = fix_code(code, rules=[RefShouldBeNoParens()], add_imports=False)
        assert "vpc_id = VPC" in fixed
        assert "ref(VPC)" not in fixed

    def test_fix_replaces_get_att(self):
        """Should replace get_att(MyRole, "Arn") with MyRole.Arn."""
        code = '''role_arn = get_att(MyRole, "Arn")'''
        fixed = fix_code(code, rules=[RefShouldBeNoParens()], add_imports=False)
        assert "role_arn = MyRole.Arn" in fixed
        assert "get_att(" not in fixed
