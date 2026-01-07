"""PropertyTypes for AWS::InspectorV2::CisScanConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CisTargets(PropertyType):
    account_ids: list[DslValue[str]] = field(default_factory=list)
    target_resource_tags: DslValue[dict[str, Any]] | None = None


@dataclass
class DailySchedule(PropertyType):
    start_time: DslValue[Time] | None = None


@dataclass
class MonthlySchedule(PropertyType):
    day: DslValue[str] | None = None
    start_time: DslValue[Time] | None = None


@dataclass
class Schedule(PropertyType):
    daily: DslValue[DailySchedule] | None = None
    monthly: DslValue[MonthlySchedule] | None = None
    one_time: DslValue[dict[str, Any]] | None = None
    weekly: DslValue[WeeklySchedule] | None = None


@dataclass
class Time(PropertyType):
    time_of_day: DslValue[str] | None = None
    time_zone: DslValue[str] | None = None


@dataclass
class WeeklySchedule(PropertyType):
    days: list[DslValue[str]] = field(default_factory=list)
    start_time: DslValue[Time] | None = None
