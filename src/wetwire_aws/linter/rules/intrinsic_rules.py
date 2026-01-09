"""Intrinsic function lint rules.

Rules:
    WAW004: Use intrinsic function classes instead of raw dicts
    WAW005: Remove unnecessary .to_dict() calls on intrinsic functions
    WAW019: Avoid explicit Ref() intrinsic - use direct variable references
    WAW020: Avoid explicit GetAtt() intrinsic - use Resource.Attribute access
"""

from __future__ import annotations

import ast

from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule


class DictShouldBeIntrinsic(LintRule):
    """Detect raw intrinsic function dicts that should use typed helpers.

    CloudFormation intrinsic functions like Ref, Sub, Select, Join, etc.
    should be expressed using the typed helpers from wetwire_aws.intrinsics
    rather than raw dict literals.

    Detects: {"Ref": "VpcId"}, {"Fn::Sub": "..."}, {"Fn::Select": [...]}
    Suggests: Ref("VpcId"), Sub("..."), Select(...)
    """

    rule_id = "WAW004"
    description = "Use intrinsic function classes instead of raw dicts"

    # Map CloudFormation intrinsic keys to Python function names
    INTRINSIC_MAP: dict[str, tuple[str, str]] = {
        "Ref": ("Ref", "wetwire_aws.intrinsics"),
        "Fn::Sub": ("Sub", "wetwire_aws.intrinsics"),
        "Fn::Select": ("Select", "wetwire_aws.intrinsics"),
        "Fn::Join": ("Join", "wetwire_aws.intrinsics"),
        "Fn::GetAZs": ("GetAZs", "wetwire_aws.intrinsics"),
        "Fn::GetAtt": ("GetAtt", "wetwire_aws.intrinsics"),
        "Fn::If": ("If", "wetwire_aws.intrinsics"),
        "Fn::Equals": ("Equals", "wetwire_aws.intrinsics"),
        "Fn::And": ("And", "wetwire_aws.intrinsics"),
        "Fn::Or": ("Or", "wetwire_aws.intrinsics"),
        "Fn::Not": ("Not", "wetwire_aws.intrinsics"),
        "Fn::Base64": ("Base64", "wetwire_aws.intrinsics"),
        "Fn::Split": ("Split", "wetwire_aws.intrinsics"),
        "Fn::ImportValue": ("ImportValue", "wetwire_aws.intrinsics"),
        "Fn::FindInMap": ("FindInMap", "wetwire_aws.intrinsics"),
        "Fn::Cidr": ("Cidr", "wetwire_aws.intrinsics"),
    }

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # Check if file uses 'from . import *' pattern
        has_star_import = self._has_star_import(context.tree)

        for node in ast.walk(context.tree):
            # Look for single-key dict literals that match intrinsic patterns
            if isinstance(node, ast.Dict) and len(node.keys) == 1:
                key = node.keys[0]
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    key_str = key.value
                    if key_str in self.INTRINSIC_MAP:
                        func_name, module = self.INTRINSIC_MAP[key_str]

                        # Get the actual source text for the dict
                        original = ast.get_source_segment(context.source, node)

                        # Get the value and convert to source
                        value_node = node.values[0]
                        value_source = ast.get_source_segment(
                            context.source, value_node
                        )

                        # Build the replacement
                        if value_source:
                            if key_str == "Fn::GetAZs":
                                if value_source in ('""', "''", "AWS_REGION"):
                                    suggestion = f"{func_name}()"
                                else:
                                    suggestion = f"{func_name}({value_source})"
                            elif key_str in ("Fn::Select", "Fn::Join"):
                                if (
                                    isinstance(value_node, ast.List)
                                    and len(value_node.elts) >= 2
                                ):
                                    args = [
                                        ast.get_source_segment(context.source, elt)
                                        for elt in value_node.elts
                                    ]
                                    if all(args):
                                        suggestion = f"{func_name}({', '.join(args)})"
                                    else:
                                        suggestion = f"{func_name}({value_source})"
                                else:
                                    suggestion = f"{func_name}({value_source})"
                            else:
                                suggestion = f"{func_name}({value_source})"
                        else:
                            suggestion = f"{func_name}(...)"

                        fix_imports: list[str] = []
                        if not has_star_import:
                            fix_imports = [f"from {module} import {func_name}"]

                        if original:
                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message=f"Use {func_name}() instead of {{'{key_str}': ...}}",
                                    line=node.lineno,
                                    column=node.col_offset,
                                    original=original,
                                    suggestion=suggestion,
                                    fix_imports=fix_imports,
                                )
                            )

        return issues

    def _has_star_import(self, tree: ast.Module) -> bool:
        """Check if the module has a star import pattern."""
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module is None and node.level > 0:
                    for alias in node.names:
                        if alias.name == "*":
                            return True
        return False


