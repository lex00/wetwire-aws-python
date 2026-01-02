"""PropertyTypes for AWS::CloudTrail::EventDataStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdvancedEventSelector(PropertyType):
    field_selectors: list[AdvancedFieldSelector] = field(default_factory=list)
    name: str | None = None


@dataclass
class AdvancedFieldSelector(PropertyType):
    field_: str | None = None
    ends_with: list[String] = field(default_factory=list)
    equals: list[String] = field(default_factory=list)
    not_ends_with: list[String] = field(default_factory=list)
    not_equals: list[String] = field(default_factory=list)
    not_starts_with: list[String] = field(default_factory=list)
    starts_with: list[String] = field(default_factory=list)


@dataclass
class ContextKeySelector(PropertyType):
    equals: list[String] = field(default_factory=list)
    type_: str | None = None


@dataclass
class InsightSelector(PropertyType):
    insight_type: str | None = None
