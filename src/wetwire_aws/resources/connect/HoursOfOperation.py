"""PropertyTypes for AWS::Connect::HoursOfOperation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HoursOfOperationConfig(PropertyType):
    day: str | None = None
    end_time: HoursOfOperationTimeSlice | None = None
    start_time: HoursOfOperationTimeSlice | None = None


@dataclass
class HoursOfOperationOverride(PropertyType):
    effective_from: str | None = None
    effective_till: str | None = None
    override_config: list[HoursOfOperationOverrideConfig] = field(default_factory=list)
    override_name: str | None = None
    hours_of_operation_override_id: str | None = None
    override_description: str | None = None
    override_type: str | None = None
    recurrence_config: RecurrenceConfig | None = None


@dataclass
class HoursOfOperationOverrideConfig(PropertyType):
    day: str | None = None
    end_time: OverrideTimeSlice | None = None
    start_time: OverrideTimeSlice | None = None


@dataclass
class HoursOfOperationTimeSlice(PropertyType):
    hours: int | None = None
    minutes: int | None = None


@dataclass
class HoursOfOperationsIdentifier(PropertyType):
    id: str | None = None
    name: str | None = None


@dataclass
class OverrideTimeSlice(PropertyType):
    hours: int | None = None
    minutes: int | None = None


@dataclass
class RecurrenceConfig(PropertyType):
    recurrence_pattern: RecurrencePattern | None = None


@dataclass
class RecurrencePattern(PropertyType):
    by_month: list[Integer] = field(default_factory=list)
    by_month_day: list[Integer] = field(default_factory=list)
    by_weekday_occurrence: list[Integer] = field(default_factory=list)
    frequency: str | None = None
    interval: int | None = None
