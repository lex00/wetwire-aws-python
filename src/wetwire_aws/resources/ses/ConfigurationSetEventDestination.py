"""PropertyTypes for AWS::SES::ConfigurationSetEventDestination."""

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
class EventBridgeDestination(PropertyType):
    event_bus_arn: str | None = None


@dataclass
class EventDestination(PropertyType):
    matching_event_types: list[String] = field(default_factory=list)
    cloud_watch_destination: CloudWatchDestination | None = None
    enabled: bool | None = None
    event_bridge_destination: EventBridgeDestination | None = None
    kinesis_firehose_destination: KinesisFirehoseDestination | None = None
    name: str | None = None
    sns_destination: SnsDestination | None = None


@dataclass
class KinesisFirehoseDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "delivery_stream_arn": "DeliveryStreamARN",
        "iam_role_arn": "IAMRoleARN",
    }

    delivery_stream_arn: str | None = None
    iam_role_arn: str | None = None


@dataclass
class SnsDestination(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicARN",
    }

    topic_arn: str | None = None
