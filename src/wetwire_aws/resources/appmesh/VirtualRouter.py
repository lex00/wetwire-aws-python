"""PropertyTypes for AWS::AppMesh::VirtualRouter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PortMapping(PropertyType):
    port: DslValue[int] | None = None
    protocol: DslValue[str] | None = None


@dataclass
class VirtualRouterListener(PropertyType):
    port_mapping: DslValue[PortMapping] | None = None


@dataclass
class VirtualRouterSpec(PropertyType):
    listeners: list[DslValue[VirtualRouterListener]] = field(default_factory=list)
