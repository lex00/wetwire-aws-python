"""PropertyTypes for AWS::WorkSpacesThinClient::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MaintenanceWindow(PropertyType):
    type_: DslValue[str] | None = None
    apply_time_of: DslValue[str] | None = None
    days_of_the_week: list[DslValue[str]] = field(default_factory=list)
    end_time_hour: DslValue[int] | None = None
    end_time_minute: DslValue[int] | None = None
    start_time_hour: DslValue[int] | None = None
    start_time_minute: DslValue[int] | None = None
