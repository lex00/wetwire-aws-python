"""PropertyTypes for AWS::MediaConnect::BridgeSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BridgeFlowSource(PropertyType):
    flow_arn: str | None = None
    flow_vpc_interface_attachment: VpcInterfaceAttachment | None = None


@dataclass
class BridgeNetworkSource(PropertyType):
    multicast_ip: str | None = None
    network_name: str | None = None
    port: int | None = None
    protocol: str | None = None
    multicast_source_settings: MulticastSourceSettings | None = None


@dataclass
class MulticastSourceSettings(PropertyType):
    multicast_source_ip: str | None = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    vpc_interface_name: str | None = None
