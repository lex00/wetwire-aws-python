"""PropertyTypes for AWS::MediaLive::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ClusterNetworkSettings(PropertyType):
    default_route: str | None = None
    interface_mappings: list[InterfaceMapping] = field(default_factory=list)


@dataclass
class InterfaceMapping(PropertyType):
    logical_interface_name: str | None = None
    network_id: str | None = None


@dataclass
class Tags(PropertyType):
    key: str | None = None
    value: str | None = None
