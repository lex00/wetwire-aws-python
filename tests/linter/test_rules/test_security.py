"""Tests for WAW021: secret pattern detection."""

import pytest

from wetwire_aws.linter import lint_code
from wetwire_aws.linter.rules.security_rules import HardcodedSecret


class TestHardcodedSecret:
    """Tests for WAW021: hardcoded secret detection."""

    def test_detects_aws_access_key(self):
        """Should detect AWS access key ID pattern."""
        code = '''access_key = "AKIAIOSFODNN7EXAMPLE"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW021"
        assert "AWS access key" in issues[0].message.lower() or "secret" in issues[0].message.lower()

    def test_detects_aws_secret_key(self):
        """Should detect AWS secret access key pattern."""
        code = '''secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW021"

    def test_detects_private_key_header(self):
        """Should detect private key header."""
        code = '''key = "-----BEGIN RSA PRIVATE KEY-----"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 1
        assert "private key" in issues[0].message.lower()

    def test_detects_generic_api_key(self):
        """Should detect generic API key patterns."""
        code = '''api_key = "sk_test_12345678901234567890ab"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW021"

    def test_detects_password_assignment(self):
        """Should detect password assignments."""
        code = '''password = "SuperSecret123!"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW021"

    def test_detects_token_assignment(self):
        """Should detect token assignments."""
        code = '''auth_token = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 1
        assert issues[0].rule_id == "WAW021"

    def test_detects_bearer_token(self):
        """Should detect bearer tokens."""
        code = '''header = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 1

    def test_ignores_non_secret_strings(self):
        """Should not flag ordinary strings."""
        code = '''bucket_name = "my-data-bucket"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 0

    def test_ignores_reference_strings(self):
        """Should not flag reference-like strings."""
        code = '''role = MyRole.Arn'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 0

    def test_ignores_placeholder_secrets(self):
        """Should not flag obvious placeholder values."""
        code = '''password = "changeme"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        # Placeholder values should be ignored
        assert len(issues) == 0

    def test_detects_in_class_attributes(self):
        """Should detect secrets in class attributes."""
        code = '''
class MyConfig:
    api_key = "AKIAIOSFODNN7EXAMPLE"
'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) == 1

    def test_detects_multiple_secrets(self):
        """Should detect multiple secrets in same file."""
        code = '''
access_key = "AKIAIOSFODNN7EXAMPLE"
password = "MySecret123"
'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) >= 2

    @pytest.mark.parametrize(
        "secret_pattern",
        [
            "AKIAIOSFODNN7EXAMPLE",  # AWS access key
            "-----BEGIN EC PRIVATE KEY-----",  # EC private key
            "-----BEGIN OPENSSH PRIVATE KEY-----",  # OpenSSH key
            "sk-ant-api03-xxxxxxxxxxxxxxxxxxxx",  # Anthropic API key
            "xoxs-000000000-test-token-xyz",  # Slack token
            "github_pat_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # GitHub PAT
        ],
    )
    def test_detects_various_patterns(self, secret_pattern):
        """Should detect various secret patterns."""
        code = f'''secret = "{secret_pattern}"'''
        issues = lint_code(code, rules=[HardcodedSecret()])
        assert len(issues) >= 1, f"Failed to detect pattern: {secret_pattern}"
