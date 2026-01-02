"""PropertyTypes for AWS::AppMesh::VirtualService."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class VirtualNodeServiceProvider(PropertyType):
    virtual_node_name: str | None = None


@dataclass
class VirtualRouterServiceProvider(PropertyType):
    virtual_router_name: str | None = None


@dataclass
class VirtualServiceProvider(PropertyType):
    virtual_node: VirtualNodeServiceProvider | None = None
    virtual_router: VirtualRouterServiceProvider | None = None


@dataclass
class VirtualServiceSpec(PropertyType):
    provider: VirtualServiceProvider | None = None
