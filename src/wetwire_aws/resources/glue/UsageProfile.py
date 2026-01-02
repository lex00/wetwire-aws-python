"""PropertyTypes for AWS::Glue::UsageProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConfigurationObject(PropertyType):
    allowed_values: list[String] = field(default_factory=list)
    default_value: str | None = None
    max_value: str | None = None
    min_value: str | None = None


@dataclass
class ProfileConfiguration(PropertyType):
    job_configuration: dict[str, ConfigurationObject] = field(default_factory=dict)
    session_configuration: dict[str, ConfigurationObject] = field(default_factory=dict)
