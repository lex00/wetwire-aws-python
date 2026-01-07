"""PropertyTypes for AWS::ECS::TaskSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AwsVpcConfiguration(PropertyType):
    subnets: list[DslValue[str]] = field(default_factory=list)
    assign_public_ip: DslValue[str] | None = None
    security_groups: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    base: DslValue[int] | None = None
    capacity_provider: DslValue[str] | None = None
    weight: DslValue[int] | None = None


@dataclass
class LoadBalancer(PropertyType):
    container_name: DslValue[str] | None = None
    container_port: DslValue[int] | None = None
    target_group_arn: DslValue[str] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    aws_vpc_configuration: DslValue[AwsVpcConfiguration] | None = None


@dataclass
class Scale(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class ServiceRegistry(PropertyType):
    container_name: DslValue[str] | None = None
    container_port: DslValue[int] | None = None
    port: DslValue[int] | None = None
    registry_arn: DslValue[str] | None = None
