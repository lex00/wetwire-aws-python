"""PropertyTypes for AWS::CloudTrail::Trail."""

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
class AggregationConfiguration(PropertyType):
    event_category: DslValue[str] | None = None
    templates: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DataResource(PropertyType):
    type_: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class EventSelector(PropertyType):
    data_resources: list[DslValue[DataResource]] = field(default_factory=list)
    exclude_management_event_sources: list[DslValue[str]] = field(default_factory=list)
    include_management_events: DslValue[bool] | None = None
    read_write_type: DslValue[str] | None = None


@dataclass
class InsightSelector(PropertyType):
    event_categories: list[DslValue[str]] = field(default_factory=list)
    insight_type: DslValue[str] | None = None
