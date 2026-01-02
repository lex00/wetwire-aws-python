"""PropertyTypes for AWS::CodeBuild::Fleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComputeConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "disk": "disk",
        "instance_type": "instanceType",
        "machine_type": "machineType",
        "memory": "memory",
        "v_cpu": "vCpu",
    }

    disk: int | None = None
    instance_type: str | None = None
    machine_type: str | None = None
    memory: int | None = None
    v_cpu: int | None = None


@dataclass
class FleetProxyRule(PropertyType):
    effect: str | None = None
    entities: list[String] = field(default_factory=list)
    type_: str | None = None


@dataclass
class ProxyConfiguration(PropertyType):
    default_behavior: str | None = None
    ordered_proxy_rules: list[FleetProxyRule] = field(default_factory=list)


@dataclass
class ScalingConfigurationInput(PropertyType):
    max_capacity: int | None = None
    scaling_type: str | None = None
    target_tracking_scaling_configs: list[TargetTrackingScalingConfiguration] = field(
        default_factory=list
    )


@dataclass
class TargetTrackingScalingConfiguration(PropertyType):
    metric_type: str | None = None
    target_value: float | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
    vpc_id: str | None = None
