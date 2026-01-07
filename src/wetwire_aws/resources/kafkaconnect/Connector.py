"""PropertyTypes for AWS::KafkaConnect::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApacheKafkaCluster(PropertyType):
    bootstrap_servers: DslValue[str] | None = None
    vpc: DslValue[Vpc] | None = None


@dataclass
class AutoScaling(PropertyType):
    max_worker_count: DslValue[int] | None = None
    mcu_count: DslValue[int] | None = None
    min_worker_count: DslValue[int] | None = None
    scale_in_policy: DslValue[ScaleInPolicy] | None = None
    scale_out_policy: DslValue[ScaleOutPolicy] | None = None


@dataclass
class Capacity(PropertyType):
    auto_scaling: DslValue[AutoScaling] | None = None
    provisioned_capacity: DslValue[ProvisionedCapacity] | None = None


@dataclass
class CloudWatchLogsLogDelivery(PropertyType):
    enabled: DslValue[bool] | None = None
    log_group: DslValue[str] | None = None


@dataclass
class CustomPlugin(PropertyType):
    custom_plugin_arn: DslValue[str] | None = None
    revision: DslValue[int] | None = None


@dataclass
class FirehoseLogDelivery(PropertyType):
    enabled: DslValue[bool] | None = None
    delivery_stream: DslValue[str] | None = None


@dataclass
class KafkaCluster(PropertyType):
    apache_kafka_cluster: DslValue[ApacheKafkaCluster] | None = None


@dataclass
class KafkaClusterClientAuthentication(PropertyType):
    authentication_type: DslValue[str] | None = None


@dataclass
class KafkaClusterEncryptionInTransit(PropertyType):
    encryption_type: DslValue[str] | None = None


@dataclass
class LogDelivery(PropertyType):
    worker_log_delivery: DslValue[WorkerLogDelivery] | None = None


@dataclass
class Plugin(PropertyType):
    custom_plugin: DslValue[CustomPlugin] | None = None


@dataclass
class ProvisionedCapacity(PropertyType):
    worker_count: DslValue[int] | None = None
    mcu_count: DslValue[int] | None = None


@dataclass
class S3LogDelivery(PropertyType):
    enabled: DslValue[bool] | None = None
    bucket: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class ScaleInPolicy(PropertyType):
    cpu_utilization_percentage: DslValue[int] | None = None


@dataclass
class ScaleOutPolicy(PropertyType):
    cpu_utilization_percentage: DslValue[int] | None = None


@dataclass
class Vpc(PropertyType):
    security_groups: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)


@dataclass
class WorkerConfiguration(PropertyType):
    revision: DslValue[int] | None = None
    worker_configuration_arn: DslValue[str] | None = None


@dataclass
class WorkerLogDelivery(PropertyType):
    cloud_watch_logs: DslValue[CloudWatchLogsLogDelivery] | None = None
    firehose: DslValue[FirehoseLogDelivery] | None = None
    s3: DslValue[S3LogDelivery] | None = None
