"""PropertyTypes for AWS::Cognito::LogDeliveryConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchLogsConfiguration(PropertyType):
    log_group_arn: str | None = None


@dataclass
class FirehoseConfiguration(PropertyType):
    stream_arn: str | None = None


@dataclass
class LogConfiguration(PropertyType):
    cloud_watch_logs_configuration: CloudWatchLogsConfiguration | None = None
    event_source: str | None = None
    firehose_configuration: FirehoseConfiguration | None = None
    log_level: str | None = None
    s3_configuration: S3Configuration | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_arn: str | None = None
