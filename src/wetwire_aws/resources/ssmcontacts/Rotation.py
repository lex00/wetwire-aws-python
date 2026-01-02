"""PropertyTypes for AWS::SSMContacts::Rotation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CoverageTime(PropertyType):
    end_time: str | None = None
    start_time: str | None = None


@dataclass
class MonthlySetting(PropertyType):
    day_of_month: int | None = None
    hand_off_time: str | None = None


@dataclass
class RecurrenceSettings(PropertyType):
    number_of_on_calls: int | None = None
    recurrence_multiplier: int | None = None
    daily_settings: list[String] = field(default_factory=list)
    monthly_settings: list[MonthlySetting] = field(default_factory=list)
    shift_coverages: list[ShiftCoverage] = field(default_factory=list)
    weekly_settings: list[WeeklySetting] = field(default_factory=list)


@dataclass
class ShiftCoverage(PropertyType):
    coverage_times: list[CoverageTime] = field(default_factory=list)
    day_of_week: str | None = None


@dataclass
class WeeklySetting(PropertyType):
    day_of_week: str | None = None
    hand_off_time: str | None = None
