"""PropertyTypes for AWS::AppIntegrations::DataIntegration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FileConfiguration(PropertyType):
    folders: list[DslValue[str]] = field(default_factory=list)
    filters: DslValue[dict[str, Any]] | None = None


@dataclass
class ScheduleConfig(PropertyType):
    schedule_expression: DslValue[str] | None = None
    first_execution_from: DslValue[str] | None = None
    object: DslValue[str] | None = None
