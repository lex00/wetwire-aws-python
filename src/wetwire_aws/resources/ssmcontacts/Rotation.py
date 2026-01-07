"""PropertyTypes for AWS::SSMContacts::Rotation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CoverageTime(PropertyType):
    end_time: DslValue[str] | None = None
    start_time: DslValue[str] | None = None


@dataclass
class MonthlySetting(PropertyType):
    day_of_month: DslValue[int] | None = None
    hand_off_time: DslValue[str] | None = None


@dataclass
class RecurrenceSettings(PropertyType):
    number_of_on_calls: DslValue[int] | None = None
    recurrence_multiplier: DslValue[int] | None = None
    daily_settings: list[DslValue[str]] = field(default_factory=list)
    monthly_settings: list[DslValue[MonthlySetting]] = field(default_factory=list)
    shift_coverages: list[DslValue[ShiftCoverage]] = field(default_factory=list)
    weekly_settings: list[DslValue[WeeklySetting]] = field(default_factory=list)


@dataclass
class ShiftCoverage(PropertyType):
    coverage_times: list[DslValue[CoverageTime]] = field(default_factory=list)
    day_of_week: DslValue[str] | None = None


@dataclass
class WeeklySetting(PropertyType):
    day_of_week: DslValue[str] | None = None
    hand_off_time: DslValue[str] | None = None
