"""PropertyTypes for AWS::EC2::NetworkInsightsAccessScope."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessScopePathRequest(PropertyType):
    destination: DslValue[PathStatementRequest] | None = None
    source: DslValue[PathStatementRequest] | None = None
    through_resources: list[DslValue[ThroughResourcesStatementRequest]] = field(
        default_factory=list
    )


@dataclass
class PacketHeaderStatementRequest(PropertyType):
    destination_addresses: list[DslValue[str]] = field(default_factory=list)
    destination_ports: list[DslValue[str]] = field(default_factory=list)
    destination_prefix_lists: list[DslValue[str]] = field(default_factory=list)
    protocols: list[DslValue[str]] = field(default_factory=list)
    source_addresses: list[DslValue[str]] = field(default_factory=list)
    source_ports: list[DslValue[str]] = field(default_factory=list)
    source_prefix_lists: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PathStatementRequest(PropertyType):
    packet_header_statement: DslValue[PacketHeaderStatementRequest] | None = None
    resource_statement: DslValue[ResourceStatementRequest] | None = None


@dataclass
class ResourceStatementRequest(PropertyType):
    resource_types: list[DslValue[str]] = field(default_factory=list)
    resources: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ThroughResourcesStatementRequest(PropertyType):
    resource_statement: DslValue[ResourceStatementRequest] | None = None
