"""PropertyTypes for AWS::ODB::CloudExadataInfrastructure."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomerContact(PropertyType):
    email: str | None = None


@dataclass
class MaintenanceWindow(PropertyType):
    custom_action_timeout_in_mins: int | None = None
    days_of_week: list[String] = field(default_factory=list)
    hours_of_day: list[Integer] = field(default_factory=list)
    is_custom_action_timeout_enabled: bool | None = None
    lead_time_in_weeks: int | None = None
    months: list[String] = field(default_factory=list)
    patching_mode: str | None = None
    preference: str | None = None
    weeks_of_month: list[Integer] = field(default_factory=list)
