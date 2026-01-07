"""PropertyTypes for AWS::AutoScaling::ScalingPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomizedMetricSpecification(PropertyType):
    dimensions: list[DslValue[MetricDimension]] = field(default_factory=list)
    metric_name: DslValue[str] | None = None
    metrics: list[DslValue[TargetTrackingMetricDataQuery]] = field(default_factory=list)
    namespace: DslValue[str] | None = None
    period: DslValue[int] | None = None
    statistic: DslValue[str] | None = None
    unit: DslValue[str] | None = None


@dataclass
class Metric(PropertyType):
    metric_name: DslValue[str] | None = None
    namespace: DslValue[str] | None = None
    dimensions: list[DslValue[MetricDimension]] = field(default_factory=list)


@dataclass
class MetricDataQuery(PropertyType):
    id: DslValue[str] | None = None
    expression: DslValue[str] | None = None
    label: DslValue[str] | None = None
    metric_stat: DslValue[MetricStat] | None = None
    return_data: DslValue[bool] | None = None


@dataclass
class MetricDimension(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class MetricStat(PropertyType):
    metric: DslValue[Metric] | None = None
    stat: DslValue[str] | None = None
    unit: DslValue[str] | None = None


@dataclass
class PredefinedMetricSpecification(PropertyType):
    predefined_metric_type: DslValue[str] | None = None
    resource_label: DslValue[str] | None = None


@dataclass
class PredictiveScalingConfiguration(PropertyType):
    metric_specifications: list[DslValue[PredictiveScalingMetricSpecification]] = field(
        default_factory=list
    )
    max_capacity_breach_behavior: DslValue[str] | None = None
    max_capacity_buffer: DslValue[int] | None = None
    mode: DslValue[str] | None = None
    scheduling_buffer_time: DslValue[int] | None = None


@dataclass
class PredictiveScalingCustomizedCapacityMetric(PropertyType):
    metric_data_queries: list[DslValue[MetricDataQuery]] = field(default_factory=list)


@dataclass
class PredictiveScalingCustomizedLoadMetric(PropertyType):
    metric_data_queries: list[DslValue[MetricDataQuery]] = field(default_factory=list)


@dataclass
class PredictiveScalingCustomizedScalingMetric(PropertyType):
    metric_data_queries: list[DslValue[MetricDataQuery]] = field(default_factory=list)


@dataclass
class PredictiveScalingMetricSpecification(PropertyType):
    target_value: DslValue[float] | None = None
    customized_capacity_metric_specification: (
        DslValue[PredictiveScalingCustomizedCapacityMetric] | None
    ) = None
    customized_load_metric_specification: (
        DslValue[PredictiveScalingCustomizedLoadMetric] | None
    ) = None
    customized_scaling_metric_specification: (
        DslValue[PredictiveScalingCustomizedScalingMetric] | None
    ) = None
    predefined_load_metric_specification: (
        DslValue[PredictiveScalingPredefinedLoadMetric] | None
    ) = None
    predefined_metric_pair_specification: (
        DslValue[PredictiveScalingPredefinedMetricPair] | None
    ) = None
    predefined_scaling_metric_specification: (
        DslValue[PredictiveScalingPredefinedScalingMetric] | None
    ) = None


@dataclass
class PredictiveScalingPredefinedLoadMetric(PropertyType):
    predefined_metric_type: DslValue[str] | None = None
    resource_label: DslValue[str] | None = None


@dataclass
class PredictiveScalingPredefinedMetricPair(PropertyType):
    predefined_metric_type: DslValue[str] | None = None
    resource_label: DslValue[str] | None = None


@dataclass
class PredictiveScalingPredefinedScalingMetric(PropertyType):
    predefined_metric_type: DslValue[str] | None = None
    resource_label: DslValue[str] | None = None


@dataclass
class StepAdjustment(PropertyType):
    scaling_adjustment: DslValue[int] | None = None
    metric_interval_lower_bound: DslValue[float] | None = None
    metric_interval_upper_bound: DslValue[float] | None = None


@dataclass
class TargetTrackingConfiguration(PropertyType):
    target_value: DslValue[float] | None = None
    customized_metric_specification: DslValue[CustomizedMetricSpecification] | None = (
        None
    )
    disable_scale_in: DslValue[bool] | None = None
    predefined_metric_specification: DslValue[PredefinedMetricSpecification] | None = (
        None
    )


@dataclass
class TargetTrackingMetricDataQuery(PropertyType):
    id: DslValue[str] | None = None
    expression: DslValue[str] | None = None
    label: DslValue[str] | None = None
    metric_stat: DslValue[TargetTrackingMetricStat] | None = None
    period: DslValue[int] | None = None
    return_data: DslValue[bool] | None = None


@dataclass
class TargetTrackingMetricStat(PropertyType):
    metric: DslValue[Metric] | None = None
    stat: DslValue[str] | None = None
    period: DslValue[int] | None = None
    unit: DslValue[str] | None = None
