"""Enum-related lint rules.

Rules:
    WAW003: Use enum constants instead of string literals
"""

from __future__ import annotations

import ast

from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule


class StringShouldBeEnum(LintRule):
    """Detect string literals that should be enum constants.

    This rule works by pattern matching known enum values in assignments,
    keyword arguments, and dict key-value pairs.

    Detects:
    - sse_algorithm = "AES256"
    - {'SSEAlgorithm': 'AES256'}
    - {'Status': 'Enabled'}

    Suggests (module-qualified, no imports needed):
    - sse_algorithm = s3.ServerSideEncryption.AES256
    - {'SSEAlgorithm': s3.ServerSideEncryption.AES256}
    - {'Status': s3.BucketVersioningStatus.ENABLED}

    Note: This rule uses static analysis with known patterns.
    The module-qualified form (e.g., s3.ServerSideEncryption) is preferred
    because the modules are available via `from . import *` in the package pattern.
    Only suggests enums that actually exist in the generated code.
    """

    rule_id = "WAW003"
    description = "Use enum constants instead of string literals"

    # Cache for enum availability checks
    _enum_availability_cache: dict[str, bool] = {}

    # Known enum patterns: field_name -> (enum_class, module_short, {value: constant_name})
    # module_short is the short module name (e.g., "s3", "lambda_") not the full path
    KNOWN_ENUMS: dict[str, tuple[str, str, dict[str, str]]] = {
        # S3 enums - snake_case keys
        "sse_algorithm": (
            "ServerSideEncryption",
            "s3",
            {"AES256": "AES256", "aws:kms": "AWSKMS", "aws:kms:dsse": "AWSKMSDSSE"},
        ),
        "status": (
            "BucketVersioningStatus",
            "s3",
            {"Enabled": "ENABLED", "Suspended": "SUSPENDED"},
        ),
        # DynamoDB enums
        "key_type": (
            "KeyType",
            "dynamodb",
            {"HASH": "HASH", "RANGE": "RANGE"},
        ),
        "attribute_type": (
            "ScalarAttributeType",
            "dynamodb",
            {"S": "S", "N": "N", "B": "B"},
        ),
        "billing_mode": (
            "BillingMode",
            "dynamodb",
            {"PROVISIONED": "PROVISIONED", "PAY_PER_REQUEST": "PAY_PER_REQUEST"},
        ),
        # Lambda enums
        "runtime": (
            "Runtime",
            "lambda_",
            {
                "python3.8": "PYTHON3_8",
                "python3.9": "PYTHON3_9",
                "python3.10": "PYTHON3_10",
                "python3.11": "PYTHON3_11",
                "python3.12": "PYTHON3_12",
                "nodejs18.x": "NODEJS18_X",
                "nodejs20.x": "NODEJS20_X",
            },
        ),
    }

    # CloudFormation PascalCase keys for dict literals
    KNOWN_DICT_KEYS: dict[str, tuple[str, str, dict[str, str]]] = {
        "SSEAlgorithm": (
            "ServerSideEncryption",
            "s3",
            {"AES256": "AES256", "aws:kms": "AWSKMS", "aws:kms:dsse": "AWSKMSDSSE"},
        ),
        "Status": (
            "BucketVersioningStatus",
            "s3",
            {"Enabled": "ENABLED", "Suspended": "SUSPENDED"},
        ),
        "KeyType": (
            "KeyType",
            "dynamodb",
            {"HASH": "HASH", "RANGE": "RANGE"},
        ),
        "AttributeType": (
            "ScalarAttributeType",
            "dynamodb",
            {"S": "S", "N": "N", "B": "B"},
        ),
        "Runtime": (
            "Runtime",
            "lambda_",
            {
                "python3.8": "PYTHON3_8",
                "python3.9": "PYTHON3_9",
                "python3.10": "PYTHON3_10",
                "python3.11": "PYTHON3_11",
                "python3.12": "PYTHON3_12",
                "nodejs18.x": "NODEJS18_X",
                "nodejs20.x": "NODEJS20_X",
            },
        ),
    }

    def _is_enum_available(self, module_short: str, enum_class: str) -> bool:
        """Check if an enum class actually exists in the generated code.

        Args:
            module_short: The short module name (e.g., "s3", "lambda_").
            enum_class: The enum class name (e.g., "ServerSideEncryption").

        Returns:
            True if the enum class exists and is importable, False otherwise.
        """
        cache_key = f"{module_short}.{enum_class}"
        if cache_key in self._enum_availability_cache:
            return self._enum_availability_cache[cache_key]

        try:
            module = __import__(
                f"wetwire_aws.resources.{module_short}", fromlist=[enum_class]
            )
            result = hasattr(module, enum_class)
        except (ImportError, ModuleNotFoundError):
            result = False

        self._enum_availability_cache[cache_key] = result
        return result

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Check assignments: field_name = "value"
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        field_name = target.id
                        if field_name in self.KNOWN_ENUMS:
                            if isinstance(node.value, ast.Constant) and isinstance(
                                node.value.value, str
                            ):
                                value = node.value.value
                                enum_class, module_short, value_map = self.KNOWN_ENUMS[
                                    field_name
                                ]
                                if value in value_map:
                                    # Only suggest if the enum actually exists
                                    if not self._is_enum_available(
                                        module_short, enum_class
                                    ):
                                        continue

                                    const_name = value_map[value]
                                    # Use module-qualified form: s3.ServerSideEncryption.AES256
                                    suggestion = (
                                        f"{module_short}.{enum_class}.{const_name}"
                                    )

                                    issues.append(
                                        LintIssue(
                                            rule_id=self.rule_id,
                                            message=f"Use {suggestion} instead of '{value}'",
                                            line=node.value.lineno,
                                            column=node.value.col_offset,
                                            original=f'"{value}"',
                                            suggestion=suggestion,
                                            # No imports needed - modules available via from . import *
                                            fix_imports=[],
                                        )
                                    )

            # Check keyword arguments in function/class calls
            if isinstance(node, ast.Call):
                for keyword in node.keywords:
                    if keyword.arg and keyword.arg in self.KNOWN_ENUMS:
                        if isinstance(keyword.value, ast.Constant) and isinstance(
                            keyword.value.value, str
                        ):
                            value = keyword.value.value
                            enum_class, module_short, value_map = self.KNOWN_ENUMS[
                                keyword.arg
                            ]
                            if value in value_map:
                                # Only suggest if the enum actually exists
                                if not self._is_enum_available(
                                    module_short, enum_class
                                ):
                                    continue

                                const_name = value_map[value]
                                # Use module-qualified form
                                suggestion = f"{module_short}.{enum_class}.{const_name}"

                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=f"Use {suggestion} instead of '{value}'",
                                        line=keyword.value.lineno,
                                        column=keyword.value.col_offset,
                                        original=f'"{value}"',
                                        suggestion=suggestion,
                                        fix_imports=[],
                                    )
                                )

            # Check dict literals: {'SSEAlgorithm': 'AES256'}
            if isinstance(node, ast.Dict):
                for key, val in zip(node.keys, node.values):
                    if isinstance(key, ast.Constant) and isinstance(key.value, str):
                        key_str = key.value
                        if key_str in self.KNOWN_DICT_KEYS:
                            if isinstance(val, ast.Constant) and isinstance(
                                val.value, str
                            ):
                                value = val.value
                                enum_class, module_short, value_map = (
                                    self.KNOWN_DICT_KEYS[key_str]
                                )
                                if value in value_map:
                                    # Only suggest if the enum actually exists
                                    if not self._is_enum_available(
                                        module_short, enum_class
                                    ):
                                        continue

                                    const_name = value_map[value]
                                    # Use module-qualified form
                                    suggestion = (
                                        f"{module_short}.{enum_class}.{const_name}"
                                    )

                                    issues.append(
                                        LintIssue(
                                            rule_id=self.rule_id,
                                            message=f"Use {suggestion} instead of '{value}'",
                                            line=val.lineno,
                                            column=val.col_offset,
                                            original=f'"{value}"',
                                            suggestion=suggestion,
                                            fix_imports=[],
                                        )
                                    )

        return issues
