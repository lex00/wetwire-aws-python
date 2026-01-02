"""PropertyTypes for AWS::CloudTrail::Trail."""

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
class AggregationConfiguration(PropertyType):
    event_category: str | None = None
    templates: list[String] = field(default_factory=list)


@dataclass
class DataResource(PropertyType):
    type_: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class EventSelector(PropertyType):
    data_resources: list[DataResource] = field(default_factory=list)
    exclude_management_event_sources: list[String] = field(default_factory=list)
    include_management_events: bool | None = None
    read_write_type: str | None = None


@dataclass
class InsightSelector(PropertyType):
    event_categories: list[String] = field(default_factory=list)
    insight_type: str | None = None
