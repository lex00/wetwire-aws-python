"""PropertyTypes for AWS::AppMesh::VirtualRouter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PortMapping(PropertyType):
    port: int | None = None
    protocol: str | None = None


@dataclass
class VirtualRouterListener(PropertyType):
    port_mapping: PortMapping | None = None


@dataclass
class VirtualRouterSpec(PropertyType):
    listeners: list[VirtualRouterListener] = field(default_factory=list)
