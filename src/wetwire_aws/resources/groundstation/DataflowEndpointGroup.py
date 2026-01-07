"""PropertyTypes for AWS::GroundStation::DataflowEndpointGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AwsGroundStationAgentEndpoint(PropertyType):
    agent_status: DslValue[str] | None = None
    audit_results: DslValue[str] | None = None
    egress_address: DslValue[ConnectionDetails] | None = None
    ingress_address: DslValue[RangedConnectionDetails] | None = None
    name: DslValue[str] | None = None


@dataclass
class ConnectionDetails(PropertyType):
    mtu: DslValue[int] | None = None
    socket_address: DslValue[SocketAddress] | None = None


@dataclass
class DataflowEndpoint(PropertyType):
    address: DslValue[SocketAddress] | None = None
    mtu: DslValue[int] | None = None
    name: DslValue[str] | None = None


@dataclass
class EndpointDetails(PropertyType):
    aws_ground_station_agent_endpoint: (
        DslValue[AwsGroundStationAgentEndpoint] | None
    ) = None
    endpoint: DslValue[DataflowEndpoint] | None = None
    security_details: DslValue[SecurityDetails] | None = None


@dataclass
class IntegerRange(PropertyType):
    maximum: DslValue[int] | None = None
    minimum: DslValue[int] | None = None


@dataclass
class RangedConnectionDetails(PropertyType):
    mtu: DslValue[int] | None = None
    socket_address: DslValue[RangedSocketAddress] | None = None


@dataclass
class RangedSocketAddress(PropertyType):
    name: DslValue[str] | None = None
    port_range: DslValue[IntegerRange] | None = None


@dataclass
class SecurityDetails(PropertyType):
    role_arn: DslValue[str] | None = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SocketAddress(PropertyType):
    name: DslValue[str] | None = None
    port: DslValue[int] | None = None
