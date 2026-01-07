"""PropertyTypes for AWS::ARCZonalShift::ZonalAutoshiftConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ControlCondition(PropertyType):
    alarm_identifier: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class PracticeRunConfiguration(PropertyType):
    outcome_alarms: list[DslValue[ControlCondition]] = field(default_factory=list)
    blocked_dates: list[DslValue[str]] = field(default_factory=list)
    blocked_windows: list[DslValue[str]] = field(default_factory=list)
    blocking_alarms: list[DslValue[ControlCondition]] = field(default_factory=list)
