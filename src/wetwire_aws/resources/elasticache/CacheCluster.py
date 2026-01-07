"""PropertyTypes for AWS::ElastiCache::CacheCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchLogsDestinationDetails(PropertyType):
    log_group: DslValue[str] | None = None


@dataclass
class DestinationDetails(PropertyType):
    cloud_watch_logs_details: DslValue[CloudWatchLogsDestinationDetails] | None = None
    kinesis_firehose_details: DslValue[KinesisFirehoseDestinationDetails] | None = None


@dataclass
class KinesisFirehoseDestinationDetails(PropertyType):
    delivery_stream: DslValue[str] | None = None


@dataclass
class LogDeliveryConfigurationRequest(PropertyType):
    destination_details: DslValue[DestinationDetails] | None = None
    destination_type: DslValue[str] | None = None
    log_format: DslValue[str] | None = None
    log_type: DslValue[str] | None = None
