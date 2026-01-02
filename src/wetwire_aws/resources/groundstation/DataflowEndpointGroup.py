"""PropertyTypes for AWS::GroundStation::DataflowEndpointGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AwsGroundStationAgentEndpoint(PropertyType):
    agent_status: str | None = None
    audit_results: str | None = None
    egress_address: ConnectionDetails | None = None
    ingress_address: RangedConnectionDetails | None = None
    name: str | None = None


@dataclass
class ConnectionDetails(PropertyType):
    mtu: int | None = None
    socket_address: SocketAddress | None = None


@dataclass
class DataflowEndpoint(PropertyType):
    address: SocketAddress | None = None
    mtu: int | None = None
    name: str | None = None


@dataclass
class EndpointDetails(PropertyType):
    aws_ground_station_agent_endpoint: AwsGroundStationAgentEndpoint | None = None
    endpoint: DataflowEndpoint | None = None
    security_details: SecurityDetails | None = None


@dataclass
class IntegerRange(PropertyType):
    maximum: int | None = None
    minimum: int | None = None


@dataclass
class RangedConnectionDetails(PropertyType):
    mtu: int | None = None
    socket_address: RangedSocketAddress | None = None


@dataclass
class RangedSocketAddress(PropertyType):
    name: str | None = None
    port_range: IntegerRange | None = None


@dataclass
class SecurityDetails(PropertyType):
    role_arn: str | None = None
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class SocketAddress(PropertyType):
    name: str | None = None
    port: int | None = None
