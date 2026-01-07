"""PropertyTypes for AWS::CloudWatch::Alarm."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Dimension(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


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
    label: DslValue[str] | None = None
    metric_stat: DslValue[MetricStat] | None = None
    period: DslValue[int] | None = None
    return_data: DslValue[bool] | None = None


@dataclass
class MetricStat(PropertyType):
    metric: DslValue[Metric] | None = None
    period: DslValue[int] | None = None
    stat: DslValue[str] | None = None
    unit: DslValue[str] | None = None
