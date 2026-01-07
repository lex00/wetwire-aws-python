"""PropertyTypes for AWS::Connect::HoursOfOperation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class HoursOfOperationConfig(PropertyType):
    day: DslValue[str] | None = None
    end_time: DslValue[HoursOfOperationTimeSlice] | None = None
    start_time: DslValue[HoursOfOperationTimeSlice] | None = None


@dataclass
class HoursOfOperationOverride(PropertyType):
    effective_from: DslValue[str] | None = None
    effective_till: DslValue[str] | None = None
    override_config: list[DslValue[HoursOfOperationOverrideConfig]] = field(
        default_factory=list
    )
    override_name: DslValue[str] | None = None
    hours_of_operation_override_id: DslValue[str] | None = None
    override_description: DslValue[str] | None = None
    override_type: DslValue[str] | None = None
    recurrence_config: DslValue[RecurrenceConfig] | None = None


@dataclass
class HoursOfOperationOverrideConfig(PropertyType):
    day: DslValue[str] | None = None
    end_time: DslValue[OverrideTimeSlice] | None = None
    start_time: DslValue[OverrideTimeSlice] | None = None


@dataclass
class HoursOfOperationTimeSlice(PropertyType):
    hours: DslValue[int] | None = None
    minutes: DslValue[int] | None = None


@dataclass
class HoursOfOperationsIdentifier(PropertyType):
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class OverrideTimeSlice(PropertyType):
    hours: DslValue[int] | None = None
    minutes: DslValue[int] | None = None


@dataclass
class RecurrenceConfig(PropertyType):
    recurrence_pattern: DslValue[RecurrencePattern] | None = None


@dataclass
class RecurrencePattern(PropertyType):
    by_month: list[DslValue[int]] = field(default_factory=list)
    by_month_day: list[DslValue[int]] = field(default_factory=list)
    by_weekday_occurrence: list[DslValue[int]] = field(default_factory=list)
    frequency: DslValue[str] | None = None
    interval: DslValue[int] | None = None
