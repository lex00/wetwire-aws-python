"""
Name conversion utilities for CloudFormation to Python.

Re-exports utilities from dataclass-dsl with enhanced sanitization for
CloudFormation identifiers that may contain hyphens or other invalid chars.
"""

from __future__ import annotations

import re

# Re-export from dataclass-dsl for backward compatibility
from dataclass_dsl import (
    PYTHON_KEYWORDS,
    is_valid_python_identifier,
    to_pascal_case,
    to_snake_case,
)
from dataclass_dsl import sanitize_class_name as _base_sanitize_class_name
from dataclass_dsl import sanitize_python_name as _base_sanitize_python_name

__all__ = [
    "PYTHON_KEYWORDS",
    "to_snake_case",
    "to_pascal_case",
    "sanitize_python_name",
    "sanitize_class_name",
    "is_valid_python_identifier",
]


def _replace_hyphens(name: str) -> str:
    """Replace hyphens with meaningful alternatives.

    - Leading hyphen followed by digit: Neg (e.g., -1 -> Neg1)
    - Hyphen between letters: remove and capitalize next letter (kebab-case -> camelCase)
    - Other hyphens: underscore

    Examples:
        Port-1ICMP -> PortNeg1ICMP
        my-resource -> MyResource (when used with to_pascal_case)
        test-name -> test_name (for snake_case contexts)
    """
    if not name or "-" not in name:
        return name

    result = []
    i = 0
    while i < len(name):
        char = name[i]
        if char == "-":
            # Check what follows the hyphen
            if i + 1 < len(name):
                next_char = name[i + 1]
                if next_char.isdigit():
                    # -1 -> Neg1
                    result.append("Neg")
                elif next_char.isalpha():
                    # my-resource -> myResource (capitalize next letter)
                    result.append(next_char.upper())
                    i += 1  # Skip the next char since we already added it
                else:
                    result.append("_")
            else:
                # Trailing hyphen
                result.append("_")
        else:
            result.append(char)
        i += 1

    return "".join(result)


def sanitize_class_name(name: str) -> str:
    """Sanitize a name for use as a Python class name.

    Handles CloudFormation identifiers with hyphens, leading digits, etc.

    Examples:
        Port-1ICMP -> PortNeg1ICMP
        my-resource -> MyResource
        123test -> _123test
        class -> Class_ (or similar)
    """
    # First handle hyphens
    sanitized = _replace_hyphens(name)

    # Then apply base sanitization (handles keywords, leading digits, etc.)
    result = _base_sanitize_class_name(sanitized)

    # Ensure result is valid (base might leave invalid chars in some edge cases)
    if not is_valid_python_identifier(result):
        # Remove any remaining invalid characters
        result = re.sub(r"[^a-zA-Z0-9_]", "", result)
        if not result or result[0].isdigit():
            result = "_" + result

    return result


def sanitize_python_name(name: str) -> str:
    """Sanitize a name for use as a Python variable/field name.

    Handles CloudFormation identifiers with hyphens, leading digits, etc.

    Examples:
        Port-1ICMP -> port_neg1_icmp (snake_case)
        my-resource -> my_resource
        123test -> _123test
        class -> class_
    """
    # First handle hyphens (replace with underscore for snake_case)
    sanitized = name.replace("-", "_")

    # Then apply base sanitization
    result = _base_sanitize_python_name(sanitized)

    # Ensure result is valid
    if not is_valid_python_identifier(result):
        # Remove any remaining invalid characters
        result = re.sub(r"[^a-zA-Z0-9_]", "", result)
        if not result or result[0].isdigit():
            result = "_" + result

    return result
