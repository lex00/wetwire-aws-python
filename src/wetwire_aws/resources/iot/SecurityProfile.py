"""PropertyTypes for AWS::IoT::SecurityProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AlertTarget(PropertyType):
    alert_target_arn: str | None = None
    role_arn: str | None = None


@dataclass
class Behavior(PropertyType):
    name: str | None = None
    criteria: BehaviorCriteria | None = None
    export_metric: bool | None = None
    metric: str | None = None
    metric_dimension: MetricDimension | None = None
    suppress_alerts: bool | None = None


@dataclass
class BehaviorCriteria(PropertyType):
    comparison_operator: str | None = None
    consecutive_datapoints_to_alarm: int | None = None
    consecutive_datapoints_to_clear: int | None = None
    duration_seconds: int | None = None
    ml_detection_config: MachineLearningDetectionConfig | None = None
    statistical_threshold: StatisticalThreshold | None = None
    value: MetricValue | None = None


@dataclass
class MachineLearningDetectionConfig(PropertyType):
    confidence_level: str | None = None


@dataclass
class MetricDimension(PropertyType):
    dimension_name: str | None = None
    operator: str | None = None


@dataclass
class MetricToRetain(PropertyType):
    metric: str | None = None
    export_metric: bool | None = None
    metric_dimension: MetricDimension | None = None


@dataclass
class MetricValue(PropertyType):
    cidrs: list[String] = field(default_factory=list)
    count: str | None = None
    number: float | None = None
    numbers: list[Double] = field(default_factory=list)
    ports: list[Integer] = field(default_factory=list)
    strings: list[String] = field(default_factory=list)


@dataclass
class MetricsExportConfig(PropertyType):
    mqtt_topic: str | None = None
    role_arn: str | None = None


@dataclass
class StatisticalThreshold(PropertyType):
    statistic: str | None = None
