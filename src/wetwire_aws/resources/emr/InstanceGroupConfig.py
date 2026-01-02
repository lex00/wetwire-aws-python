"""PropertyTypes for AWS::EMR::InstanceGroupConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoScalingPolicy(PropertyType):
    constraints: ScalingConstraints | None = None
    rules: list[ScalingRule] = field(default_factory=list)


@dataclass
class CloudWatchAlarmDefinition(PropertyType):
    comparison_operator: str | None = None
    metric_name: str | None = None
    period: int | None = None
    threshold: float | None = None
    dimensions: list[MetricDimension] = field(default_factory=list)
    evaluation_periods: int | None = None
    namespace: str | None = None
    statistic: str | None = None
    unit: str | None = None


@dataclass
class Configuration(PropertyType):
    classification: str | None = None
    configuration_properties: dict[str, String] = field(default_factory=dict)
    configurations: list[Configuration] = field(default_factory=list)


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    volume_specification: VolumeSpecification | None = None
    volumes_per_instance: int | None = None


@dataclass
class EbsConfiguration(PropertyType):
    ebs_block_device_configs: list[EbsBlockDeviceConfig] = field(default_factory=list)
    ebs_optimized: bool | None = None


@dataclass
class MetricDimension(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class ScalingAction(PropertyType):
    simple_scaling_policy_configuration: SimpleScalingPolicyConfiguration | None = None
    market: str | None = None


@dataclass
class ScalingConstraints(PropertyType):
    max_capacity: int | None = None
    min_capacity: int | None = None


@dataclass
class ScalingRule(PropertyType):
    action: ScalingAction | None = None
    name: str | None = None
    trigger: ScalingTrigger | None = None
    description: str | None = None


@dataclass
class ScalingTrigger(PropertyType):
    cloud_watch_alarm_definition: CloudWatchAlarmDefinition | None = None


@dataclass
class SimpleScalingPolicyConfiguration(PropertyType):
    scaling_adjustment: int | None = None
    adjustment_type: str | None = None
    cool_down: int | None = None


@dataclass
class VolumeSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gb": "SizeInGB",
    }

    size_in_gb: int | None = None
    volume_type: str | None = None
    iops: int | None = None
    throughput: int | None = None
