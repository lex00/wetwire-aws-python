"""Base classes for lint rules.

This module defines the core data structures and abstract base class
for all lint rules.
"""

from __future__ import annotations

import ast
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class LintIssue:
    """A detected lint issue with fix information.

    Represents a single issue found by a lint rule, including all information
    needed to display the issue and optionally auto-fix it.

    Attributes:
        rule_id: The rule identifier (e.g., "WAW001").
        message: Human-readable description of the issue.
        line: Line number where the issue was found (1-indexed).
        column: Column number where the issue was found (0-indexed).
        original: The original code that should be replaced (empty for insertions).
        suggestion: The suggested replacement code (or line to insert).
        fix_imports: List of import statements needed for the fix.
        insert_after_line: If set, insert suggestion as new line after this line number.
            Line 0 means insert at the very beginning (after module docstring if present).
    """

    rule_id: str
    message: str
    line: int
    column: int
    original: str
    suggestion: str
    fix_imports: list[str]
    insert_after_line: int | None = None


@dataclass
class LintContext:
    """Context for linting, including source code and AST.

    Provides all the information a lint rule needs to analyze code.

    Attributes:
        source: The original source code as a string.
        tree: The parsed AST of the source code.
        filename: The filename for error messages (default: "<unknown>").
    """

    source: str
    tree: ast.AST
    filename: str = "<unknown>"


class LintRule(ABC):
    """Abstract base class for lint rules.

    Each lint rule must define a rule_id, description, and implement
    the check() method to detect issues.

    Attributes:
        rule_id: Unique identifier for the rule (e.g., "WAW001").
        description: Human-readable description of what the rule checks.
    """

    rule_id: str
    description: str

    @abstractmethod
    def check(self, context: LintContext) -> list[LintIssue]:
        """Check code for issues matching this rule.

        Args:
            context: The lint context containing source and AST.

        Returns:
            List of LintIssue objects for each detected issue.
        """
        pass
