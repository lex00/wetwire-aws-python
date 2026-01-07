"""PropertyTypes for AWS::GroundStation::DataflowEndpointGroupV2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectionDetails(PropertyType):
    socket_address: DslValue[SocketAddress] | None = None
    mtu: DslValue[int] | None = None


@dataclass
class CreateEndpointDetails(PropertyType):
    downlink_aws_ground_station_agent_endpoint: (
        DslValue[DownlinkAwsGroundStationAgentEndpoint] | None
    ) = None
    uplink_aws_ground_station_agent_endpoint: (
        DslValue[UplinkAwsGroundStationAgentEndpoint] | None
    ) = None


@dataclass
class DownlinkAwsGroundStationAgentEndpoint(PropertyType):
    dataflow_details: DslValue[DownlinkDataflowDetails] | None = None
    name: DslValue[str] | None = None


@dataclass
class DownlinkAwsGroundStationAgentEndpointDetails(PropertyType):
    dataflow_details: DslValue[DownlinkDataflowDetails] | None = None
    name: DslValue[str] | None = None
    agent_status: DslValue[str] | None = None
    audit_results: DslValue[str] | None = None


@dataclass
class DownlinkConnectionDetails(PropertyType):
    agent_ip_and_port_address: DslValue[RangedConnectionDetails] | None = None
    egress_address_and_port: DslValue[ConnectionDetails] | None = None


@dataclass
class DownlinkDataflowDetails(PropertyType):
    agent_connection_details: DslValue[DownlinkConnectionDetails] | None = None


@dataclass
class EndpointDetails(PropertyType):
    downlink_aws_ground_station_agent_endpoint: (
        DslValue[DownlinkAwsGroundStationAgentEndpointDetails] | None
    ) = None
    uplink_aws_ground_station_agent_endpoint: (
        DslValue[UplinkAwsGroundStationAgentEndpointDetails] | None
    ) = None


@dataclass
class IntegerRange(PropertyType):
    maximum: DslValue[int] | None = None
    minimum: DslValue[int] | None = None


@dataclass
class RangedConnectionDetails(PropertyType):
    socket_address: DslValue[RangedSocketAddress] | None = None
    mtu: DslValue[int] | None = None


@dataclass
class RangedSocketAddress(PropertyType):
    name: DslValue[str] | None = None
    port_range: DslValue[IntegerRange] | None = None


@dataclass
class SocketAddress(PropertyType):
    name: DslValue[str] | None = None
    port: DslValue[int] | None = None


@dataclass
class UplinkAwsGroundStationAgentEndpoint(PropertyType):
    dataflow_details: DslValue[UplinkDataflowDetails] | None = None
    name: DslValue[str] | None = None


@dataclass
class UplinkAwsGroundStationAgentEndpointDetails(PropertyType):
    dataflow_details: DslValue[UplinkDataflowDetails] | None = None
    name: DslValue[str] | None = None
    agent_status: DslValue[str] | None = None
    audit_results: DslValue[str] | None = None


@dataclass
class UplinkConnectionDetails(PropertyType):
    agent_ip_and_port_address: DslValue[RangedConnectionDetails] | None = None
    ingress_address_and_port: DslValue[ConnectionDetails] | None = None


@dataclass
class UplinkDataflowDetails(PropertyType):
    agent_connection_details: DslValue[UplinkConnectionDetails] | None = None
