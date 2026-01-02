"""PropertyTypes for AWS::ODB::CloudAutonomousVmCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MaintenanceWindow(PropertyType):
    days_of_week: list[String] = field(default_factory=list)
    hours_of_day: list[Integer] = field(default_factory=list)
    lead_time_in_weeks: int | None = None
    months: list[String] = field(default_factory=list)
    preference: str | None = None
    weeks_of_month: list[Integer] = field(default_factory=list)
