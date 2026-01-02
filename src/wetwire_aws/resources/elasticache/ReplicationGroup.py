"""PropertyTypes for AWS::ElastiCache::ReplicationGroup."""

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


@dataclass
class NodeGroupConfiguration(PropertyType):
    node_group_id: str | None = None
    primary_availability_zone: str | None = None
    replica_availability_zones: list[String] = field(default_factory=list)
    replica_count: int | None = None
    slots: str | None = None
