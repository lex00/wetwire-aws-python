"""PropertyTypes for AWS::CloudWatch::MetricStream."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MetricStreamFilter(PropertyType):
    namespace: str | None = None
    metric_names: list[String] = field(default_factory=list)


@dataclass
class MetricStreamStatisticsConfiguration(PropertyType):
    additional_statistics: list[String] = field(default_factory=list)
    include_metrics: list[MetricStreamStatisticsMetric] = field(default_factory=list)


@dataclass
class MetricStreamStatisticsMetric(PropertyType):
    metric_name: str | None = None
    namespace: str | None = None
