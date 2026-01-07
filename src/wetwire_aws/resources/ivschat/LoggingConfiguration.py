"""PropertyTypes for AWS::IVSChat::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchLogsDestinationConfiguration(PropertyType):
    log_group_name: DslValue[str] | None = None


@dataclass
class DestinationConfiguration(PropertyType):
    cloud_watch_logs: DslValue[CloudWatchLogsDestinationConfiguration] | None = None
    firehose: DslValue[FirehoseDestinationConfiguration] | None = None
    s3: DslValue[S3DestinationConfiguration] | None = None


@dataclass
class FirehoseDestinationConfiguration(PropertyType):
    delivery_stream_name: DslValue[str] | None = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    bucket_name: DslValue[str] | None = None
