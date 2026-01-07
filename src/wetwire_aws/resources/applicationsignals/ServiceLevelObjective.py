"""PropertyTypes for AWS::ApplicationSignals::ServiceLevelObjective."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BurnRateConfiguration(PropertyType):
    look_back_window_minutes: DslValue[int] | None = None


@dataclass
class CalendarInterval(PropertyType):
    duration: DslValue[int] | None = None
    duration_unit: DslValue[str] | None = None
    start_time: DslValue[int] | None = None


@dataclass
class DependencyConfig(PropertyType):
    dependency_key_attributes: dict[str, DslValue[str]] = field(default_factory=dict)
    dependency_operation_name: DslValue[str] | None = None


@dataclass
class Dimension(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ExclusionWindow(PropertyType):
    window: DslValue[Window] | None = None
    reason: DslValue[str] | None = None
    recurrence_rule: DslValue[RecurrenceRule] | None = None
    start_time: DslValue[str] | None = None


@dataclass
class Goal(PropertyType):
    attainment_goal: DslValue[float] | None = None
    interval: DslValue[Interval] | None = None
    warning_threshold: DslValue[float] | None = None


@dataclass
class Interval(PropertyType):
    calendar_interval: DslValue[CalendarInterval] | None = None
    rolling_interval: DslValue[RollingInterval] | None = None


@dataclass
class Metric(PropertyType):
    dimensions: list[DslValue[Dimension]] = field(default_factory=list)
    metric_name: DslValue[str] | None = None
    namespace: DslValue[str] | None = None


@dataclass
class MetricDataQuery(PropertyType):
    id: DslValue[str] | None = None
    account_id: DslValue[str] | None = None
    expression: DslValue[str] | None = None
    metric_stat: DslValue[MetricStat] | None = None
    return_data: DslValue[bool] | None = None


@dataclass
class MetricStat(PropertyType):
    metric: DslValue[Metric] | None = None
    period: DslValue[int] | None = None
    stat: DslValue[str] | None = None
    unit: DslValue[str] | None = None


@dataclass
class MonitoredRequestCountMetric(PropertyType):
    bad_count_metric: list[DslValue[MetricDataQuery]] = field(default_factory=list)
    good_count_metric: list[DslValue[MetricDataQuery]] = field(default_factory=list)


@dataclass
class RecurrenceRule(PropertyType):
    expression: DslValue[str] | None = None


@dataclass
class RequestBasedSli(PropertyType):
    request_based_sli_metric: DslValue[RequestBasedSliMetric] | None = None
    comparison_operator: DslValue[str] | None = None
    metric_threshold: DslValue[float] | None = None


@dataclass
class RequestBasedSliMetric(PropertyType):
    dependency_config: DslValue[DependencyConfig] | None = None
    key_attributes: dict[str, DslValue[str]] = field(default_factory=dict)
    metric_type: DslValue[str] | None = None
    monitored_request_count_metric: DslValue[MonitoredRequestCountMetric] | None = None
    operation_name: DslValue[str] | None = None
    total_request_count_metric: list[DslValue[MetricDataQuery]] = field(
        default_factory=list
    )


@dataclass
class RollingInterval(PropertyType):
    duration: DslValue[int] | None = None
    duration_unit: DslValue[str] | None = None


@dataclass
class Sli(PropertyType):
    comparison_operator: DslValue[str] | None = None
    metric_threshold: DslValue[float] | None = None
    sli_metric: DslValue[SliMetric] | None = None


@dataclass
class SliMetric(PropertyType):
    dependency_config: DslValue[DependencyConfig] | None = None
    key_attributes: dict[str, DslValue[str]] = field(default_factory=dict)
    metric_data_queries: list[DslValue[MetricDataQuery]] = field(default_factory=list)
    metric_type: DslValue[str] | None = None
    operation_name: DslValue[str] | None = None
    period_seconds: DslValue[int] | None = None
    statistic: DslValue[str] | None = None


@dataclass
class Window(PropertyType):
    duration: DslValue[int] | None = None
    duration_unit: DslValue[str] | None = None
