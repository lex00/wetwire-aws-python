"""PropertyTypes for AWS::NetworkManager::CoreNetwork."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CoreNetworkEdge(PropertyType):
    asn: float | None = None
    edge_location: str | None = None
    inside_cidr_blocks: list[String] = field(default_factory=list)


@dataclass
class CoreNetworkNetworkFunctionGroup(PropertyType):
    edge_locations: list[String] = field(default_factory=list)
    name: str | None = None
    segments: Segments | None = None


@dataclass
class CoreNetworkSegment(PropertyType):
    edge_locations: list[String] = field(default_factory=list)
    name: str | None = None
    shared_segments: list[String] = field(default_factory=list)


@dataclass
class Segments(PropertyType):
    send_to: list[String] = field(default_factory=list)
    send_via: list[String] = field(default_factory=list)
