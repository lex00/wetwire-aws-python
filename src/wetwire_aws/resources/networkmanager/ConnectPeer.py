"""PropertyTypes for AWS::NetworkManager::ConnectPeer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BgpOptions(PropertyType):
    peer_asn: DslValue[float] | None = None


@dataclass
class ConnectPeerBgpConfiguration(PropertyType):
    core_network_address: DslValue[str] | None = None
    core_network_asn: DslValue[float] | None = None
    peer_address: DslValue[str] | None = None
    peer_asn: DslValue[float] | None = None


@dataclass
class ConnectPeerConfiguration(PropertyType):
    bgp_configurations: list[DslValue[ConnectPeerBgpConfiguration]] = field(
        default_factory=list
    )
    core_network_address: DslValue[str] | None = None
    inside_cidr_blocks: list[DslValue[str]] = field(default_factory=list)
    peer_address: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
