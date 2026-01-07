"""PropertyTypes for AWS::NetworkManager::CoreNetwork."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CoreNetworkEdge(PropertyType):
    asn: DslValue[float] | None = None
    edge_location: DslValue[str] | None = None
    inside_cidr_blocks: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CoreNetworkNetworkFunctionGroup(PropertyType):
    edge_locations: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    segments: DslValue[Segments] | None = None


@dataclass
class CoreNetworkSegment(PropertyType):
    edge_locations: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    shared_segments: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Segments(PropertyType):
    send_to: list[DslValue[str]] = field(default_factory=list)
    send_via: list[DslValue[str]] = field(default_factory=list)
