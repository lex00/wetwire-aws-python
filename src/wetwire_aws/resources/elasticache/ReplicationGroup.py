"""PropertyTypes for AWS::ElastiCache::ReplicationGroup."""

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


@dataclass
class NodeGroupConfiguration(PropertyType):
    node_group_id: DslValue[str] | None = None
    primary_availability_zone: DslValue[str] | None = None
    replica_availability_zones: list[DslValue[str]] = field(default_factory=list)
    replica_count: DslValue[int] | None = None
    slots: DslValue[str] | None = None
