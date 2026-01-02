"""PropertyTypes for AWS::CloudWatch::Alarm."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Dimension(PropertyType):
    name: str | None = None
    value: str | None = None


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
    label: str | None = None
    metric_stat: MetricStat | None = None
    period: int | None = None
    return_data: bool | None = None


@dataclass
class MetricStat(PropertyType):
    metric: Metric | None = None
    period: int | None = None
    stat: str | None = None
    unit: str | None = None
