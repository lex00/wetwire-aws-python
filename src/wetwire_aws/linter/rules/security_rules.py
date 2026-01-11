"""Security-related lint rules.

Rules:
    WAW021: Detect hardcoded secrets in code
"""

from __future__ import annotations

import ast
import re

from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule

# Secret patterns to detect
# Each tuple: (pattern_name, regex_pattern, is_value_pattern)
# is_value_pattern: True if the regex matches the value, False if it matches var name + value
SECRET_PATTERNS: list[tuple[str, re.Pattern[str], bool]] = [
    # AWS Access Key ID (starts with AKIA, ABIA, ACCA, ASIA)
    ("AWS access key", re.compile(r"^A[KBS]IA[A-Z0-9]{16}$"), True),
    # AWS Secret Access Key (40 chars, base64-ish)
    ("AWS secret key", re.compile(r"^[A-Za-z0-9/+=]{40}$"), True),
    # Private key headers
    ("Private key", re.compile(r"-----BEGIN[A-Z\s]*PRIVATE KEY-----"), True),
    # Generic API key patterns (sk_, api_, key_ prefixes with long alphanumeric)
    ("API key", re.compile(r"^(sk|api|key)[-_][a-zA-Z0-9]{20,}$"), True),
    # Bearer/JWT tokens
    ("Bearer token", re.compile(r"^Bearer\s+[A-Za-z0-9\-_\.]+$"), True),
    # GitHub tokens
    ("GitHub token", re.compile(r"^(ghp|gho|ghu|ghs|ghr|github_pat)_[A-Za-z0-9_]{36,}$"), True),
    # Slack tokens
    ("Slack token", re.compile(r"^xox[baprs]-[A-Za-z0-9\-]+$"), True),
    # Anthropic API keys
    ("Anthropic API key", re.compile(r"^sk-ant-[a-zA-Z0-9\-]+$"), True),
    # OpenAI API keys
    ("OpenAI API key", re.compile(r"^sk-[a-zA-Z0-9]{48}$"), True),
    # Generic long hex strings (likely API keys/tokens)
    ("Hex token", re.compile(r"^[a-fA-F0-9]{32,}$"), True),
]

# Variable name patterns that suggest secrets
SECRET_VAR_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("password", re.compile(r"(?i)(password|passwd|pwd|secret)")),
    ("token", re.compile(r"(?i)(token|auth_token|api_token|access_token)")),
    ("API key", re.compile(r"(?i)(api_key|apikey|secret_key|private_key)")),
    ("credential", re.compile(r"(?i)(credential|cred|auth)")),
]

# Placeholder values that should be ignored (exact match only)
PLACEHOLDER_VALUES = {
    "changeme",
    "password",
    "xxx",
    "placeholder",
    "test",
    "dummy",
    "fake",
    "todo",
    "fixme",
}


def _is_placeholder(value: str) -> bool:
    """Check if a value looks like a placeholder.

    Only returns True for exact matches of known placeholder values.
    """
    lower_val = value.lower()
    return lower_val in PLACEHOLDER_VALUES


def _detect_secret_in_value(value: str) -> str | None:
    """Check if a string value matches a secret pattern.

    Returns the pattern name if matched, None otherwise.
    """
    if _is_placeholder(value):
        return None

    for pattern_name, pattern, is_value_pattern in SECRET_PATTERNS:
        if is_value_pattern and pattern.search(value):
            return pattern_name

    return None


def _detect_secret_by_varname(var_name: str, value: str) -> str | None:
    """Check if a variable name suggests a secret with a non-trivial value.

    Returns the pattern name if the var name suggests a secret.
    """
    if _is_placeholder(value):
        return None

    # Don't flag empty or very short values
    if len(value) < 4:
        return None

    for pattern_name, pattern in SECRET_VAR_PATTERNS:
        if pattern.search(var_name):
            return pattern_name

    return None


class HardcodedSecret(LintRule):
    """Detect hardcoded secrets in code.

    Detects:
    - AWS access keys and secret keys
    - Private key headers
    - API tokens and keys
    - Passwords and credentials

    Suggests using environment variables or secrets management.
    """

    rule_id = "WAW021"
    description = "Avoid hardcoded secrets; use environment variables or secrets management"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Check assignments: var = "value"
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id
                        if isinstance(node.value, ast.Constant) and isinstance(
                            node.value.value, str
                        ):
                            value = node.value.value
                            secret_type = self._check_for_secret(var_name, value)
                            if secret_type:
                                issues.append(
                                    self._create_issue(
                                        secret_type, value, node.value
                                    )
                                )

            # Check class attributes
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                var_name = node.target.id
                if (
                    node.value
                    and isinstance(node.value, ast.Constant)
                    and isinstance(node.value.value, str)
                ):
                    value = node.value.value
                    secret_type = self._check_for_secret(var_name, value)
                    if secret_type:
                        issues.append(
                            self._create_issue(secret_type, value, node.value)
                        )

        return issues

    def _check_for_secret(self, var_name: str, value: str) -> str | None:
        """Check if a variable assignment looks like a hardcoded secret.

        Returns the secret type if detected, None otherwise.
        """
        # First check if the value itself matches a secret pattern
        secret_type = _detect_secret_in_value(value)
        if secret_type:
            return secret_type

        # Then check if the variable name suggests a secret
        return _detect_secret_by_varname(var_name, value)

    def _create_issue(
        self, secret_type: str, value: str, node: ast.expr
    ) -> LintIssue:
        """Create a LintIssue for a detected secret."""
        # Truncate value for display
        display_value = value[:20] + "..." if len(value) > 20 else value
        return LintIssue(
            rule_id=self.rule_id,
            message=f"Potential {secret_type} detected: '{display_value}'. Use environment variables or secrets management.",
            line=node.lineno,
            column=node.col_offset,
            original=f'"{value}"',
            suggestion="os.environ.get('SECRET_NAME')",
            fix_imports=["import os"],
        )
