"""PropertyTypes for AWS::Logs::MetricFilter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Dimension(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class MetricTransformation(PropertyType):
    metric_name: DslValue[str] | None = None
    metric_namespace: DslValue[str] | None = None
    metric_value: DslValue[str] | None = None
    default_value: DslValue[float] | None = None
    dimensions: list[DslValue[Dimension]] = field(default_factory=list)
    unit: DslValue[str] | None = None
