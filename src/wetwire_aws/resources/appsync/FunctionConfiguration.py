"""PropertyTypes for AWS::AppSync::FunctionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AppSyncRuntime(PropertyType):
    name: DslValue[str] | None = None
    runtime_version: DslValue[str] | None = None


@dataclass
class LambdaConflictHandlerConfig(PropertyType):
    lambda_conflict_handler_arn: DslValue[str] | None = None


@dataclass
class SyncConfig(PropertyType):
    conflict_detection: DslValue[str] | None = None
    conflict_handler: DslValue[str] | None = None
    lambda_conflict_handler_config: DslValue[LambdaConflictHandlerConfig] | None = None
