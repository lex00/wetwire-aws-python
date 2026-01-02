"""PropertyTypes for AWS::CloudWatch::AnomalyDetector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Configuration(PropertyType):
    excluded_time_ranges: list[Range] = field(default_factory=list)
    metric_time_zone: str | None = None


@dataclass
class Dimension(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class Metric(PropertyType):
    metric_name: str | None = None
    namespace: str | None = None
    dimensions: list[Dimension] = field(default_factory=list)


@dataclass
class MetricCharacteristics(PropertyType):
    periodic_spikes: bool | None = None


@dataclass
class MetricDataQueries(PropertyType):
    pass


@dataclass
class MetricDataQuery(PropertyType):
    id: str | None = None
    account_id: str | None = None
    expression: str | None = None
    label: str | None = None
    metric_stat: MetricStat | None = None
    period: int | None = None
    return_data: bool | None = None


@dataclass
class MetricMathAnomalyDetector(PropertyType):
    metric_data_queries: list[MetricDataQuery] = field(default_factory=list)


@dataclass
class MetricStat(PropertyType):
    metric: Metric | None = None
    period: int | None = None
    stat: str | None = None
    unit: str | None = None


@dataclass
class Range(PropertyType):
    end_time: str | None = None
    start_time: str | None = None


@dataclass
class SingleMetricAnomalyDetector(PropertyType):
    account_id: str | None = None
    dimensions: list[Dimension] = field(default_factory=list)
    metric_name: str | None = None
    namespace: str | None = None
    stat: str | None = None
