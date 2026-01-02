"""PropertyTypes for AWS::QuickSight::RefreshSchedule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RefreshOnDay(PropertyType):
    day_of_month: str | None = None
    day_of_week: str | None = None


@dataclass
class RefreshScheduleMap(PropertyType):
    refresh_type: str | None = None
    schedule_frequency: ScheduleFrequency | None = None
    schedule_id: str | None = None
    start_after_date_time: str | None = None


@dataclass
class ScheduleFrequency(PropertyType):
    interval: str | None = None
    refresh_on_day: RefreshOnDay | None = None
    time_of_the_day: str | None = None
    time_zone: str | None = None
