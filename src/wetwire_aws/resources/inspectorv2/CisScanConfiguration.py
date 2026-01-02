"""PropertyTypes for AWS::InspectorV2::CisScanConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CisTargets(PropertyType):
    account_ids: list[String] = field(default_factory=list)
    target_resource_tags: dict[str, Any] | None = None


@dataclass
class DailySchedule(PropertyType):
    start_time: Time | None = None


@dataclass
class MonthlySchedule(PropertyType):
    day: str | None = None
    start_time: Time | None = None


@dataclass
class Schedule(PropertyType):
    daily: DailySchedule | None = None
    monthly: MonthlySchedule | None = None
    one_time: dict[str, Any] | None = None
    weekly: WeeklySchedule | None = None


@dataclass
class Time(PropertyType):
    time_of_day: str | None = None
    time_zone: str | None = None


@dataclass
class WeeklySchedule(PropertyType):
    days: list[String] = field(default_factory=list)
    start_time: Time | None = None
