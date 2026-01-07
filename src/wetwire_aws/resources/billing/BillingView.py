"""PropertyTypes for AWS::Billing::BillingView."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataFilterExpression(PropertyType):
    dimensions: DslValue[Dimensions] | None = None
    tags: DslValue[Tags] | None = None
    time_range: DslValue[TimeRange] | None = None


@dataclass
class Dimensions(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Tags(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TimeRange(PropertyType):
    begin_date_inclusive: DslValue[str] | None = None
    end_date_inclusive: DslValue[str] | None = None
