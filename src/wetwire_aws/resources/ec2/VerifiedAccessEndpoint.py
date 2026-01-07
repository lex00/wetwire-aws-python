"""PropertyTypes for AWS::EC2::VerifiedAccessEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CidrOptions(PropertyType):
    cidr: DslValue[str] | None = None
    port_ranges: list[DslValue[PortRange]] = field(default_factory=list)
    protocol: DslValue[str] | None = None
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LoadBalancerOptions(PropertyType):
    load_balancer_arn: DslValue[str] | None = None
    port: DslValue[int] | None = None
    port_ranges: list[DslValue[PortRange]] = field(default_factory=list)
    protocol: DslValue[str] | None = None
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class NetworkInterfaceOptions(PropertyType):
    network_interface_id: DslValue[str] | None = None
    port: DslValue[int] | None = None
    port_ranges: list[DslValue[PortRange]] = field(default_factory=list)
    protocol: DslValue[str] | None = None


@dataclass
class PortRange(PropertyType):
    from_port: DslValue[int] | None = None
    to_port: DslValue[int] | None = None


@dataclass
class RdsOptions(PropertyType):
    port: DslValue[int] | None = None
    protocol: DslValue[str] | None = None
    rds_db_cluster_arn: DslValue[str] | None = None
    rds_db_instance_arn: DslValue[str] | None = None
    rds_db_proxy_arn: DslValue[str] | None = None
    rds_endpoint: DslValue[str] | None = None
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SseSpecification(PropertyType):
    customer_managed_key_enabled: DslValue[bool] | None = None
    kms_key_arn: DslValue[str] | None = None
