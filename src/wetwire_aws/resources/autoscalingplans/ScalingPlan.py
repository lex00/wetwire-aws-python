"""PropertyTypes for AWS::AutoScalingPlans::ScalingPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApplicationSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cloud_formation_stack_arn": "CloudFormationStackARN",
    }

    cloud_formation_stack_arn: str | None = None
    tag_filters: list[TagFilter] = field(default_factory=list)


@dataclass
class CustomizedLoadMetricSpecification(PropertyType):
    metric_name: str | None = None
    namespace: str | None = None
    statistic: str | None = None
    dimensions: list[MetricDimension] = field(default_factory=list)
    unit: str | None = None


@dataclass
class CustomizedScalingMetricSpecification(PropertyType):
    metric_name: str | None = None
    namespace: str | None = None
    statistic: str | None = None
    dimensions: list[MetricDimension] = field(default_factory=list)
    unit: str | None = None


@dataclass
class MetricDimension(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class PredefinedLoadMetricSpecification(PropertyType):
    predefined_load_metric_type: str | None = None
    resource_label: str | None = None


@dataclass
class PredefinedScalingMetricSpecification(PropertyType):
    predefined_scaling_metric_type: str | None = None
    resource_label: str | None = None


@dataclass
class ScalingInstruction(PropertyType):
    max_capacity: int | None = None
    min_capacity: int | None = None
    resource_id: str | None = None
    scalable_dimension: str | None = None
    service_namespace: str | None = None
    target_tracking_configurations: list[TargetTrackingConfiguration] = field(
        default_factory=list
    )
    customized_load_metric_specification: CustomizedLoadMetricSpecification | None = (
        None
    )
    disable_dynamic_scaling: bool | None = None
    predefined_load_metric_specification: PredefinedLoadMetricSpecification | None = (
        None
    )
    predictive_scaling_max_capacity_behavior: str | None = None
    predictive_scaling_max_capacity_buffer: int | None = None
    predictive_scaling_mode: str | None = None
    scaling_policy_update_behavior: str | None = None
    scheduled_action_buffer_time: int | None = None


@dataclass
class TagFilter(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class TargetTrackingConfiguration(PropertyType):
    target_value: float | None = None
    customized_scaling_metric_specification: (
        CustomizedScalingMetricSpecification | None
    ) = None
    disable_scale_in: bool | None = None
    estimated_instance_warmup: int | None = None
    predefined_scaling_metric_specification: (
        PredefinedScalingMetricSpecification | None
    ) = None
    scale_in_cooldown: int | None = None
    scale_out_cooldown: int | None = None
