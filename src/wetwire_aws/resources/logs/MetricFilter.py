"""PropertyTypes for AWS::Logs::MetricFilter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Dimension(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class MetricTransformation(PropertyType):
    metric_name: str | None = None
    metric_namespace: str | None = None
    metric_value: str | None = None
    default_value: float | None = None
    dimensions: list[Dimension] = field(default_factory=list)
    unit: str | None = None
