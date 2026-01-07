"""PropertyTypes for AWS::Lambda::CapacityProvider."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapacityProviderPermissionsConfig(PropertyType):
    capacity_provider_operator_role_arn: DslValue[str] | None = None


@dataclass
class CapacityProviderScalingConfig(PropertyType):
    max_v_cpu_count: DslValue[int] | None = None
    scaling_mode: DslValue[str] | None = None
    scaling_policies: list[DslValue[TargetTrackingScalingPolicy]] = field(
        default_factory=list
    )


@dataclass
class CapacityProviderVpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class InstanceRequirements(PropertyType):
    allowed_instance_types: list[DslValue[str]] = field(default_factory=list)
    architectures: list[DslValue[str]] = field(default_factory=list)
    excluded_instance_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TargetTrackingScalingPolicy(PropertyType):
    predefined_metric_type: DslValue[str] | None = None
    target_value: DslValue[float] | None = None
