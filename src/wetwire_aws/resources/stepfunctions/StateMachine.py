"""PropertyTypes for AWS::StepFunctions::StateMachine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchLogsLogGroup(PropertyType):
    log_group_arn: str | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    type_: str | None = None
    kms_data_key_reuse_period_seconds: int | None = None
    kms_key_id: str | None = None


@dataclass
class LogDestination(PropertyType):
    cloud_watch_logs_log_group: CloudWatchLogsLogGroup | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    destinations: list[LogDestination] = field(default_factory=list)
    include_execution_data: bool | None = None
    level: str | None = None


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    key: str | None = None
    version: str | None = None


@dataclass
class TagsEntry(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class TracingConfiguration(PropertyType):
    enabled: bool | None = None
