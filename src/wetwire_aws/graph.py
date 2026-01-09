"""Graph export for CloudFormation resource dependencies.

This module provides functionality to generate dependency graphs from
CloudFormation resources in DOT (Graphviz) and Mermaid formats.
"""

from __future__ import annotations

from enum import Enum

from graphviz import Digraph


class EdgeType(Enum):
    """Type of dependency edge between resources."""

    REF = "ref"
    GETATT = "getatt"


class Graph:
    """Dependency graph for CloudFormation resources."""

    def __init__(self) -> None:
        self.nodes: dict[str, str] = {}  # resource_name -> resource_type
        self.edges: list[tuple[str, str, EdgeType]] = []  # (src, dst, type)
        self.parameters: dict[str, str] = {}  # param_name -> type

    @classmethod
    def from_registry(
        cls,
        registry,
        scope_package: str | None = None,
        include_params: bool = False,
    ) -> Graph:
        """Build graph from resource registry.

        Args:
            registry: The resource registry to build from.
            scope_package: Optional package scope to filter resources.
            include_params: Whether to include parameter nodes.

        Returns:
            A Graph instance with nodes and edges populated.
        """
        from dataclass_dsl import is_attr_ref, is_class_ref

        from wetwire_aws.base import CloudFormationResource
        from wetwire_aws.decorator import param_registry

        graph = cls()

        # Get all wrapper classes
        all_wrappers = list(registry.get_all(scope_package))

        # Build a map of class to name for lookup
        class_to_name: dict[type, str] = {}
        for wrapper_cls in all_wrappers:
            name = wrapper_cls.__name__
            class_to_name[wrapper_cls] = name

            # Get resource type from inheritance
            resource_type = "Unknown"
            for base in wrapper_cls.__mro__:
                if (
                    base is not wrapper_cls
                    and hasattr(base, "_resource_type")
                    and base._resource_type
                ):
                    resource_type = base._resource_type
                    break

            graph.nodes[name] = resource_type

        # Build edges from dependencies
        for wrapper_cls in all_wrappers:
            src_name = wrapper_cls.__name__
            for attr_name, value in wrapper_cls.__dict__.items():
                if attr_name.startswith("_"):
                    continue

                if is_attr_ref(value):
                    # GetAtt reference (e.g., MyRole.Arn)
                    target_cls = value.target
                    if target_cls in class_to_name:
                        dst_name = class_to_name[target_cls]
                        graph.edges.append((src_name, dst_name, EdgeType.GETATT))
                elif is_class_ref(value):
                    # Ref reference (e.g., MyVPC)
                    if value in class_to_name:
                        dst_name = class_to_name[value]
                        graph.edges.append((src_name, dst_name, EdgeType.REF))
                elif isinstance(value, type) and issubclass(
                    value, CloudFormationResource
                ):
                    # Direct resource reference
                    if value in class_to_name:
                        dst_name = class_to_name[value]
                        graph.edges.append((src_name, dst_name, EdgeType.REF))

        # Include parameters if requested
        if include_params:
            for param_cls in param_registry.get_all(scope_package):
                name = param_cls.__name__
                param_type = getattr(param_cls, "type_", "String")
                graph.parameters[name] = param_type

        return graph

    def to_dot(self, cluster_by_service: bool = False) -> str:
        """Export graph in DOT format using graphviz library.

        Args:
            cluster_by_service: If True, group nodes by AWS service.

        Returns:
            DOT format string.
        """
        dot = Digraph()
        dot.attr(rankdir="TB")

        if cluster_by_service:
            services = self._group_by_service()
            for service, resources in services.items():
                with dot.subgraph(name=f"cluster_{service}") as s:
                    s.attr(label=service)
                    for name in resources:
                        s.node(name, f"{name}\\n{self.nodes[name]}", shape="box")
        else:
            for name, rtype in self.nodes.items():
                dot.node(name, f"{name}\\n{rtype}", shape="box")

        # Add parameter nodes with different shape
        for name, ptype in self.parameters.items():
            dot.node(name, f"{name}\\n[{ptype}]", shape="ellipse", style="dashed")

        # Edges with different styles for Ref vs GetAtt
        for src, dst, edge_type in self.edges:
            if edge_type == EdgeType.GETATT:
                dot.edge(src, dst, color="blue")
            else:
                dot.edge(src, dst)

        return dot.source

    def to_mermaid(self) -> str:
        """Export graph in Mermaid format.

        Returns:
            Mermaid format string for embedding in Markdown.
        """
        lines = ["graph TD"]

        for name, rtype in self.nodes.items():
            # Mermaid requires special handling for colons
            safe_type = rtype.replace("::", ":")
            # Node IDs can't have hyphens in some Mermaid renderers
            safe_name = name.replace("-", "_")
            lines.append(f'  {safe_name}["{name}<br/>{safe_type}"]')

        # Add parameter nodes with different shape
        for name, ptype in self.parameters.items():
            safe_name = name.replace("-", "_")
            lines.append(f'  {safe_name}(("{name}<br/>[{ptype}]"))')

        for src, dst, edge_type in self.edges:
            safe_src = src.replace("-", "_")
            safe_dst = dst.replace("-", "_")
            if edge_type == EdgeType.GETATT:
                lines.append(f"  {safe_src} -->|GetAtt| {safe_dst}")
            else:
                lines.append(f"  {safe_src} --> {safe_dst}")

        return "\n".join(lines)

    def _group_by_service(self) -> dict[str, list[str]]:
        """Group resources by AWS service.

        Returns:
            Dict mapping service name to list of resource names.
        """
        services: dict[str, list[str]] = {}
        for name, rtype in self.nodes.items():
            parts = rtype.split("::")
            service = parts[1] if len(parts) >= 2 else "Other"
            services.setdefault(service, []).append(name)
        return services
