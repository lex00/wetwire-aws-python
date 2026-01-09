"""Parameter-related lint rules.

Rules:
    WAW001: Use parameter type constants instead of string literals
"""

from __future__ import annotations

import ast

from wetwire_aws.constants import PARAMETER_TYPE_MAP
from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule


class StringShouldBeParameterType(LintRule):
    """Detect parameter types as string literals.

    Detects: type = "String", type = "Number"
    Suggests: type = STRING, type = NUMBER
    """

    rule_id = "WAW001"
    description = "Use parameter type constants instead of string literals"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Look for assignments to 'type' attribute
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "type":
                        if isinstance(node.value, ast.Constant) and isinstance(
                            node.value.value, str
                        ):
                            type_str = node.value.value
                            if type_str in PARAMETER_TYPE_MAP:
                                constant_name = PARAMETER_TYPE_MAP[type_str]
                                import_stmt = f"from wetwire_aws.intrinsics import {constant_name}"

                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=f"Use {constant_name} instead of '{type_str}'",
                                        line=node.value.lineno,
                                        column=node.value.col_offset,
                                        original=f'"{type_str}"',
                                        suggestion=constant_name,
                                        fix_imports=[import_stmt],
                                    )
                                )

            # Also check keyword arguments in function/class calls
            if isinstance(node, ast.Call):
                for keyword in node.keywords:
                    if keyword.arg == "type":
                        if isinstance(keyword.value, ast.Constant) and isinstance(
                            keyword.value.value, str
                        ):
                            type_str = keyword.value.value
                            if type_str in PARAMETER_TYPE_MAP:
                                constant_name = PARAMETER_TYPE_MAP[type_str]
                                import_stmt = f"from wetwire_aws.intrinsics import {constant_name}"

                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=f"Use {constant_name} instead of '{type_str}'",
                                        line=keyword.value.lineno,
                                        column=keyword.value.col_offset,
                                        original=f'"{type_str}"',
                                        suggestion=constant_name,
                                        fix_imports=[import_stmt],
                                    )
                                )

        return issues
