"""PropertyTypes for AWS::MediaConnect::Bridge."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BridgeFlowSource(PropertyType):
    flow_arn: str | None = None
    name: str | None = None
    flow_vpc_interface_attachment: VpcInterfaceAttachment | None = None


@dataclass
class BridgeNetworkOutput(PropertyType):
    ip_address: str | None = None
    name: str | None = None
    network_name: str | None = None
    port: int | None = None
    protocol: str | None = None
    ttl: int | None = None


@dataclass
class BridgeNetworkSource(PropertyType):
    multicast_ip: str | None = None
    name: str | None = None
    network_name: str | None = None
    port: int | None = None
    protocol: str | None = None
    multicast_source_settings: MulticastSourceSettings | None = None


@dataclass
class BridgeOutput(PropertyType):
    network_output: BridgeNetworkOutput | None = None


@dataclass
class BridgeSource(PropertyType):
    flow_source: BridgeFlowSource | None = None
    network_source: BridgeNetworkSource | None = None


@dataclass
class EgressGatewayBridge(PropertyType):
    max_bitrate: int | None = None


@dataclass
class FailoverConfig(PropertyType):
    failover_mode: str | None = None
    source_priority: SourcePriority | None = None
    state: str | None = None


@dataclass
class IngressGatewayBridge(PropertyType):
    max_bitrate: int | None = None
    max_outputs: int | None = None


@dataclass
class MulticastSourceSettings(PropertyType):
    multicast_source_ip: str | None = None


@dataclass
class SourcePriority(PropertyType):
    primary_source: str | None = None


@dataclass
class VpcInterfaceAttachment(PropertyType):
    vpc_interface_name: str | None = None
