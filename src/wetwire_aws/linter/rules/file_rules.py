"""File-level lint rules.

Rules:
    WAW010: Split large files into smaller ones
    WAW012: Detect duplicate resource class names
"""

from __future__ import annotations

import ast

from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule


class FileTooLarge(LintRule):
    """Detect files with too many resources that should be split.

    Large files are harder to read, navigate, and maintain. Files with more
    than MAX_RESOURCES (default 15) resources should be split into smaller,
    focused files by category (storage, compute, network, security, etc.).

    The rule counts @wetwire_aws decorated classes in the file.

    Detects:
    - Files with > 15 @wetwire_aws decorated classes

    Suggests:
    - Split file into category-based files (storage.py, compute.py, etc.)
    """

    rule_id = "WAW010"
    description = "Split large files into smaller ones"
    MAX_RESOURCES = 15

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # Count @wetwire_aws decorated classes
        resource_classes: list[tuple[str, int]] = []  # (name, line)

        for node in ast.walk(context.tree):
            if isinstance(node, ast.ClassDef):
                # Check if this class has @wetwire_aws decorator
                if self._has_wetwire_aws_decorator(node):
                    resource_classes.append((node.name, node.lineno))

        count = len(resource_classes)
        if count > self.MAX_RESOURCES:
            # Build a list of the resource names for the message
            names = [name for name, _ in resource_classes[:5]]
            if count > 5:
                names.append(f"... and {count - 5} more")

            issues.append(
                LintIssue(
                    rule_id=self.rule_id,
                    message=(
                        f"File has {count} resources (max {self.MAX_RESOURCES}). "
                        f"Consider splitting by category: storage.py, compute.py, "
                        f"network.py, security.py"
                    ),
                    line=1,  # File-level issue
                    column=0,
                    original="",  # No specific code to replace
                    suggestion=f"# Split {count} resources into multiple files",
                    fix_imports=[],
                )
            )

        return issues

    def _has_wetwire_aws_decorator(self, class_node: ast.ClassDef) -> bool:
        """Check if a class has the @wetwire_aws decorator."""
        for decorator in class_node.decorator_list:
            if isinstance(decorator, ast.Name) and decorator.id == "wetwire_aws":
                return True
            if isinstance(decorator, ast.Attribute) and decorator.attr == "wetwire_aws":
                return True
        return False


class DuplicateResource(LintRule):
    """Detect duplicate @wetwire_aws class names within a file.

    CloudFormation logical resource names must be unique within a template.
    This rule catches duplicate class definitions early, at the Python level.

    Detects:
    - Two or more @wetwire_aws decorated classes with the same name in one file

    Note: Cross-file duplicate detection requires package-level analysis and
    is handled separately by setup_resources() at runtime.
    """

    rule_id = "WAW012"
    description = "Detect duplicate resource class names"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # Track class names and their locations
        class_locations: dict[str, list[tuple[int, int]]] = {}  # name -> [(line, col)]

        for node in ast.walk(context.tree):
            if isinstance(node, ast.ClassDef):
                # Check if this class has @wetwire_aws decorator
                if self._has_wetwire_aws_decorator(node):
                    name = node.name
                    if name not in class_locations:
                        class_locations[name] = []
                    class_locations[name].append((node.lineno, node.col_offset))

        # Report duplicates
        for name, locations in class_locations.items():
            if len(locations) > 1:
                # First occurrence is okay, report subsequent ones
                for line, col in locations[1:]:
                    first_line = locations[0][0]
                    issues.append(
                        LintIssue(
                            rule_id=self.rule_id,
                            message=(
                                f"Duplicate resource class '{name}' "
                                f"(first defined at line {first_line})"
                            ),
                            line=line,
                            column=col,
                            original=f"class {name}:",
                            suggestion=f"# DUPLICATE: class {name}:",
                            fix_imports=[],
                        )
                    )

        return issues

    def _has_wetwire_aws_decorator(self, class_node: ast.ClassDef) -> bool:
        """Check if a class has the @wetwire_aws decorator."""
        for decorator in class_node.decorator_list:
            if isinstance(decorator, ast.Name) and decorator.id == "wetwire_aws":
                return True
            if isinstance(decorator, ast.Attribute) and decorator.attr == "wetwire_aws":
                return True
        return False
