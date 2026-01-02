"""PropertyTypes for AWS::KafkaConnect::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApacheKafkaCluster(PropertyType):
    bootstrap_servers: str | None = None
    vpc: Vpc | None = None


@dataclass
class AutoScaling(PropertyType):
    max_worker_count: int | None = None
    mcu_count: int | None = None
    min_worker_count: int | None = None
    scale_in_policy: ScaleInPolicy | None = None
    scale_out_policy: ScaleOutPolicy | None = None


@dataclass
class Capacity(PropertyType):
    auto_scaling: AutoScaling | None = None
    provisioned_capacity: ProvisionedCapacity | None = None


@dataclass
class CloudWatchLogsLogDelivery(PropertyType):
    enabled: bool | None = None
    log_group: str | None = None


@dataclass
class CustomPlugin(PropertyType):
    custom_plugin_arn: str | None = None
    revision: int | None = None


@dataclass
class FirehoseLogDelivery(PropertyType):
    enabled: bool | None = None
    delivery_stream: str | None = None


@dataclass
class KafkaCluster(PropertyType):
    apache_kafka_cluster: ApacheKafkaCluster | None = None


@dataclass
class KafkaClusterClientAuthentication(PropertyType):
    authentication_type: str | None = None


@dataclass
class KafkaClusterEncryptionInTransit(PropertyType):
    encryption_type: str | None = None


@dataclass
class LogDelivery(PropertyType):
    worker_log_delivery: WorkerLogDelivery | None = None


@dataclass
class Plugin(PropertyType):
    custom_plugin: CustomPlugin | None = None


@dataclass
class ProvisionedCapacity(PropertyType):
    worker_count: int | None = None
    mcu_count: int | None = None


@dataclass
class S3LogDelivery(PropertyType):
    enabled: bool | None = None
    bucket: str | None = None
    prefix: str | None = None


@dataclass
class ScaleInPolicy(PropertyType):
    cpu_utilization_percentage: int | None = None


@dataclass
class ScaleOutPolicy(PropertyType):
    cpu_utilization_percentage: int | None = None


@dataclass
class Vpc(PropertyType):
    security_groups: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)


@dataclass
class WorkerConfiguration(PropertyType):
    revision: int | None = None
    worker_configuration_arn: str | None = None


@dataclass
class WorkerLogDelivery(PropertyType):
    cloud_watch_logs: CloudWatchLogsLogDelivery | None = None
    firehose: FirehoseLogDelivery | None = None
    s3: S3LogDelivery | None = None
