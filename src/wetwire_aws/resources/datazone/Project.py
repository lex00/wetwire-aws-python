"""PropertyTypes for AWS::DataZone::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EnvironmentConfigurationUserParameter(PropertyType):
    environment_configuration_name: DslValue[str] | None = None
    environment_id: DslValue[str] | None = None
    environment_parameters: list[DslValue[EnvironmentParameter]] = field(
        default_factory=list
    )


@dataclass
class EnvironmentParameter(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None
