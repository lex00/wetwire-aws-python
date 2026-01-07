"""PropertyTypes for AWS::CustomerProfiles::EventTrigger."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EventTriggerCondition(PropertyType):
    event_trigger_dimensions: list[DslValue[EventTriggerDimension]] = field(
        default_factory=list
    )
    logical_operator: DslValue[str] | None = None


@dataclass
class EventTriggerDimension(PropertyType):
    object_attributes: list[DslValue[ObjectAttribute]] = field(default_factory=list)


@dataclass
class EventTriggerLimits(PropertyType):
    event_expiration: DslValue[int] | None = None
    periods: list[DslValue[Period]] = field(default_factory=list)


@dataclass
class ObjectAttribute(PropertyType):
    comparison_operator: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)
    field_name: DslValue[str] | None = None
    source: DslValue[str] | None = None


@dataclass
class Period(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[int] | None = None
    max_invocations_per_profile: DslValue[int] | None = None
    unlimited: DslValue[bool] | None = None
