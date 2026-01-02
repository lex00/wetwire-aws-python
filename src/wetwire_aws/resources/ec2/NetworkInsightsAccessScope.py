"""PropertyTypes for AWS::EC2::NetworkInsightsAccessScope."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessScopePathRequest(PropertyType):
    destination: PathStatementRequest | None = None
    source: PathStatementRequest | None = None
    through_resources: list[ThroughResourcesStatementRequest] = field(
        default_factory=list
    )


@dataclass
class PacketHeaderStatementRequest(PropertyType):
    destination_addresses: list[String] = field(default_factory=list)
    destination_ports: list[String] = field(default_factory=list)
    destination_prefix_lists: list[String] = field(default_factory=list)
    protocols: list[String] = field(default_factory=list)
    source_addresses: list[String] = field(default_factory=list)
    source_ports: list[String] = field(default_factory=list)
    source_prefix_lists: list[String] = field(default_factory=list)


@dataclass
class PathStatementRequest(PropertyType):
    packet_header_statement: PacketHeaderStatementRequest | None = None
    resource_statement: ResourceStatementRequest | None = None


@dataclass
class ResourceStatementRequest(PropertyType):
    resource_types: list[String] = field(default_factory=list)
    resources: list[String] = field(default_factory=list)


@dataclass
class ThroughResourcesStatementRequest(PropertyType):
    resource_statement: ResourceStatementRequest | None = None
