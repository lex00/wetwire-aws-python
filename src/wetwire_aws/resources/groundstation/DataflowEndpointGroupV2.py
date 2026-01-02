"""PropertyTypes for AWS::GroundStation::DataflowEndpointGroupV2."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConnectionDetails(PropertyType):
    socket_address: SocketAddress | None = None
    mtu: int | None = None


@dataclass
class CreateEndpointDetails(PropertyType):
    downlink_aws_ground_station_agent_endpoint: (
        DownlinkAwsGroundStationAgentEndpoint | None
    ) = None
    uplink_aws_ground_station_agent_endpoint: (
        UplinkAwsGroundStationAgentEndpoint | None
    ) = None


@dataclass
class DownlinkAwsGroundStationAgentEndpoint(PropertyType):
    dataflow_details: DownlinkDataflowDetails | None = None
    name: str | None = None


@dataclass
class DownlinkAwsGroundStationAgentEndpointDetails(PropertyType):
    dataflow_details: DownlinkDataflowDetails | None = None
    name: str | None = None
    agent_status: str | None = None
    audit_results: str | None = None


@dataclass
class DownlinkConnectionDetails(PropertyType):
    agent_ip_and_port_address: RangedConnectionDetails | None = None
    egress_address_and_port: ConnectionDetails | None = None


@dataclass
class DownlinkDataflowDetails(PropertyType):
    agent_connection_details: DownlinkConnectionDetails | None = None


@dataclass
class EndpointDetails(PropertyType):
    downlink_aws_ground_station_agent_endpoint: (
        DownlinkAwsGroundStationAgentEndpointDetails | None
    ) = None
    uplink_aws_ground_station_agent_endpoint: (
        UplinkAwsGroundStationAgentEndpointDetails | None
    ) = None


@dataclass
class IntegerRange(PropertyType):
    maximum: int | None = None
    minimum: int | None = None


@dataclass
class RangedConnectionDetails(PropertyType):
    socket_address: RangedSocketAddress | None = None
    mtu: int | None = None


@dataclass
class RangedSocketAddress(PropertyType):
    name: str | None = None
    port_range: IntegerRange | None = None


@dataclass
class SocketAddress(PropertyType):
    name: str | None = None
    port: int | None = None


@dataclass
class UplinkAwsGroundStationAgentEndpoint(PropertyType):
    dataflow_details: UplinkDataflowDetails | None = None
    name: str | None = None


@dataclass
class UplinkAwsGroundStationAgentEndpointDetails(PropertyType):
    dataflow_details: UplinkDataflowDetails | None = None
    name: str | None = None
    agent_status: str | None = None
    audit_results: str | None = None


@dataclass
class UplinkConnectionDetails(PropertyType):
    agent_ip_and_port_address: RangedConnectionDetails | None = None
    ingress_address_and_port: ConnectionDetails | None = None


@dataclass
class UplinkDataflowDetails(PropertyType):
    agent_connection_details: UplinkConnectionDetails | None = None
