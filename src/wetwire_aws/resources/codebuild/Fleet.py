"""PropertyTypes for AWS::CodeBuild::Fleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComputeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "disk": "disk",
        "instance_type": "instanceType",
        "machine_type": "machineType",
        "memory": "memory",
        "v_cpu": "vCpu",
    }

    disk: DslValue[int] | None = None
    instance_type: DslValue[str] | None = None
    machine_type: DslValue[str] | None = None
    memory: DslValue[int] | None = None
    v_cpu: DslValue[int] | None = None


@dataclass
class FleetProxyRule(PropertyType):
    effect: DslValue[str] | None = None
    entities: list[DslValue[str]] = field(default_factory=list)
    type_: DslValue[str] | None = None


@dataclass
class ProxyConfiguration(PropertyType):
    default_behavior: DslValue[str] | None = None
    ordered_proxy_rules: list[DslValue[FleetProxyRule]] = field(default_factory=list)


@dataclass
class ScalingConfigurationInput(PropertyType):
    max_capacity: DslValue[int] | None = None
    scaling_type: DslValue[str] | None = None
    target_tracking_scaling_configs: list[
        DslValue[TargetTrackingScalingConfiguration]
    ] = field(default_factory=list)


@dataclass
class TargetTrackingScalingConfiguration(PropertyType):
    metric_type: DslValue[str] | None = None
    target_value: DslValue[float] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
    vpc_id: DslValue[str] | None = None
