"""PropertyTypes for AWS::Config::RemediationConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ExecutionControls(PropertyType):
    ssm_controls: SsmControls | None = None


@dataclass
class RemediationParameterValue(PropertyType):
    resource_value: ResourceValue | None = None
    static_value: StaticValue | None = None


@dataclass
class ResourceValue(PropertyType):
    value: str | None = None


@dataclass
class SsmControls(PropertyType):
    concurrent_execution_rate_percentage: int | None = None
    error_percentage: int | None = None


@dataclass
class StaticValue(PropertyType):
    values: list[String] = field(default_factory=list)
