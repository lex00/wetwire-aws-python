"""PropertyTypes for AWS::ApplicationSignals::ServiceLevelObjective."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BurnRateConfiguration(PropertyType):
    look_back_window_minutes: int | None = None


@dataclass
class CalendarInterval(PropertyType):
    duration: int | None = None
    duration_unit: str | None = None
    start_time: int | None = None


@dataclass
class DependencyConfig(PropertyType):
    dependency_key_attributes: dict[str, String] = field(default_factory=dict)
    dependency_operation_name: str | None = None


@dataclass
class Dimension(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class ExclusionWindow(PropertyType):
    window: Window | None = None
    reason: str | None = None
    recurrence_rule: RecurrenceRule | None = None
    start_time: str | None = None


@dataclass
class Goal(PropertyType):
    attainment_goal: float | None = None
    interval: Interval | None = None
    warning_threshold: float | None = None


@dataclass
class Interval(PropertyType):
    calendar_interval: CalendarInterval | None = None
    rolling_interval: RollingInterval | None = None


@dataclass
class Metric(PropertyType):
    dimensions: list[Dimension] = field(default_factory=list)
    metric_name: str | None = None
    namespace: str | None = None


@dataclass
class MetricDataQuery(PropertyType):
    id: str | None = None
    account_id: str | None = None
    expression: str | None = None
    metric_stat: MetricStat | None = None
    return_data: bool | None = None


@dataclass
class MetricStat(PropertyType):
    metric: Metric | None = None
    period: int | None = None
    stat: str | None = None
    unit: str | None = None


@dataclass
class MonitoredRequestCountMetric(PropertyType):
    bad_count_metric: list[MetricDataQuery] = field(default_factory=list)
    good_count_metric: list[MetricDataQuery] = field(default_factory=list)


@dataclass
class RecurrenceRule(PropertyType):
    expression: str | None = None


@dataclass
class RequestBasedSli(PropertyType):
    request_based_sli_metric: RequestBasedSliMetric | None = None
    comparison_operator: str | None = None
    metric_threshold: float | None = None


@dataclass
class RequestBasedSliMetric(PropertyType):
    dependency_config: DependencyConfig | None = None
    key_attributes: dict[str, String] = field(default_factory=dict)
    metric_type: str | None = None
    monitored_request_count_metric: MonitoredRequestCountMetric | None = None
    operation_name: str | None = None
    total_request_count_metric: list[MetricDataQuery] = field(default_factory=list)


@dataclass
class RollingInterval(PropertyType):
    duration: int | None = None
    duration_unit: str | None = None


@dataclass
class Sli(PropertyType):
    comparison_operator: str | None = None
    metric_threshold: float | None = None
    sli_metric: SliMetric | None = None


@dataclass
class SliMetric(PropertyType):
    dependency_config: DependencyConfig | None = None
    key_attributes: dict[str, String] = field(default_factory=dict)
    metric_data_queries: list[MetricDataQuery] = field(default_factory=list)
    metric_type: str | None = None
    operation_name: str | None = None
    period_seconds: int | None = None
    statistic: str | None = None


@dataclass
class Window(PropertyType):
    duration: int | None = None
    duration_unit: str | None = None
