"""PropertyTypes for AWS::StepFunctions::StateMachine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchLogsLogGroup(PropertyType):
    log_group_arn: DslValue[str] | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    kms_data_key_reuse_period_seconds: DslValue[int] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class LogDestination(PropertyType):
    cloud_watch_logs_log_group: DslValue[CloudWatchLogsLogGroup] | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    destinations: list[DslValue[LogDestination]] = field(default_factory=list)
    include_execution_data: DslValue[bool] | None = None
    level: DslValue[str] | None = None


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class TagsEntry(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TracingConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
