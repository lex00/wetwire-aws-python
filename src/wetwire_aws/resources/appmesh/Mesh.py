"""PropertyTypes for AWS::AppMesh::Mesh."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EgressFilter(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class MeshServiceDiscovery(PropertyType):
    ip_preference: DslValue[str] | None = None


@dataclass
class MeshSpec(PropertyType):
    egress_filter: DslValue[EgressFilter] | None = None
    service_discovery: DslValue[MeshServiceDiscovery] | None = None
