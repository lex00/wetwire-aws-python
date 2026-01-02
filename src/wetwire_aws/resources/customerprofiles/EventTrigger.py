"""PropertyTypes for AWS::CustomerProfiles::EventTrigger."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EventTriggerCondition(PropertyType):
    event_trigger_dimensions: list[EventTriggerDimension] = field(default_factory=list)
    logical_operator: str | None = None


@dataclass
class EventTriggerDimension(PropertyType):
    object_attributes: list[ObjectAttribute] = field(default_factory=list)


@dataclass
class EventTriggerLimits(PropertyType):
    event_expiration: int | None = None
    periods: list[Period] = field(default_factory=list)


@dataclass
class ObjectAttribute(PropertyType):
    comparison_operator: str | None = None
    values: list[String] = field(default_factory=list)
    field_name: str | None = None
    source: str | None = None


@dataclass
class Period(PropertyType):
    unit: str | None = None
    value: int | None = None
    max_invocations_per_profile: int | None = None
    unlimited: bool | None = None
