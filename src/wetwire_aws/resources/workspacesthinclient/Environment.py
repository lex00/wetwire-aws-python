"""PropertyTypes for AWS::WorkSpacesThinClient::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MaintenanceWindow(PropertyType):
    type_: str | None = None
    apply_time_of: str | None = None
    days_of_the_week: list[String] = field(default_factory=list)
    end_time_hour: int | None = None
    end_time_minute: int | None = None
    start_time_hour: int | None = None
    start_time_minute: int | None = None
