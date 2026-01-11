"""Dependency-related lint rules.

Rules:
    WAW022: Detect circular dependencies between resources
"""

from __future__ import annotations

import ast

from wetwire_aws.linter.rules.base import LintContext, LintIssue, LintRule


def _is_resource_class(node: ast.ClassDef) -> bool:
    """Check if a class definition is a CloudFormation resource.

    Resource classes:
    - Inherit from a module attribute like s3.Bucket
    - Have a 'resource:' annotation
    """
    # Check for inheritance from resource types (e.g., s3.Bucket)
    for base in node.bases:
        if isinstance(base, ast.Attribute):
            return True
    # Check for resource: annotation
    for stmt in node.body:
        if isinstance(stmt, ast.AnnAssign):
            if isinstance(stmt.target, ast.Name) and stmt.target.id == "resource":
                return True
    return False


def _extract_references(node: ast.ClassDef, all_class_names: set[str]) -> set[str]:
    """Extract class names that this class references.

    Looks for:
    - Direct name references: field = OtherClass
    - List/dict containing references: field = [OtherClass]
    - Attribute references: field = OtherClass.Arn
    """
    refs: set[str] = set()

    for stmt in node.body:
        if isinstance(stmt, ast.Assign):
            for value in _walk_value(stmt.value):
                if isinstance(value, ast.Name) and value.id in all_class_names:
                    refs.add(value.id)
                elif isinstance(value, ast.Attribute):
                    if (
                        isinstance(value.value, ast.Name)
                        and value.value.id in all_class_names
                    ):
                        refs.add(value.value.id)

    return refs


def _walk_value(node: ast.AST):
    """Walk through a value expression and yield all nodes."""
    yield node
    for child in ast.iter_child_nodes(node):
        yield from _walk_value(child)


def _find_cycles(
    graph: dict[str, set[str]],
) -> list[list[str]]:
    """Find all cycles in a directed graph using DFS.

    Args:
        graph: Adjacency list representation (node -> set of neighbors)

    Returns:
        List of cycles, each cycle is a list of node names.
    """
    visited: set[str] = set()
    rec_stack: list[str] = []
    rec_set: set[str] = set()
    cycles: list[list[str]] = []

    def dfs(node: str) -> None:
        visited.add(node)
        rec_stack.append(node)
        rec_set.add(node)

        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                dfs(neighbor)
            elif neighbor in rec_set:
                # Found a cycle
                cycle_start = rec_stack.index(neighbor)
                cycle = rec_stack[cycle_start:] + [neighbor]
                cycles.append(cycle)

        rec_stack.pop()
        rec_set.remove(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return cycles


def _normalize_cycle(cycle: list[str]) -> tuple[str, ...]:
    """Normalize a cycle to a canonical form for deduplication.

    Rotates the cycle so the smallest element is first.
    """
    if not cycle or len(cycle) < 2:
        return tuple(cycle)

    # Remove the duplicate last element (closing the cycle)
    if cycle[0] == cycle[-1]:
        cycle = cycle[:-1]

    # Find the minimum element's index
    min_idx = cycle.index(min(cycle))
    # Rotate
    normalized = cycle[min_idx:] + cycle[:min_idx]
    return tuple(normalized)


class CircularDependency(LintRule):
    """Detect circular dependencies between resources.

    Circular dependencies in CloudFormation cause deployment failures.
    This rule detects cycles in the resource dependency graph.

    Example of a cycle:
        class BucketA(s3.Bucket):
            bucket_name = BucketB

        class BucketB(s3.Bucket):
            bucket_name = BucketA
    """

    rule_id = "WAW022"
    description = "Avoid circular dependencies between resources"

    def check(self, context: LintContext) -> list[LintIssue]:
        issues = []

        # First pass: collect all resource class names and their locations
        resource_classes: dict[str, ast.ClassDef] = {}
        for node in ast.walk(context.tree):
            if isinstance(node, ast.ClassDef) and _is_resource_class(node):
                resource_classes[node.name] = node

        all_class_names = set(resource_classes.keys())

        # Second pass: build dependency graph
        graph: dict[str, set[str]] = {}
        for name, node in resource_classes.items():
            refs = _extract_references(node, all_class_names)
            graph[name] = refs

        # Find cycles
        cycles = _find_cycles(graph)

        # Normalize and deduplicate cycles
        seen_cycles: set[tuple[str, ...]] = set()
        for cycle in cycles:
            normalized = _normalize_cycle(cycle)
            if normalized not in seen_cycles:
                seen_cycles.add(normalized)

                # Report the cycle
                if len(normalized) > 0:
                    cycle_str = " -> ".join(normalized) + " -> " + normalized[0]
                    first_node = normalized[0]
                    node = resource_classes.get(first_node)
                    line = node.lineno if node else 1

                    issues.append(
                        LintIssue(
                            rule_id=self.rule_id,
                            message=f"Circular dependency detected: {cycle_str}",
                            line=line,
                            column=0,
                            original="",
                            suggestion="Break the cycle by removing one of the dependencies",
                            fix_imports=[],
                        )
                    )

        return issues
