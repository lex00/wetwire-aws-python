"""PropertyTypes for AWS::CloudTrail::EventDataStore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdvancedEventSelector(PropertyType):
    field_selectors: list[DslValue[AdvancedFieldSelector]] = field(default_factory=list)
    name: DslValue[str] | None = None


@dataclass
class AdvancedFieldSelector(PropertyType):
    field_: DslValue[str] | None = None
    ends_with: list[DslValue[str]] = field(default_factory=list)
    equals: list[DslValue[str]] = field(default_factory=list)
    not_ends_with: list[DslValue[str]] = field(default_factory=list)
    not_equals: list[DslValue[str]] = field(default_factory=list)
    not_starts_with: list[DslValue[str]] = field(default_factory=list)
    starts_with: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ContextKeySelector(PropertyType):
    equals: list[DslValue[str]] = field(default_factory=list)
    type_: DslValue[str] | None = None


@dataclass
class InsightSelector(PropertyType):
    insight_type: DslValue[str] | None = None
