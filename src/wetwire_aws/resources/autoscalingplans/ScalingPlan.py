"""PropertyTypes for AWS::AutoScalingPlans::ScalingPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApplicationSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_formation_stack_arn": "CloudFormationStackARN",
    }

    cloud_formation_stack_arn: DslValue[str] | None = None
    tag_filters: list[DslValue[TagFilter]] = field(default_factory=list)


@dataclass
class CustomizedLoadMetricSpecification(PropertyType):
    metric_name: DslValue[str] | None = None
    namespace: DslValue[str] | None = None
    statistic: DslValue[str] | None = None
    dimensions: list[DslValue[MetricDimension]] = field(default_factory=list)
    unit: DslValue[str] | None = None


@dataclass
class CustomizedScalingMetricSpecification(PropertyType):
    metric_name: DslValue[str] | None = None
    namespace: DslValue[str] | None = None
    statistic: DslValue[str] | None = None
    dimensions: list[DslValue[MetricDimension]] = field(default_factory=list)
    unit: DslValue[str] | None = None


@dataclass
class MetricDimension(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class PredefinedLoadMetricSpecification(PropertyType):
    predefined_load_metric_type: DslValue[str] | None = None
    resource_label: DslValue[str] | None = None


@dataclass
class PredefinedScalingMetricSpecification(PropertyType):
    predefined_scaling_metric_type: DslValue[str] | None = None
    resource_label: DslValue[str] | None = None


@dataclass
class ScalingInstruction(PropertyType):
    max_capacity: DslValue[int] | None = None
    min_capacity: DslValue[int] | None = None
    resource_id: DslValue[str] | None = None
    scalable_dimension: DslValue[str] | None = None
    service_namespace: DslValue[str] | None = None
    target_tracking_configurations: list[DslValue[TargetTrackingConfiguration]] = field(
        default_factory=list
    )
    customized_load_metric_specification: (
        DslValue[CustomizedLoadMetricSpecification] | None
    ) = None
    disable_dynamic_scaling: DslValue[bool] | None = None
    predefined_load_metric_specification: (
        DslValue[PredefinedLoadMetricSpecification] | None
    ) = None
    predictive_scaling_max_capacity_behavior: DslValue[str] | None = None
    predictive_scaling_max_capacity_buffer: DslValue[int] | None = None
    predictive_scaling_mode: DslValue[str] | None = None
    scaling_policy_update_behavior: DslValue[str] | None = None
    scheduled_action_buffer_time: DslValue[int] | None = None


@dataclass
class TagFilter(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TargetTrackingConfiguration(PropertyType):
    target_value: DslValue[float] | None = None
    customized_scaling_metric_specification: (
        DslValue[CustomizedScalingMetricSpecification] | None
    ) = None
    disable_scale_in: DslValue[bool] | None = None
    estimated_instance_warmup: DslValue[int] | None = None
    predefined_scaling_metric_specification: (
        DslValue[PredefinedScalingMetricSpecification] | None
    ) = None
    scale_in_cooldown: DslValue[int] | None = None
    scale_out_cooldown: DslValue[int] | None = None
