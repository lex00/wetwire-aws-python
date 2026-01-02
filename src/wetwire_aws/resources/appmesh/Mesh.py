"""PropertyTypes for AWS::AppMesh::Mesh."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EgressFilter(PropertyType):
    type_: str | None = None


@dataclass
class MeshServiceDiscovery(PropertyType):
    ip_preference: str | None = None


@dataclass
class MeshSpec(PropertyType):
    egress_filter: EgressFilter | None = None
    service_discovery: MeshServiceDiscovery | None = None
