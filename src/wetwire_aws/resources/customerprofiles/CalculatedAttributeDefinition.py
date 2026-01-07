"""PropertyTypes for AWS::CustomerProfiles::CalculatedAttributeDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttributeDetails(PropertyType):
    attributes: list[DslValue[AttributeItem]] = field(default_factory=list)
    expression: DslValue[str] | None = None


@dataclass
class AttributeItem(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class Conditions(PropertyType):
    object_count: DslValue[int] | None = None
    range: DslValue[Range] | None = None
    threshold: DslValue[Threshold] | None = None


@dataclass
class Range(PropertyType):
    unit: DslValue[str] | None = None
    timestamp_format: DslValue[str] | None = None
    timestamp_source: DslValue[str] | None = None
    value: DslValue[int] | None = None
    value_range: DslValue[ValueRange] | None = None


@dataclass
class Readiness(PropertyType):
    message: DslValue[str] | None = None
    progress_percentage: DslValue[int] | None = None


@dataclass
class Threshold(PropertyType):
    operator: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ValueRange(PropertyType):
    end: DslValue[int] | None = None
    start: DslValue[int] | None = None
