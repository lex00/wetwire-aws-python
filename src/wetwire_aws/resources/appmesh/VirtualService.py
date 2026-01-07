"""PropertyTypes for AWS::AppMesh::VirtualService."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class VirtualNodeServiceProvider(PropertyType):
    virtual_node_name: DslValue[str] | None = None


@dataclass
class VirtualRouterServiceProvider(PropertyType):
    virtual_router_name: DslValue[str] | None = None


@dataclass
class VirtualServiceProvider(PropertyType):
    virtual_node: DslValue[VirtualNodeServiceProvider] | None = None
    virtual_router: DslValue[VirtualRouterServiceProvider] | None = None


@dataclass
class VirtualServiceSpec(PropertyType):
    provider: DslValue[VirtualServiceProvider] | None = None
