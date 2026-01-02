"""PropertyTypes for AWS::IVSChat::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchLogsDestinationConfiguration(PropertyType):
    log_group_name: str | None = None


@dataclass
class DestinationConfiguration(PropertyType):
    cloud_watch_logs: CloudWatchLogsDestinationConfiguration | None = None
    firehose: FirehoseDestinationConfiguration | None = None
    s3: S3DestinationConfiguration | None = None


@dataclass
class FirehoseDestinationConfiguration(PropertyType):
    delivery_stream_name: str | None = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    bucket_name: str | None = None
