"""PropertyTypes for AWS::Glue::UsageProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConfigurationObject(PropertyType):
    allowed_values: list[DslValue[str]] = field(default_factory=list)
    default_value: DslValue[str] | None = None
    max_value: DslValue[str] | None = None
    min_value: DslValue[str] | None = None


@dataclass
class ProfileConfiguration(PropertyType):
    job_configuration: dict[str, DslValue[ConfigurationObject]] = field(
        default_factory=dict
    )
    session_configuration: dict[str, DslValue[ConfigurationObject]] = field(
        default_factory=dict
    )
