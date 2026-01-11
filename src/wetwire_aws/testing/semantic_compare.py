"""Semantic comparison for round-trip testing.

This module provides functions to compare two data structures semantically,
ignoring formatting differences like:
- Whitespace and indentation
- Key ordering in dictionaries
- Quote style variations

Use this for testing that imported templates generate equivalent output.
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class SemanticDiff:
    """Represents a difference between two values."""

    path: str
    expected: Any
    actual: Any
    diff_type: str  # "value_changed", "missing", "extra", "type_mismatch"

    def __str__(self) -> str:
        if self.diff_type == "missing":
            return f"[{self.diff_type}] {self.path}: expected {self.expected!r}, but key is missing"
        elif self.diff_type == "extra":
            return f"[{self.diff_type}] {self.path}: unexpected key with value {self.actual!r}"
        elif self.diff_type == "type_mismatch":
            return f"[{self.diff_type}] {self.path}: expected {type(self.expected).__name__}, got {type(self.actual).__name__}"
        else:
            return f"[{self.diff_type}] {self.path}: expected {self.expected!r}, got {self.actual!r}"


def semantic_equal(expected: Any, actual: Any) -> bool:
    """Check if two values are semantically equal.

    Ignores key ordering in dictionaries but preserves order in lists.

    Args:
        expected: The expected value (e.g., from original template)
        actual: The actual value (e.g., from generated output)

    Returns:
        True if the values are semantically equal, False otherwise.
    """
    return len(semantic_compare(expected, actual)) == 0


def semantic_compare(
    expected: Any,
    actual: Any,
    path: str = "root",
) -> list[SemanticDiff]:
    """Compare two values and return a list of differences.

    Args:
        expected: The expected value (e.g., from original template)
        actual: The actual value (e.g., from generated output)
        path: The current path in the data structure (for error reporting)

    Returns:
        List of SemanticDiff objects describing differences.
    """
    diffs: list[SemanticDiff] = []

    # Handle None cases
    if expected is None and actual is None:
        return diffs
    if expected is None or actual is None:
        diffs.append(
            SemanticDiff(
                path=path,
                expected=expected,
                actual=actual,
                diff_type="value_changed",
            )
        )
        return diffs

    # Type mismatch (but allow int/float comparison)
    if type(expected) is not type(actual):
        # Allow numeric comparison between int and float
        if isinstance(expected, (int, float)) and isinstance(actual, (int, float)):
            if expected != actual:
                diffs.append(
                    SemanticDiff(
                        path=path,
                        expected=expected,
                        actual=actual,
                        diff_type="value_changed",
                    )
                )
            return diffs

        diffs.append(
            SemanticDiff(
                path=path,
                expected=expected,
                actual=actual,
                diff_type="type_mismatch",
            )
        )
        return diffs

    # Dictionary comparison
    if isinstance(expected, dict):
        expected_keys = set(expected.keys())
        actual_keys = set(actual.keys())

        # Check for missing keys
        for key in expected_keys - actual_keys:
            diffs.append(
                SemanticDiff(
                    path=f"{path}.{key}",
                    expected=expected[key],
                    actual=None,
                    diff_type="missing",
                )
            )

        # Check for extra keys
        for key in actual_keys - expected_keys:
            diffs.append(
                SemanticDiff(
                    path=f"{path}.{key}",
                    expected=None,
                    actual=actual[key],
                    diff_type="extra",
                )
            )

        # Compare common keys recursively
        for key in expected_keys & actual_keys:
            diffs.extend(
                semantic_compare(
                    expected[key],
                    actual[key],
                    f"{path}.{key}",
                )
            )

        return diffs

    # List comparison (order matters)
    if isinstance(expected, list):
        # Compare lengths
        if len(expected) != len(actual):
            diffs.append(
                SemanticDiff(
                    path=f"{path}[length]",
                    expected=len(expected),
                    actual=len(actual),
                    diff_type="value_changed",
                )
            )
            # Still compare elements up to the shorter length
            min_len = min(len(expected), len(actual))
        else:
            min_len = len(expected)

        # Compare elements
        for i in range(min_len):
            diffs.extend(
                semantic_compare(
                    expected[i],
                    actual[i],
                    f"{path}[{i}]",
                )
            )

        return diffs

    # Scalar comparison
    if expected != actual:
        diffs.append(
            SemanticDiff(
                path=path,
                expected=expected,
                actual=actual,
                diff_type="value_changed",
            )
        )

    return diffs


def format_diffs(diffs: list[SemanticDiff], max_diffs: int = 10) -> str:
    """Format a list of differences as a human-readable string.

    Args:
        diffs: List of SemanticDiff objects
        max_diffs: Maximum number of diffs to show (default 10)

    Returns:
        Formatted string describing the differences
    """
    if not diffs:
        return "No differences"

    lines = []
    for i, diff in enumerate(diffs[:max_diffs]):
        lines.append(str(diff))

    if len(diffs) > max_diffs:
        lines.append(f"... and {len(diffs) - max_diffs} more differences")

    return "\n".join(lines)
