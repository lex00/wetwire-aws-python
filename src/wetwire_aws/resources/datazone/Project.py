"""PropertyTypes for AWS::DataZone::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class EnvironmentConfigurationUserParameter(PropertyType):
    environment_configuration_name: str | None = None
    environment_id: str | None = None
    environment_parameters: list[EnvironmentParameter] = field(default_factory=list)


@dataclass
class EnvironmentParameter(PropertyType):
    name: str | None = None
    value: str | None = None
