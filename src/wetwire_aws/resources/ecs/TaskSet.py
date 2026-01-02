"""PropertyTypes for AWS::ECS::TaskSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AwsVpcConfiguration(PropertyType):
    subnets: list[String] = field(default_factory=list)
    assign_public_ip: str | None = None
    security_groups: list[String] = field(default_factory=list)


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    base: int | None = None
    capacity_provider: str | None = None
    weight: int | None = None


@dataclass
class LoadBalancer(PropertyType):
    container_name: str | None = None
    container_port: int | None = None
    target_group_arn: str | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    aws_vpc_configuration: AwsVpcConfiguration | None = None


@dataclass
class Scale(PropertyType):
    unit: str | None = None
    value: float | None = None


@dataclass
class ServiceRegistry(PropertyType):
    container_name: str | None = None
    container_port: int | None = None
    port: int | None = None
    registry_arn: str | None = None
