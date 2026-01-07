"""PropertyTypes for AWS::QuickSight::RefreshSchedule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RefreshOnDay(PropertyType):
    day_of_month: DslValue[str] | None = None
    day_of_week: DslValue[str] | None = None


@dataclass
class RefreshScheduleMap(PropertyType):
    refresh_type: DslValue[str] | None = None
    schedule_frequency: DslValue[ScheduleFrequency] | None = None
    schedule_id: DslValue[str] | None = None
    start_after_date_time: DslValue[str] | None = None


@dataclass
class ScheduleFrequency(PropertyType):
    interval: DslValue[str] | None = None
    refresh_on_day: DslValue[RefreshOnDay] | None = None
    time_of_the_day: DslValue[str] | None = None
    time_zone: DslValue[str] | None = None
