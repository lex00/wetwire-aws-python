"""Tests for WAW002: Ref() with pseudo-parameters."""

import pytest

from wetwire_aws.linter import (
    RefShouldBePseudoParameter,
    fix_code,
    lint_code,
)


class TestRefShouldBePseudoParameter:
    """Tests for WAW002: Ref() with pseudo-parameters."""

    @pytest.mark.parametrize(
        "pseudo_param,expected_constant",
        [
            ("AWS::Region", "AWS_REGION"),
            ("AWS::StackName", "AWS_STACK_NAME"),
            ("AWS::AccountId", "AWS_ACCOUNT_ID"),
            ("AWS::Partition", "AWS_PARTITION"),
            ("AWS::StackId", "AWS_STACK_ID"),
            ("AWS::URLSuffix", "AWS_URL_SUFFIX"),
            ("AWS::NotificationARNs", "AWS_NOTIFICATION_ARNS"),
            ("AWS::NoValue", "AWS_NO_VALUE"),
        ],
    )
    def test_detects_pseudo_parameter(self, pseudo_param, expected_constant):
        """Should detect Ref('AWS::X') and suggest constant."""
        code = f'''value = Ref("{pseudo_param}")'''
        issues = lint_code(code, rules=[RefShouldBePseudoParameter()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW002"
        assert expected_constant in issues[0].suggestion

    def test_detects_all_pseudo_parameters(self):
        """Should detect all AWS pseudo-parameters in single file."""
        code = """
region = Ref("AWS::Region")
stack = Ref("AWS::StackName")
account = Ref("AWS::AccountId")
partition = Ref("AWS::Partition")
"""
        issues = lint_code(code, rules=[RefShouldBePseudoParameter()])
        assert len(issues) == 4

    def test_ignores_regular_refs(self):
        """Should not flag Ref() with regular resource/parameter references."""
        code = """
bucket_ref = Ref("MyBucket")
param_ref = Ref("Environment")
"""
        issues = lint_code(code, rules=[RefShouldBePseudoParameter()])
        assert len(issues) == 0

    def test_fix_replaces_ref(self):
        """Should replace Ref('AWS::Region') with AWS_REGION."""
        code = '''region = Ref("AWS::Region")'''
        fixed = fix_code(code, rules=[RefShouldBePseudoParameter()], add_imports=False)
        assert "AWS_REGION" in fixed
        assert 'Ref("AWS::Region")' not in fixed
