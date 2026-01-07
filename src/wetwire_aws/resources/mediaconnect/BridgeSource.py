"""PropertyTypes for AWS::MediaConnect::BridgeSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BridgeFlowSource(PropertyType):
    flow_arn: DslValue[str] | None = None
    flow_vpc_interface_attachment: DslValue[VpcInterfaceAttachment] | None = None


@dataclass
class BridgeNetworkSource(PropertyType):
    multicast_ip: DslValue[str] | None = None
    network_name: DslValue[str] | None = None
    port: DslValue[int] | None = None
    protocol: DslValue[str] | None = None
    multicast_source_settings: DslValue[MulticastSourceSettings] | None = None


@dataclass
class MulticastSourceSettings(PropertyType):
    multicast_source_ip: DslValue[str] | None = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    vpc_interface_name: DslValue[str] | None = None
