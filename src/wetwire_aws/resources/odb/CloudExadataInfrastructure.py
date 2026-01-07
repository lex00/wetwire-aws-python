"""PropertyTypes for AWS::ODB::CloudExadataInfrastructure."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomerContact(PropertyType):
    email: DslValue[str] | None = None


@dataclass
class MaintenanceWindow(PropertyType):
    custom_action_timeout_in_mins: DslValue[int] | None = None
    days_of_week: list[DslValue[str]] = field(default_factory=list)
    hours_of_day: list[DslValue[int]] = field(default_factory=list)
    is_custom_action_timeout_enabled: DslValue[bool] | None = None
    lead_time_in_weeks: DslValue[int] | None = None
    months: list[DslValue[str]] = field(default_factory=list)
    patching_mode: DslValue[str] | None = None
    preference: DslValue[str] | None = None
    weeks_of_month: list[DslValue[int]] = field(default_factory=list)
