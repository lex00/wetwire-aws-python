"""PropertyTypes for AWS::NetworkManager::ConnectPeer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BgpOptions(PropertyType):
    peer_asn: float | None = None


@dataclass
class ConnectPeerBgpConfiguration(PropertyType):
    core_network_address: str | None = None
    core_network_asn: float | None = None
    peer_address: str | None = None
    peer_asn: float | None = None


@dataclass
class ConnectPeerConfiguration(PropertyType):
    bgp_configurations: list[ConnectPeerBgpConfiguration] = field(default_factory=list)
    core_network_address: str | None = None
    inside_cidr_blocks: list[String] = field(default_factory=list)
    peer_address: str | None = None
    protocol: str | None = None
