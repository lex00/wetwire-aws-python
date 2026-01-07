"""PropertyTypes for AWS::MediaLive::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ClusterNetworkSettings(PropertyType):
    default_route: DslValue[str] | None = None
    interface_mappings: list[DslValue[InterfaceMapping]] = field(default_factory=list)


@dataclass
class InterfaceMapping(PropertyType):
    logical_interface_name: DslValue[str] | None = None
    network_id: DslValue[str] | None = None


@dataclass
class Tags(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
