"""PropertyTypes for AWS::ODB::CloudAutonomousVmCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MaintenanceWindow(PropertyType):
    days_of_week: list[DslValue[str]] = field(default_factory=list)
    hours_of_day: list[DslValue[int]] = field(default_factory=list)
    lead_time_in_weeks: DslValue[int] | None = None
    months: list[DslValue[str]] = field(default_factory=list)
    preference: DslValue[str] | None = None
    weeks_of_month: list[DslValue[int]] = field(default_factory=list)
