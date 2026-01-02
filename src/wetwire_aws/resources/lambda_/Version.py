"""PropertyTypes for AWS::Lambda::Version."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FunctionScalingConfig(PropertyType):
    max_execution_environments: int | None = None
    min_execution_environments: int | None = None


@dataclass
class ProvisionedConcurrencyConfiguration(PropertyType):
    provisioned_concurrent_executions: int | None = None


@dataclass
class RuntimePolicy(PropertyType):
    update_runtime_on: str | None = None
    runtime_version_arn: str | None = None
