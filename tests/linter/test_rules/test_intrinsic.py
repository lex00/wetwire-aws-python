"""Tests for intrinsic function rules.

Rules:
    WAW004: Use intrinsic function classes instead of raw dicts
    WAW005: Remove unnecessary .to_dict() calls
    WAW019: Avoid explicit Ref() intrinsic
    WAW020: Avoid explicit GetAtt() intrinsic
"""

import pytest

from wetwire_aws.linter import (
    DictShouldBeIntrinsic,
    UnnecessaryToDict,
    fix_code,
    lint_code,
)
from wetwire_aws.linter.rules import (
    ExplicitGetAttIntrinsic,
    ExplicitRefIntrinsic,
)


class TestDictShouldBeIntrinsic:
    """Tests for WAW004: dict literals that should be intrinsic functions."""

    @pytest.mark.parametrize(
        "intrinsic_key,value,expected_func",
        [
            ("Ref", '"MyBucket"', "Ref("),
            ("Fn::Sub", '"${AWS::Region}-bucket"', "Sub("),
            ("Fn::GetAtt", '"MyBucket.Arn"', "GetAtt("),
            ("Fn::Join", '[",", ["a", "b"]]', "Join("),
            ("Fn::Select", '[0, ["a", "b"]]', "Select("),
            ("Fn::Base64", '"hello"', "Base64("),
            ("Fn::GetAZs", '""', "GetAZs("),
        ],
    )
    def test_detects_intrinsic_dict(self, intrinsic_key, value, expected_func):
        """Should detect intrinsic dict patterns and suggest function."""
        code = f'''value = {{"{intrinsic_key}": {value}}}'''
        issues = lint_code(code, rules=[DictShouldBeIntrinsic()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW004"
        assert expected_func in issues[0].suggestion

    def test_ignores_regular_dicts(self):
        """Should not flag regular dicts."""
        code = '''data = {"Name": "value", "Value": 123}'''
        issues = lint_code(code, rules=[DictShouldBeIntrinsic()])
        assert len(issues) == 0

    def test_ignores_multi_key_dicts(self):
        """Should not flag dicts with multiple keys."""
        code = '''data = {"Ref": "MyBucket", "Other": "value"}'''
        issues = lint_code(code, rules=[DictShouldBeIntrinsic()])
        assert len(issues) == 0


class TestUnnecessaryToDict:
    """Tests for WAW005: unnecessary .to_dict() calls."""

    @pytest.mark.parametrize(
        "func_name",
        ["ref", "get_att", "Ref", "GetAtt", "Sub", "Join", "Select", "If"],
    )
    def test_detects_to_dict_on_intrinsic(self, func_name):
        """Should detect intrinsic().to_dict()."""
        code = f'''value = {func_name}(MyBucket).to_dict()'''
        issues = lint_code(code, rules=[UnnecessaryToDict()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW005"
        assert f"{func_name}(" in issues[0].message

    def test_ignores_other_to_dict(self):
        """Should not flag .to_dict() on other objects."""
        code = '''value = some_object.to_dict()'''
        issues = lint_code(code, rules=[UnnecessaryToDict()])
        assert len(issues) == 0


class TestExplicitRefIntrinsic:
    """Tests for WAW019: explicit Ref() intrinsic usage."""

    def test_detects_ref_with_string_literal(self):
        """Should detect Ref('MyBucket')."""
        code = '''bucket_ref = Ref("MyBucket")'''
        issues = lint_code(code, rules=[ExplicitRefIntrinsic()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW019"
        assert issues[0].suggestion == "MyBucket"

    def test_ignores_pseudo_parameters(self):
        """Should not flag Ref('AWS::Region') - handled by WAW002."""
        code = '''region = Ref("AWS::Region")'''
        issues = lint_code(code, rules=[ExplicitRefIntrinsic()])
        assert len(issues) == 0

    def test_ignores_lowercase_ref(self):
        """Should not flag ref() helper function - handled by WAW006."""
        code = '''bucket_ref = ref("MyBucket")'''
        issues = lint_code(code, rules=[ExplicitRefIntrinsic()])
        assert len(issues) == 0

    def test_detects_ref_with_parameter_name(self):
        """Should detect Ref('MyParameter')."""
        code = '''vpc_id = Ref("VpcIdParam")'''
        issues = lint_code(code, rules=[ExplicitRefIntrinsic()])
        assert len(issues) == 1
        assert issues[0].suggestion == "VpcIdParam"

    def test_fix_replaces_with_direct_ref(self):
        """Should replace Ref('X') with X."""
        code = '''bucket_ref = Ref("MyBucket")'''
        fixed = fix_code(code, rules=[ExplicitRefIntrinsic()], add_imports=False)
        assert "bucket_ref = MyBucket" in fixed
        assert 'Ref("MyBucket")' not in fixed


class TestExplicitGetAttIntrinsic:
    """Tests for WAW020: explicit GetAtt() intrinsic usage."""

    def test_detects_getatt_with_string_literals(self):
        """Should detect GetAtt('MyRole', 'Arn')."""
        code = '''role_arn = GetAtt("MyRole", "Arn")'''
        issues = lint_code(code, rules=[ExplicitGetAttIntrinsic()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW020"
        assert issues[0].suggestion == "MyRole.Arn"

    def test_flags_getatt_with_nested_attr(self):
        """Should flag nested GetAtt - Resource.Attr.SubAttr now works.

        Nested attributes like "Endpoint.Address" work via PropertyTypeProxy
        which enables chained attribute access for nested GetAtt patterns.
        """
        code = '''db_endpoint = GetAtt("MyDB", "Endpoint.Address")'''
        issues = lint_code(code, rules=[ExplicitGetAttIntrinsic()])
        assert len(issues) == 1
        assert issues[0].suggestion == "MyDB.Endpoint.Address"

    def test_ignores_lowercase_get_att(self):
        """Should not flag get_att() helper function - handled by WAW006."""
        code = '''role_arn = get_att("MyRole", "Arn")'''
        issues = lint_code(code, rules=[ExplicitGetAttIntrinsic()])
        assert len(issues) == 0

    def test_ignores_getatt_with_variable_resource(self):
        """Should not flag GetAtt(resource_var, 'Arn') - may be intentional."""
        code = '''role_arn = GetAtt(role_resource, "Arn")'''
        issues = lint_code(code, rules=[ExplicitGetAttIntrinsic()])
        assert len(issues) == 0

    def test_fix_replaces_with_attribute_access(self):
        """Should replace GetAtt('X', 'Y') with X.Y."""
        code = '''role_arn = GetAtt("MyRole", "Arn")'''
        fixed = fix_code(code, rules=[ExplicitGetAttIntrinsic()], add_imports=False)
        assert "MyRole.Arn" in fixed
        assert 'GetAtt("MyRole"' not in fixed
