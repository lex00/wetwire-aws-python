"""PropertyTypes for AWS::AppIntegrations::DataIntegration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FileConfiguration(PropertyType):
    folders: list[String] = field(default_factory=list)
    filters: dict[str, Any] | None = None


@dataclass
class ScheduleConfig(PropertyType):
    schedule_expression: str | None = None
    first_execution_from: str | None = None
    object: str | None = None
