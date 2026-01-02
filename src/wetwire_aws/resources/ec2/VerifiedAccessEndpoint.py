"""PropertyTypes for AWS::EC2::VerifiedAccessEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CidrOptions(PropertyType):
    cidr: str | None = None
    port_ranges: list[PortRange] = field(default_factory=list)
    protocol: str | None = None
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class LoadBalancerOptions(PropertyType):
    load_balancer_arn: str | None = None
    port: int | None = None
    port_ranges: list[PortRange] = field(default_factory=list)
    protocol: str | None = None
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class NetworkInterfaceOptions(PropertyType):
    network_interface_id: str | None = None
    port: int | None = None
    port_ranges: list[PortRange] = field(default_factory=list)
    protocol: str | None = None


@dataclass
class PortRange(PropertyType):
    from_port: int | None = None
    to_port: int | None = None


@dataclass
class RdsOptions(PropertyType):
    port: int | None = None
    protocol: str | None = None
    rds_db_cluster_arn: str | None = None
    rds_db_instance_arn: str | None = None
    rds_db_proxy_arn: str | None = None
    rds_endpoint: str | None = None
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class SseSpecification(PropertyType):
    customer_managed_key_enabled: bool | None = None
    kms_key_arn: str | None = None
