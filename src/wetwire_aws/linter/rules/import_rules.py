"""Import-related lint rules.

Rules:
    WAW007: Use flat imports with module-qualified names instead of explicit resource imports
    WAW008: Remove verbose imports that setup_params/setup_resources handle
    WAW018: Remove redundant relative import (already available via 'from . import *')
"""

from __future__ import annotations

import ast

from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule


class ExplicitResourceImport(LintRule):
    """Detect explicit imports from wetwire_aws.resources that should use flat imports.

    Resource files should use `from . import *` and access types via module-qualified
    names (e.g., `lambda_.Runtime`, `s3.ServerSideEncryption`) rather than explicit
    imports. The `setup_resources()` function injects all service modules automatically.

    Detects:
    - from wetwire_aws.resources.lambda_ import Runtime
    - from wetwire_aws.resources.s3 import ServerSideEncryption
    - from wetwire_aws.resources import ec2, lambda_  (redundant in packages using setup_resources)

    Suggests:
    - Remove the import line
    - Qualify usages: Runtime.PYTHON3_12 -> lambda_.Runtime.PYTHON3_12
    """

    rule_id = "WAW007"
    description = "Use flat imports with module-qualified names instead of explicit resource imports"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # Check if this file uses setup_resources (indicating it's a package __init__)
        uses_setup_resources = "setup_resources" in context.source

        # First pass: collect all explicit resource imports
        # Maps imported name -> service module (e.g., "Runtime" -> "lambda_")
        imported_names: dict[str, str] = {}
        import_lines_to_remove: set[int] = set()

        for node in ast.walk(context.tree):
            if isinstance(node, ast.ImportFrom):
                module = node.module or ""

                # Check for imports from wetwire_aws.resources.* (e.g., lambda_, s3)
                if module.startswith("wetwire_aws.resources."):
                    # Extract the service module name (e.g., "lambda_", "s3")
                    parts = module.split(".")
                    if len(parts) >= 3:
                        service_module = parts[2]  # e.g., "lambda_", "s3"

                        for alias in node.names:
                            imported_name = alias.asname or alias.name
                            imported_names[imported_name] = service_module

                        # Mark this line for removal (only once per line)
                        if node.lineno not in import_lines_to_remove:
                            import_lines_to_remove.add(node.lineno)
                            original = ast.get_source_segment(context.source, node)
                            if original:
                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message="Remove explicit resource import; use module-qualified names",
                                        line=node.lineno,
                                        column=node.col_offset,
                                        original=original,
                                        suggestion="",  # Remove the line
                                        fix_imports=[],
                                    )
                                )

                # Check for imports from wetwire_aws.resources (module imports)
                # These are redundant in packages using setup_resources()
                elif module == "wetwire_aws.resources" and uses_setup_resources:
                    if node.lineno not in import_lines_to_remove:
                        import_lines_to_remove.add(node.lineno)
                        original = ast.get_source_segment(context.source, node)
                        if original:
                            issues.append(
                                LintIssue(
                                    rule_id=self.rule_id,
                                    message="Remove redundant import; setup_resources() handles module injection",
                                    line=node.lineno,
                                    column=node.col_offset,
                                    original=original,
                                    suggestion="",  # Remove the line
                                    fix_imports=[],
                                )
                            )

        # Second pass: find usages of imported names and qualify them
        if imported_names:
            for node in ast.walk(context.tree):
                # Look for attribute access like Runtime.PYTHON3_12
                if isinstance(node, ast.Attribute):
                    if isinstance(node.value, ast.Name):
                        name = node.value.id
                        if name in imported_names:
                            service_module = imported_names[name]
                            # Get the full attribute access expression
                            original = ast.get_source_segment(context.source, node)
                            if original:
                                # Replace Name.attr with module.Name.attr
                                qualified = f"{service_module}.{original}"
                                issues.append(
                                    LintIssue(
                                        rule_id=self.rule_id,
                                        message=f"Use module-qualified name: {qualified}",
                                        line=node.lineno,
                                        column=node.col_offset,
                                        original=original,
                                        suggestion=qualified,
                                        fix_imports=[],
                                    )
                                )

        return issues


