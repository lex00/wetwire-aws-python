"""PropertyTypes for AWS::EC2::TransitGatewayConnectPeer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class TransitGatewayAttachmentBgpConfiguration(PropertyType):
    bgp_status: DslValue[str] | None = None
    peer_address: DslValue[str] | None = None
    peer_asn: DslValue[float] | None = None
    transit_gateway_address: DslValue[str] | None = None
    transit_gateway_asn: DslValue[float] | None = None


@dataclass
class TransitGatewayConnectPeerConfiguration(PropertyType):
    inside_cidr_blocks: list[DslValue[str]] = field(default_factory=list)
    peer_address: DslValue[str] | None = None
    bgp_configurations: list[DslValue[TransitGatewayAttachmentBgpConfiguration]] = (
        field(default_factory=list)
    )
    protocol: DslValue[str] | None = None
    transit_gateway_address: DslValue[str] | None = None
