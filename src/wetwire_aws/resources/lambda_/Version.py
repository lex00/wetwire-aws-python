"""PropertyTypes for AWS::Lambda::Version."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FunctionScalingConfig(PropertyType):
    max_execution_environments: DslValue[int] | None = None
    min_execution_environments: DslValue[int] | None = None


@dataclass
class ProvisionedConcurrencyConfiguration(PropertyType):
    provisioned_concurrent_executions: DslValue[int] | None = None


@dataclass
class RuntimePolicy(PropertyType):
    update_runtime_on: DslValue[str] | None = None
    runtime_version_arn: DslValue[str] | None = None
