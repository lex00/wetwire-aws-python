"""PropertyTypes for AWS::RedshiftServerless::Workgroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfigParameter(PropertyType):
    parameter_key: str | None = None
    parameter_value: str | None = None


@dataclass
class Endpoint(PropertyType):
    address: str | None = None
    port: int | None = None
    vpc_endpoints: list[VpcEndpoint] = field(default_factory=list)


@dataclass
class NetworkInterface(PropertyType):
    availability_zone: str | None = None
    network_interface_id: str | None = None
    private_ip_address: str | None = None
    subnet_id: str | None = None


@dataclass
class PerformanceTarget(PropertyType):
    level: int | None = None
    status: str | None = None


@dataclass
class VpcEndpoint(PropertyType):
    network_interfaces: list[NetworkInterface] = field(default_factory=list)
    vpc_endpoint_id: str | None = None
    vpc_id: str | None = None


@dataclass
class Workgroup(PropertyType):
    base_capacity: int | None = None
    config_parameters: list[ConfigParameter] = field(default_factory=list)
    creation_date: str | None = None
    endpoint: Endpoint | None = None
    enhanced_vpc_routing: bool | None = None
    max_capacity: int | None = None
    namespace_name: str | None = None
    price_performance_target: PerformanceTarget | None = None
    publicly_accessible: bool | None = None
    security_group_ids: list[String] = field(default_factory=list)
    status: str | None = None
    subnet_ids: list[String] = field(default_factory=list)
    track_name: str | None = None
    workgroup_arn: str | None = None
    workgroup_id: str | None = None
    workgroup_name: str | None = None
