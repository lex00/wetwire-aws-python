"""PropertyTypes for AWS::CloudWatch::MetricStream."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MetricStreamFilter(PropertyType):
    namespace: DslValue[str] | None = None
    metric_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class MetricStreamStatisticsConfiguration(PropertyType):
    additional_statistics: list[DslValue[str]] = field(default_factory=list)
    include_metrics: list[DslValue[MetricStreamStatisticsMetric]] = field(
        default_factory=list
    )


@dataclass
class MetricStreamStatisticsMetric(PropertyType):
    metric_name: DslValue[str] | None = None
    namespace: DslValue[str] | None = None
