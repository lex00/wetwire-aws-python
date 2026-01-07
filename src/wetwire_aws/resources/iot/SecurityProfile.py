"""PropertyTypes for AWS::IoT::SecurityProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AlertTarget(PropertyType):
    alert_target_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class Behavior(PropertyType):
    name: DslValue[str] | None = None
    criteria: DslValue[BehaviorCriteria] | None = None
    export_metric: DslValue[bool] | None = None
    metric: DslValue[str] | None = None
    metric_dimension: DslValue[MetricDimension] | None = None
    suppress_alerts: DslValue[bool] | None = None


@dataclass
class BehaviorCriteria(PropertyType):
    comparison_operator: DslValue[str] | None = None
    consecutive_datapoints_to_alarm: DslValue[int] | None = None
    consecutive_datapoints_to_clear: DslValue[int] | None = None
    duration_seconds: DslValue[int] | None = None
    ml_detection_config: DslValue[MachineLearningDetectionConfig] | None = None
    statistical_threshold: DslValue[StatisticalThreshold] | None = None
    value: DslValue[MetricValue] | None = None


@dataclass
class MachineLearningDetectionConfig(PropertyType):
    confidence_level: DslValue[str] | None = None


@dataclass
class MetricDimension(PropertyType):
    dimension_name: DslValue[str] | None = None
    operator: DslValue[str] | None = None


@dataclass
class MetricToRetain(PropertyType):
    metric: DslValue[str] | None = None
    export_metric: DslValue[bool] | None = None
    metric_dimension: DslValue[MetricDimension] | None = None


@dataclass
class MetricValue(PropertyType):
    cidrs: list[DslValue[str]] = field(default_factory=list)
    count: DslValue[str] | None = None
    number: DslValue[float] | None = None
    numbers: list[DslValue[float]] = field(default_factory=list)
    ports: list[DslValue[int]] = field(default_factory=list)
    strings: list[DslValue[str]] = field(default_factory=list)


@dataclass
class MetricsExportConfig(PropertyType):
    mqtt_topic: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class StatisticalThreshold(PropertyType):
    statistic: DslValue[str] | None = None