class UnnecessaryToDict(LintRule):
    """Detect unnecessary .to_dict() calls on intrinsic function results.

    When using intrinsic functions like ref(), get_att(), Join(), etc.,
    calling .to_dict() is unnecessary because these functions return objects
    that serialize correctly when used directly.

    Detects: ref(MyResource).to_dict(), get_att(MyResource, "Arn").to_dict()
    Suggests: ref(MyResource), get_att(MyResource, "Arn")
    """

    rule_id = "WAW005"
    description = "Remove unnecessary .to_dict() calls on intrinsic functions"

    # Functions that return serializable intrinsic objects
    INTRINSIC_FUNCTIONS = {
        "ref",
        "get_att",
        "Ref",
        "GetAtt",
        "Sub",
        "Join",
        "Select",
        "If",
    }

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            # Look for method calls: something.to_dict()
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute) and node.func.attr == "to_dict":
                    # Check if the object is a call to an intrinsic function
                    obj = node.func.value
                    if isinstance(obj, ast.Call):
                        func = obj.func
                        func_name = None
                        if isinstance(func, ast.Name):
                            func_name = func.id
                        elif isinstance(func, ast.Attribute):
                            func_name = func.attr

                        if func_name in self.INTRINSIC_FUNCTIONS:
                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message=f"Remove .to_dict() - {func_name}() returns a serializable object",
                                    line=node.lineno,
                                    column=node.col_offset,
                                    original=f"{func_name}(...).to_dict()",
                                    suggestion=f"{func_name}(...)",
                                    fix_imports=[],
                                )
                            )

        return issues


class ExplicitRefIntrinsic(LintRule):
    """Detect explicit Ref() intrinsic function calls.

    Using Ref("ResourceName") or Ref("ParameterName") explicitly is verbose.
    The preferred style is to use direct variable references:
    - For resources: use the bare class name (MyBucket)
    - For parameters: use Param("Name") or the parameter class

    Note: Some Ref() calls are necessary for pseudo-parameters like
    Ref("AWS::Region"), but those should use constants (REGION).

    Detects:
    - Ref("MyBucket") or Ref("MyParameter")

    Suggests:
    - MyBucket (direct reference)
    - Or use WAW002 for pseudo-parameters

    This rule only flags Ref() calls with string literals. The ref() helper
    function is handled by WAW006.
    """

    rule_id = "WAW019"
    description = "Avoid explicit Ref() intrinsic - use direct variable references"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.Call):
                func = node.func

                # Check for Ref() call (capital R)
                if isinstance(func, ast.Name) and func.id == "Ref":
                    if node.args and isinstance(node.args[0], ast.Constant):
                        target = node.args[0].value
                        if isinstance(target, str):
                            # Skip pseudo-parameters (handled by WAW002)
                            if target.startswith("AWS::"):
                                continue

                            original = ast.get_source_segment(context.source, node)
                            if original:
                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=(
                                            f'Use {target} instead of Ref("{target}") '
                                            f"for direct variable reference"
                                        ),
                                        line=node.lineno,
                                        column=node.col_offset,
                                        original=original,
                                        suggestion=target,
                                        fix_imports=[],
                                    )
                                )

        return issues


class ExplicitGetAttIntrinsic(LintRule):
    """Detect explicit GetAtt() intrinsic function calls.

    Using GetAtt("ResourceName", "Attribute") explicitly is verbose.
    The preferred style is to use attribute access: Resource.Attribute

    Detects:
    - GetAtt("MyBucket", "Arn")
    - GetAtt("MyRole", "RoleId")

    Suggests:
    - MyBucket.Arn
    - MyRole.RoleId

    This rule only flags GetAtt() calls with string literals for the resource.
    The get_att() helper function is handled by WAW006.
    """

    rule_id = "WAW020"
    description = "Avoid explicit GetAtt() intrinsic - use Resource.Attribute access"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.Call):
                func = node.func

                # Check for GetAtt() call (capital G)
                if isinstance(func, ast.Name) and func.id == "GetAtt":
                    if len(node.args) >= 2:
                        resource_arg = node.args[0]
                        attr_arg = node.args[1]

                        # Only flag when resource is a string literal
                        if isinstance(resource_arg, ast.Constant):
                            resource = resource_arg.value
                            if isinstance(resource, str):
                                # Extract attribute name
                                attr = None
                                if isinstance(attr_arg, ast.Constant):
                                    attr = attr_arg.value
                                elif isinstance(attr_arg, ast.Name):
                                    attr = attr_arg.id

                                if attr:
                                    # All attributes work with dot notation
                                    # Nested attributes like "Endpoint.Address" work via PropertyTypeProxy
                                    original = ast.get_source_segment(
                                        context.source, node
                                    )
                                    suggestion = f"{resource}.{attr}"
                                    if original:
                                        issues.append(
                                            LintIssue(
                                                rule_id=self.rule_id,
                                                message=(
                                                    f"Use {suggestion} instead of "
                                                    f'GetAtt("{resource}", ...) '
                                                    f"for attribute access"
                                                ),
                                                line=node.lineno,
                                                column=node.col_offset,
                                                original=original,
                                                suggestion=suggestion,
                                                fix_imports=[],
                                            )
                                        )

        return issues
