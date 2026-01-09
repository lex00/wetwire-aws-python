"""Pseudo-parameter lint rules.

Rules:
    WAW002: Use pseudo-parameter constants instead of Ref() with strings
"""

from __future__ import annotations

import ast

from wetwire_aws.constants import PSEUDO_PARAMETER_MAP
from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule


class RefShouldBePseudoParameter(LintRule):
    """Detect Ref() calls with pseudo-parameters that should use constants.

    Detects: Ref("AWS::Region"), Ref("AWS::StackName")
    Suggests: AWS_REGION, AWS_STACK_NAME
    """

    rule_id = "WAW002"
    description = "Use pseudo-parameter constants instead of Ref() with string literals"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.Call):
                # Check if it's a Ref() call
                func = node.func
                is_ref = False
                if isinstance(func, ast.Name) and func.id == "Ref":
                    is_ref = True
                elif isinstance(func, ast.Attribute) and func.attr == "Ref":
                    is_ref = True

                if is_ref and node.args:
                    arg = node.args[0]
                    if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                        pseudo_param = arg.value
                        if pseudo_param in PSEUDO_PARAMETER_MAP:
                            constant_name = PSEUDO_PARAMETER_MAP[pseudo_param]
                            import_stmt = (
                                f"from wetwire_aws.intrinsics import {constant_name}"
                            )

                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message=f"Use {constant_name} instead of Ref('{pseudo_param}')",
                                    line=node.lineno,
                                    column=node.col_offset,
                                    original=f'Ref("{pseudo_param}")',
                                    suggestion=constant_name,
                                    fix_imports=[import_stmt],
                                )
                            )

        return issues
