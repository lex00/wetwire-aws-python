"""PropertyTypes for AWS::RedshiftServerless::Workgroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfigParameter(PropertyType):
    parameter_key: DslValue[str] | None = None
    parameter_value: DslValue[str] | None = None


@dataclass
class Endpoint(PropertyType):
    address: DslValue[str] | None = None
    port: DslValue[int] | None = None
    vpc_endpoints: list[DslValue[VpcEndpoint]] = field(default_factory=list)


@dataclass
class NetworkInterface(PropertyType):
    availability_zone: DslValue[str] | None = None
    network_interface_id: DslValue[str] | None = None
    private_ip_address: DslValue[str] | None = None
    subnet_id: DslValue[str] | None = None


@dataclass
class PerformanceTarget(PropertyType):
    level: DslValue[int] | None = None
    status: DslValue[str] | None = None


@dataclass
class VpcEndpoint(PropertyType):
    network_interfaces: list[DslValue[NetworkInterface]] = field(default_factory=list)
    vpc_endpoint_id: DslValue[str] | None = None
    vpc_id: DslValue[str] | None = None


@dataclass
class Workgroup(PropertyType):
    base_capacity: DslValue[int] | None = None
    config_parameters: list[DslValue[ConfigParameter]] = field(default_factory=list)
    creation_date: DslValue[str] | None = None
    endpoint: DslValue[Endpoint] | None = None
    enhanced_vpc_routing: DslValue[bool] | None = None
    max_capacity: DslValue[int] | None = None
    namespace_name: DslValue[str] | None = None
    price_performance_target: DslValue[PerformanceTarget] | None = None
    publicly_accessible: DslValue[bool] | None = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    status: DslValue[str] | None = None
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
    track_name: DslValue[str] | None = None
    workgroup_arn: DslValue[str] | None = None
    workgroup_id: DslValue[str] | None = None
    workgroup_name: DslValue[str] | None = None
