"""PropertyTypes for AWS::EC2::TransitGatewayConnectPeer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class TransitGatewayAttachmentBgpConfiguration(PropertyType):
    bgp_status: str | None = None
    peer_address: str | None = None
    peer_asn: float | None = None
    transit_gateway_address: str | None = None
    transit_gateway_asn: float | None = None


@dataclass
class TransitGatewayConnectPeerConfiguration(PropertyType):
    inside_cidr_blocks: list[String] = field(default_factory=list)
    peer_address: str | None = None
    bgp_configurations: list[TransitGatewayAttachmentBgpConfiguration] = field(
        default_factory=list
    )
    protocol: str | None = None
    transit_gateway_address: str | None = None
