"""PropertyTypes for AWS::Config::RemediationConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ExecutionControls(PropertyType):
    ssm_controls: DslValue[SsmControls] | None = None


@dataclass
class RemediationParameterValue(PropertyType):
    resource_value: DslValue[ResourceValue] | None = None
    static_value: DslValue[StaticValue] | None = None


@dataclass
class ResourceValue(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class SsmControls(PropertyType):
    concurrent_execution_rate_percentage: DslValue[int] | None = None
    error_percentage: DslValue[int] | None = None


@dataclass
class StaticValue(PropertyType):
    values: list[DslValue[str]] = field(default_factory=list)
