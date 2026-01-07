"""PropertyTypes for AWS::Cognito::LogDeliveryConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchLogsConfiguration(PropertyType):
    log_group_arn: DslValue[str] | None = None


@dataclass
class FirehoseConfiguration(PropertyType):
    stream_arn: DslValue[str] | None = None


@dataclass
class LogConfiguration(PropertyType):
    cloud_watch_logs_configuration: DslValue[CloudWatchLogsConfiguration] | None = None
    event_source: DslValue[str] | None = None
    firehose_configuration: DslValue[FirehoseConfiguration] | None = None
    log_level: DslValue[str] | None = None
    s3_configuration: DslValue[S3Configuration] | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_arn: DslValue[str] | None = None
