"""PropertyTypes for AWS::ARCZonalShift::ZonalAutoshiftConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ControlCondition(PropertyType):
    alarm_identifier: str | None = None
    type_: str | None = None


@dataclass
class PracticeRunConfiguration(PropertyType):
    outcome_alarms: list[ControlCondition] = field(default_factory=list)
    blocked_dates: list[String] = field(default_factory=list)
    blocked_windows: list[String] = field(default_factory=list)
    blocking_alarms: list[ControlCondition] = field(default_factory=list)
