"""PropertyTypes for AWS::SMSVOICE::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchLogsDestination(PropertyType):
    iam_role_arn: str | None = None
    log_group_arn: str | None = None


@dataclass
class EventDestination(PropertyType):
    enabled: bool | None = None
    event_destination_name: str | None = None
    matching_event_types: list[String] = field(default_factory=list)
    cloud_watch_logs_destination: CloudWatchLogsDestination | None = None
    kinesis_firehose_destination: KinesisFirehoseDestination | None = None
    sns_destination: SnsDestination | None = None


@dataclass
class KinesisFirehoseDestination(PropertyType):
    delivery_stream_arn: str | None = None
    iam_role_arn: str | None = None


@dataclass
class SnsDestination(PropertyType):
    topic_arn: str | None = None
