"""PropertyTypes for AWS::SMSVOICE::ConfigurationSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchLogsDestination(PropertyType):
    iam_role_arn: DslValue[str] | None = None
    log_group_arn: DslValue[str] | None = None


@dataclass
class EventDestination(PropertyType):
    enabled: DslValue[bool] | None = None
    event_destination_name: DslValue[str] | None = None
    matching_event_types: list[DslValue[str]] = field(default_factory=list)
    cloud_watch_logs_destination: DslValue[CloudWatchLogsDestination] | None = None
    kinesis_firehose_destination: DslValue[KinesisFirehoseDestination] | None = None
    sns_destination: DslValue[SnsDestination] | None = None


@dataclass
class KinesisFirehoseDestination(PropertyType):
    delivery_stream_arn: DslValue[str] | None = None
    iam_role_arn: DslValue[str] | None = None


@dataclass
class SnsDestination(PropertyType):
    topic_arn: DslValue[str] | None = None
