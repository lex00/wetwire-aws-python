"""PropertyTypes for AWS::Billing::BillingView."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataFilterExpression(PropertyType):
    dimensions: Dimensions | None = None
    tags: Tags | None = None
    time_range: TimeRange | None = None


@dataclass
class Dimensions(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class Tags(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class TimeRange(PropertyType):
    begin_date_inclusive: str | None = None
    end_date_inclusive: str | None = None
