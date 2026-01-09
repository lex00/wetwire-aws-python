"""Tests for WAW003: string literals that should be enums."""

import pytest

from wetwire_aws.linter import (
    StringShouldBeEnum,
    fix_code,
    lint_code,
)


class TestStringShouldBeEnum:
    """Tests for WAW003: string literals that should be enums.

    These tests mock _is_enum_available to test pattern detection logic
    without requiring actual enum generation (which needs botocore).
    """

    @pytest.mark.parametrize(
        "field_name,value,expected_suggestion",
        [
            ("sse_algorithm", "AES256", "s3.ServerSideEncryption.AES256"),
            ("sse_algorithm", "aws:kms", "s3.ServerSideEncryption.AWSKMS"),
            ("sse_algorithm", "aws:kms:dsse", "s3.ServerSideEncryption.AWSKMSDSSE"),
            ("status", "Enabled", "s3.BucketVersioningStatus.ENABLED"),
            ("status", "Suspended", "s3.BucketVersioningStatus.SUSPENDED"),
            ("key_type", "HASH", "dynamodb.KeyType.HASH"),
            ("key_type", "RANGE", "dynamodb.KeyType.RANGE"),
            ("attribute_type", "S", "dynamodb.ScalarAttributeType.S"),
            ("attribute_type", "N", "dynamodb.ScalarAttributeType.N"),
            ("attribute_type", "B", "dynamodb.ScalarAttributeType.B"),
            ("billing_mode", "PROVISIONED", "dynamodb.BillingMode.PROVISIONED"),
            ("billing_mode", "PAY_PER_REQUEST", "dynamodb.BillingMode.PAY_PER_REQUEST"),
            ("runtime", "python3.12", "lambda_.Runtime.PYTHON3_12"),
            ("runtime", "nodejs20.x", "lambda_.Runtime.NODEJS20_X"),
        ],
    )
    def test_detects_enum_value(self, mock_enum_available, field_name, value, expected_suggestion):
        """Should detect enum values and suggest module-qualified name."""
        code = f'''{field_name} = "{value}"'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW003"
        assert issues[0].suggestion == expected_suggestion

    def test_detects_enum_in_kwargs(self, mock_enum_available):
        """Should detect enum values in keyword arguments with module-qualified name."""
        code = '''encryption = ServerSideEncryptionByDefault(sse_algorithm="AES256")'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 1
        assert issues[0].suggestion == "s3.ServerSideEncryption.AES256"

    def test_ignores_unknown_field_names(self):
        """Should not flag unknown field names."""
        code = '''unknown_field = "AES256"'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 0

    def test_ignores_unknown_values(self):
        """Should not flag unknown values for known fields."""
        code = '''sse_algorithm = "UNKNOWN_VALUE"'''
        issues = lint_code(code, rules=[StringShouldBeEnum()])
        assert len(issues) == 0

    def test_fix_replaces_enum_value(self, mock_enum_available):
        """Should replace string with module-qualified enum constant."""
        code = '''sse_algorithm = "AES256"'''
        fixed = fix_code(code, rules=[StringShouldBeEnum()], add_imports=False)
        assert "s3.ServerSideEncryption.AES256" in fixed
        assert '"AES256"' not in fixed
