"""PropertyTypes for AWS::PinpointEmail::ConfigurationSetEventDestination."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchDestination(PropertyType):
    dimension_configurations: list[DimensionConfiguration] = field(default_factory=list)


@dataclass
class DimensionConfiguration(PropertyType):
    default_dimension_value: str | None = None
    dimension_name: str | None = None
    dimension_value_source: str | None = None


@dataclass
class EventDestination(PropertyType):
    matching_event_types: list[String] = field(default_factory=list)
    cloud_watch_destination: CloudWatchDestination | None = None
    enabled: bool | None = None
    kinesis_firehose_destination: KinesisFirehoseDestination | None = None
    pinpoint_destination: PinpointDestination | None = None
    sns_destination: SnsDestination | None = None


@dataclass
class KinesisFirehoseDestination(PropertyType):
    delivery_stream_arn: str | None = None
    iam_role_arn: str | None = None


@dataclass
class PinpointDestination(PropertyType):
    application_arn: str | None = None


@dataclass
class SnsDestination(PropertyType):
    topic_arn: str | None = None