class VerboseInitImports(LintRule):
    """Detect verbose imports in __init__.py that setup_params/setup_resources handle.

    When a package uses `setup_params()` and `setup_resources()`, they inject all
    needed AWS types. The __init__.py only needs:
        from wetwire_aws.loader import setup_params, setup_resources
        setup_params(globals())
        from .params import *
        setup_resources(__file__, __name__, globals())

    Detects:
    - from wetwire_aws import (...)  (multi-line import blocks)
    - from wetwire_aws.params import (...)  (should use setup_params instead)
    - from wetwire_aws.intrinsics import (...)  (should use setup_params instead)
    - __all__ = [...]  (explicit exports, not needed)

    Suggests:
    - Remove the verbose import block
    - Remove the __all__ definition
    """

    rule_id = "WAW008"
    description = "Remove verbose imports that setup_params/setup_resources handle"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # Only apply to files that use setup_resources (package __init__ files)
        if "setup_resources" not in context.source:
            return issues

        lines = context.source.splitlines(keepends=True)

        # Find and mark verbose import blocks for removal
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.lstrip()

            # Detect verbose multi-line imports that setup_params handles:
            # - from wetwire_aws import (...)
            # - from wetwire_aws.params import (...)
            # - from wetwire_aws.intrinsics import (...)
            # But keep: from wetwire_aws.loader import setup_params, setup_resources
            verbose_prefixes = [
                "from wetwire_aws import (",
                "from wetwire_aws.params import (",
                "from wetwire_aws.intrinsics import (",
            ]

            if any(stripped.startswith(prefix) for prefix in verbose_prefixes):
                # Find the end of this import block
                start_line = i
                end_line = i
                paren_count = line.count("(") - line.count(")")
                while paren_count > 0 and end_line < len(lines) - 1:
                    end_line += 1
                    paren_count += lines[end_line].count("(")
                    paren_count -= lines[end_line].count(")")

                # Get the full multi-line import as original
                original_lines = lines[start_line : end_line + 1]
                original = "".join(original_lines).rstrip("\n")

                issues.append(
                    LintIssue(
                        rule_id=self.rule_id,
                        message="Remove verbose import; use setup_params() instead",
                        line=start_line + 1,  # 1-indexed
                        column=0,
                        original=original,
                        suggestion="",  # Remove entirely
                        fix_imports=[],
                    )
                )
                i = end_line + 1
                continue

            # Detect: __all__ = [
            if stripped.startswith("__all__") and "=" in stripped and "[" in stripped:
                # Find the end of this __all__ block
                start_line = i
                end_line = i
                bracket_count = line.count("[") - line.count("]")
                while bracket_count > 0 and end_line < len(lines) - 1:
                    end_line += 1
                    bracket_count += lines[end_line].count("[")
                    bracket_count -= lines[end_line].count("]")

                # Get the full multi-line __all__ as original
                original_lines = lines[start_line : end_line + 1]
                original = "".join(original_lines).rstrip("\n")

                issues.append(
                    LintIssue(
                        rule_id=self.rule_id,
                        message="Remove __all__; setup_resources() exports all classes automatically",
                        line=start_line + 1,  # 1-indexed
                        column=0,
                        original=original,
                        suggestion="",  # Remove entirely
                        fix_imports=[],
                    )
                )
                i = end_line + 1
                continue

            i += 1

        return issues


class RedundantRelativeImport(LintRule):
    """Detect redundant relative imports when using `from . import *`.

    When a file uses `from . import *` (which relies on setup_resources),
    explicit imports like `from .network import MyVPC` are redundant
    because all classes are already injected into the namespace.

    Detects:
    - from . import *
    - from .module import SomeClass  # redundant

    Suggests:
    - Remove the explicit import
    """

    rule_id = "WAW018"
    description = (
        "Remove redundant relative import (already available via 'from . import *')"
    )

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        has_star_import = False
        redundant_imports = []

        for node in ast.walk(context.tree):
            if isinstance(node, ast.ImportFrom):
                if node.module is None and node.level == 1:
                    # from . import *
                    for alias in node.names:
                        if alias.name == "*":
                            has_star_import = True
                            break
                elif node.level == 1 and node.module is not None:
                    # from .module import Something
                    redundant_imports.append(node)

        if has_star_import:
            for node in redundant_imports:
                names = ", ".join(alias.name for alias in node.names)
                issues.append(
                    LintIssue(
                        rule_id=self.rule_id,
                        message=f"Redundant import: {names} (already available via 'from . import *')",
                        line=node.lineno,
                        column=node.col_offset,
                        original=f"from .{node.module} import {names}",
                        suggestion="# Remove this line - classes are injected by setup_resources()",
                        fix_imports=[],
                    )
                )

        return issues
