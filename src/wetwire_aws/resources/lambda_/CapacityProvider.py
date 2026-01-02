"""PropertyTypes for AWS::Lambda::CapacityProvider."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapacityProviderPermissionsConfig(PropertyType):
    capacity_provider_operator_role_arn: str | None = None


@dataclass
class CapacityProviderScalingConfig(PropertyType):
    max_v_cpu_count: int | None = None
    scaling_mode: str | None = None
    scaling_policies: list[TargetTrackingScalingPolicy] = field(default_factory=list)


@dataclass
class CapacityProviderVpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class InstanceRequirements(PropertyType):
    allowed_instance_types: list[String] = field(default_factory=list)
    architectures: list[String] = field(default_factory=list)
    excluded_instance_types: list[String] = field(default_factory=list)


@dataclass
class TargetTrackingScalingPolicy(PropertyType):
    predefined_metric_type: str | None = None
    target_value: float | None = None
