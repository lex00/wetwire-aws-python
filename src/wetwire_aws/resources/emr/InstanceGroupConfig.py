"""PropertyTypes for AWS::EMR::InstanceGroupConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoScalingPolicy(PropertyType):
    constraints: DslValue[ScalingConstraints] | None = None
    rules: list[DslValue[ScalingRule]] = field(default_factory=list)


@dataclass
class CloudWatchAlarmDefinition(PropertyType):
    comparison_operator: DslValue[str] | None = None
    metric_name: DslValue[str] | None = None
    period: DslValue[int] | None = None
    threshold: DslValue[float] | None = None
    dimensions: list[DslValue[MetricDimension]] = field(default_factory=list)
    evaluation_periods: DslValue[int] | None = None
    namespace: DslValue[str] | None = None
    statistic: DslValue[str] | None = None
    unit: DslValue[str] | None = None


@dataclass
class Configuration(PropertyType):
    classification: DslValue[str] | None = None
    configuration_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    configurations: list[DslValue[Configuration]] = field(default_factory=list)


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    volume_specification: DslValue[VolumeSpecification] | None = None
    volumes_per_instance: DslValue[int] | None = None


@dataclass
class EbsConfiguration(PropertyType):
    ebs_block_device_configs: list[DslValue[EbsBlockDeviceConfig]] = field(
        default_factory=list
    )
    ebs_optimized: DslValue[bool] | None = None


@dataclass
class MetricDimension(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ScalingAction(PropertyType):
    simple_scaling_policy_configuration: (
        DslValue[SimpleScalingPolicyConfiguration] | None
    ) = None
    market: DslValue[str] | None = None


@dataclass
class ScalingConstraints(PropertyType):
    max_capacity: DslValue[int] | None = None
    min_capacity: DslValue[int] | None = None


@dataclass
class ScalingRule(PropertyType):
    action: DslValue[ScalingAction] | None = None
    name: DslValue[str] | None = None
    trigger: DslValue[ScalingTrigger] | None = None
    description: DslValue[str] | None = None


@dataclass
class ScalingTrigger(PropertyType):
    cloud_watch_alarm_definition: DslValue[CloudWatchAlarmDefinition] | None = None


@dataclass
class SimpleScalingPolicyConfiguration(PropertyType):
    scaling_adjustment: DslValue[int] | None = None
    adjustment_type: DslValue[str] | None = None
    cool_down: DslValue[int] | None = None


@dataclass
class VolumeSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gb": "SizeInGB",
    }

    size_in_gb: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None
    iops: DslValue[int] | None = None
    throughput: DslValue[int] | None = None
