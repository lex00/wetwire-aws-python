"""PropertyTypes for AWS::AppSync::FunctionConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AppSyncRuntime(PropertyType):
    name: str | None = None
    runtime_version: str | None = None


@dataclass
class LambdaConflictHandlerConfig(PropertyType):
    lambda_conflict_handler_arn: str | None = None


@dataclass
class SyncConfig(PropertyType):
    conflict_detection: str | None = None
    conflict_handler: str | None = None
    lambda_conflict_handler_config: LambdaConflictHandlerConfig | None = None
