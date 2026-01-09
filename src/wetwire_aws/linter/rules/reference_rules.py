"""Reference-related lint rules.

Rules:
    WAW006: Use no-parens references instead of ref()/get_att()
"""

from __future__ import annotations

import ast

from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule


class RefShouldBeNoParens(LintRule):
    """Detect ref()/get_att() calls that should use no-parens style.

    The no-parens style is more declarative and readable. References to other
    resources should be expressed as bare class names, and attribute references
    as Class.Attribute.

    Detects:
    - ref(VPC) or ref("VPC")
    - get_att(MyRole, "Arn") or get_att("MyRole", "Arn")

    Suggests:
    - VPC
    - MyRole.Arn
    """

    rule_id = "WAW006"
    description = "Use no-parens references instead of ref()/get_att()"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.Call):
                func = node.func
                func_name = None

                if isinstance(func, ast.Name):
                    func_name = func.id
                elif isinstance(func, ast.Attribute):
                    func_name = func.attr

                # Check for ref() calls - only convert when target is a Name node
                # (already a class reference). String literals like ref("VPC") are
                # forward references and should not be converted to bare names.
                if func_name == "ref" and node.args:
                    arg = node.args[0]
                    # Only convert Name nodes (ref(VPC)), not string literals (ref("VPC"))
                    if isinstance(arg, ast.Name):
                        target = arg.id
                        original = ast.get_source_segment(context.source, node)
                        if original:
                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message=f"Use {target} instead of ref({target})",
                                    line=node.lineno,
                                    column=node.col_offset,
                                    original=original,
                                    suggestion=target,
                                    fix_imports=[],
                                )
                            )

                # Check for get_att() calls - only convert when target is a Name node
                # String-based forward references like get_att("VPC", "Arn") are needed
                # for classes defined later in the file (e.g., in PropertyType wrappers).
                if func_name == "get_att" and len(node.args) >= 2:
                    target_arg = node.args[0]
                    attr_arg = node.args[1]

                    # Only convert Name nodes, not string literals
                    if isinstance(target_arg, ast.Name):
                        target = target_arg.id
                        attr_name = self._extract_attr_name(attr_arg, context)

                        # Convert all attributes: get_att(MyRole, "Arn") -> MyRole.Arn
                        # Nested attributes like "Endpoint.Address" also work via PropertyTypeProxy
                        if attr_name:
                            original = ast.get_source_segment(context.source, node)
                            suggestion = f"{target}.{attr_name}"
                            if original:
                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=f"Use {suggestion} instead of get_att()",
                                        line=node.lineno,
                                        column=node.col_offset,
                                        original=original,
                                        suggestion=suggestion,
                                        fix_imports=[],
                                    )
                                )

        return issues

    def _extract_target(self, node: ast.expr) -> str | None:
        """Extract target class name from a ref/get_att argument.

        Handles both Name nodes (ref(VPC)) and string literals (ref("VPC")).
        """
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        return None

    def _extract_attr_name(self, node: ast.expr, context: LintContext) -> str | None:
        """Extract attribute name from a get_att second argument.

        Handles string literals ("Arn") and constant references (ARN).
        """
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            # It's a constant like ARN - get the source text
            return ast.get_source_segment(context.source, node)
        return None
