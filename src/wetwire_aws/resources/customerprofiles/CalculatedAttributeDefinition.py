"""PropertyTypes for AWS::CustomerProfiles::CalculatedAttributeDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeDetails(PropertyType):
    attributes: list[AttributeItem] = field(default_factory=list)
    expression: str | None = None


@dataclass
class AttributeItem(PropertyType):
    name: str | None = None


@dataclass
class Conditions(PropertyType):
    object_count: int | None = None
    range: Range | None = None
    threshold: Threshold | None = None


@dataclass
class Range(PropertyType):
    unit: str | None = None
    timestamp_format: str | None = None
    timestamp_source: str | None = None
    value: int | None = None
    value_range: ValueRange | None = None


@dataclass
class Readiness(PropertyType):
    message: str | None = None
    progress_percentage: int | None = None


@dataclass
class Threshold(PropertyType):
    operator: str | None = None
    value: str | None = None


@dataclass
class ValueRange(PropertyType):
    end: int | None = None
    start: int | None = None
