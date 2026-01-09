"""CLI utilities for wetwire-aws.

This module provides common helper functions for CLI commands, reducing
code duplication across command implementations.

Re-exports CLI utilities from dataclass-dsl for backward compatibility.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import TYPE_CHECKING, Any, NoReturn

# Re-export from dataclass-dsl for backward compatibility
from dataclass_dsl import (
    add_common_args,
    create_list_command,
    create_validate_command,
    discover_resources,
)

if TYPE_CHECKING:
    import argparse


def error_exit(message: str, hint: str | None = None) -> NoReturn:
    """Print an error message and exit with status 1.

    Args:
        message: The error message to display.
        hint: Optional hint text to help the user fix the issue.
    """
    print(f"Error: {message}", file=sys.stderr)
    if hint:
        print(f"Hint: {hint}", file=sys.stderr)
    sys.exit(1)


def validate_package_path(path: str) -> tuple[Path, str]:
    """Validate that a path is a valid Python package directory.

    Checks that:
    1. The path exists
    2. It's a directory
    3. It contains an __init__.py file

    Also adds the parent directory to sys.path so the package can be imported.

    Args:
        path: The path to validate.

    Returns:
        A tuple of (package_path, module_name).

    Raises:
        SystemExit: If validation fails.
    """
    package_path = Path(path).resolve()

    if not package_path.exists():
        error_exit(f"Path does not exist: {path}")

    if not package_path.is_dir():
        error_exit(f"Path is not a directory: {path}")

    if not (package_path / "__init__.py").exists():
        error_exit(
            f"Path is not a Python package (missing __init__.py): {path}",
            hint="Ensure the directory contains an __init__.py file.",
        )

    # Add parent directory to sys.path so the package can be imported
    parent_dir = str(package_path.parent)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

    return package_path, package_path.name


def require_optional_dependency(
    module: str,
    package: str,
    extra: str,
    import_from: str | None = None,
) -> Any:
    """Import an optional dependency, with helpful error message on failure.

    Args:
        module: The module name to import (e.g., "wetwire_aws.kiro").
        package: The package name for display (e.g., "Kiro integration").
        extra: The pip extra to install (e.g., "kiro").
        import_from: Optional attribute to import from the module.

    Returns:
        The imported module or attribute.

    Raises:
        SystemExit: If the import fails.
    """
    try:
        imported = __import__(module, fromlist=[import_from] if import_from else [])
        if import_from:
            return getattr(imported, import_from)
        return imported
    except ImportError:
        error_exit(
            f"{package} requires additional dependencies.",
            hint=f"Install with: pip install wetwire-aws[{extra}]",
        )


def resolve_output_dir(args: argparse.Namespace, attr: str = "output") -> Path:
    """Resolve the output directory from command arguments.

    Args:
        args: Parsed command-line arguments.
        attr: The attribute name for the output directory (default: "output").

    Returns:
        The resolved output directory Path, defaulting to current directory.
    """
    output = getattr(args, attr, None)
    return Path(output) if output else Path.cwd()


__all__ = [
    # Re-exported from dataclass-dsl
    "discover_resources",
    "add_common_args",
    "create_list_command",
    "create_validate_command",
    # New helpers
    "error_exit",
    "validate_package_path",
    "require_optional_dependency",
    "resolve_output_dir",
]
