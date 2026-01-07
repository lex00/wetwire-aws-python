"""PropertyTypes for AWS::PinpointEmail::ConfigurationSetEventDestination."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchDestination(PropertyType):
    dimension_configurations: list[DslValue[DimensionConfiguration]] = field(
        default_factory=list
    )


@dataclass
class DimensionConfiguration(PropertyType):
    default_dimension_value: DslValue[str] | None = None
    dimension_name: DslValue[str] | None = None
    dimension_value_source: DslValue[str] | None = None


@dataclass
class EventDestination(PropertyType):
    matching_event_types: list[DslValue[str]] = field(default_factory=list)
    cloud_watch_destination: DslValue[CloudWatchDestination] | None = None
    enabled: DslValue[bool] | None = None
    kinesis_firehose_destination: DslValue[KinesisFirehoseDestination] | None = None
    pinpoint_destination: DslValue[PinpointDestination] | None = None
    sns_destination: DslValue[SnsDestination] | None = None


@dataclass
class KinesisFirehoseDestination(PropertyType):
    delivery_stream_arn: DslValue[str] | None = None
    iam_role_arn: DslValue[str] | None = None


@dataclass
class PinpointDestination(PropertyType):
    application_arn: DslValue[str] | None = None


@dataclass
class SnsDestination(PropertyType):
    topic_arn: DslValue[str] | None = None
