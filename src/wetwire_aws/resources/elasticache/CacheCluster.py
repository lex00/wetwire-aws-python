"""PropertyTypes for AWS::ElastiCache::CacheCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchLogsDestinationDetails(PropertyType):
    log_group: str | None = None


@dataclass
class DestinationDetails(PropertyType):
    cloud_watch_logs_details: CloudWatchLogsDestinationDetails | None = None
    kinesis_firehose_details: KinesisFirehoseDestinationDetails | None = None


@dataclass
class KinesisFirehoseDestinationDetails(PropertyType):
    delivery_stream: str | None = None


@dataclass
class LogDeliveryConfigurationRequest(PropertyType):
    destination_details: DestinationDetails | None = None
    destination_type: str | None = None
    log_format: str | None = None
    log_type: str | None = None
