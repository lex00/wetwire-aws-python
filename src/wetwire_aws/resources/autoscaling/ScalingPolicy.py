"""PropertyTypes for AWS::AutoScaling::ScalingPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomizedMetricSpecification(PropertyType):
    dimensions: list[MetricDimension] = field(default_factory=list)
    metric_name: str | None = None
    metrics: list[TargetTrackingMetricDataQuery] = field(default_factory=list)
    namespace: str | None = None
    period: int | None = None
    statistic: str | None = None
    unit: str | None = None


@dataclass
class Metric(PropertyType):
    metric_name: str | None = None
    namespace: str | None = None
    dimensions: list[MetricDimension] = field(default_factory=list)


@dataclass
class MetricDataQuery(PropertyType):
    id: str | None = None
    expression: str | None = None
    label: str | None = None
    metric_stat: MetricStat | None = None
    return_data: bool | None = None


@dataclass
class MetricDimension(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class MetricStat(PropertyType):
    metric: Metric | None = None
    stat: str | None = None
    unit: str | None = None


@dataclass
class PredefinedMetricSpecification(PropertyType):
    predefined_metric_type: str | None = None
    resource_label: str | None = None


@dataclass
class PredictiveScalingConfiguration(PropertyType):
    metric_specifications: list[PredictiveScalingMetricSpecification] = field(
        default_factory=list
    )
    max_capacity_breach_behavior: str | None = None
    max_capacity_buffer: int | None = None
    mode: str | None = None
    scheduling_buffer_time: int | None = None


@dataclass
class PredictiveScalingCustomizedCapacityMetric(PropertyType):
    metric_data_queries: list[MetricDataQuery] = field(default_factory=list)


@dataclass
class PredictiveScalingCustomizedLoadMetric(PropertyType):
    metric_data_queries: list[MetricDataQuery] = field(default_factory=list)


@dataclass
class PredictiveScalingCustomizedScalingMetric(PropertyType):
    metric_data_queries: list[MetricDataQuery] = field(default_factory=list)


@dataclass
class PredictiveScalingMetricSpecification(PropertyType):
    target_value: float | None = None
    customized_capacity_metric_specification: (
        PredictiveScalingCustomizedCapacityMetric | None
    ) = None
    customized_load_metric_specification: (
        PredictiveScalingCustomizedLoadMetric | None
    ) = None
    customized_scaling_metric_specification: (
        PredictiveScalingCustomizedScalingMetric | None
    ) = None
    predefined_load_metric_specification: (
        PredictiveScalingPredefinedLoadMetric | None
    ) = None
    predefined_metric_pair_specification: (
        PredictiveScalingPredefinedMetricPair | None
    ) = None
    predefined_scaling_metric_specification: (
        PredictiveScalingPredefinedScalingMetric | None
    ) = None


@dataclass
class PredictiveScalingPredefinedLoadMetric(PropertyType):
    predefined_metric_type: str | None = None
    resource_label: str | None = None


@dataclass
class PredictiveScalingPredefinedMetricPair(PropertyType):
    predefined_metric_type: str | None = None
    resource_label: str | None = None


@dataclass
class PredictiveScalingPredefinedScalingMetric(PropertyType):
    predefined_metric_type: str | None = None
    resource_label: str | None = None


@dataclass
class StepAdjustment(PropertyType):
    scaling_adjustment: int | None = None
    metric_interval_lower_bound: float | None = None
    metric_interval_upper_bound: float | None = None


@dataclass
class TargetTrackingConfiguration(PropertyType):
    target_value: float | None = None
    customized_metric_specification: CustomizedMetricSpecification | None = None
    disable_scale_in: bool | None = None
    predefined_metric_specification: PredefinedMetricSpecification | None = None


@dataclass
class TargetTrackingMetricDataQuery(PropertyType):
    id: str | None = None
    expression: str | None = None
    label: str | None = None
    metric_stat: TargetTrackingMetricStat | None = None
    period: int | None = None
    return_data: bool | None = None


@dataclass
class TargetTrackingMetricStat(PropertyType):
    metric: Metric | None = None
    stat: str | None = None
    period: int | None = None
    unit: str | None = None
