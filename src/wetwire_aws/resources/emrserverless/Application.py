"""PropertyTypes for AWS::EMRServerless::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoStartConfiguration(PropertyType):
    enabled: bool | None = None


@dataclass
class AutoStopConfiguration(PropertyType):
    enabled: bool | None = None
    idle_timeout_minutes: int | None = None


@dataclass
class CloudWatchLoggingConfiguration(PropertyType):
    enabled: bool | None = None
    encryption_key_arn: str | None = None
    log_group_name: str | None = None
    log_stream_name_prefix: str | None = None
    log_type_map: list[LogTypeMapKeyValuePair] = field(default_factory=list)


@dataclass
class ConfigurationObject(PropertyType):
    classification: str | None = None
    configurations: list[ConfigurationObject] = field(default_factory=list)
    properties: dict[str, String] = field(default_factory=dict)


@dataclass
class IdentityCenterConfiguration(PropertyType):
    identity_center_instance_arn: str | None = None


@dataclass
class ImageConfigurationInput(PropertyType):
    image_uri: str | None = None


@dataclass
class InitialCapacityConfig(PropertyType):
    worker_configuration: WorkerConfiguration | None = None
    worker_count: int | None = None


@dataclass
class InitialCapacityConfigKeyValuePair(PropertyType):
    key: str | None = None
    value: InitialCapacityConfig | None = None


@dataclass
class InteractiveConfiguration(PropertyType):
    livy_endpoint_enabled: bool | None = None
    studio_enabled: bool | None = None


@dataclass
class LogTypeMapKeyValuePair(PropertyType):
    key: str | None = None
    value: list[String] = field(default_factory=list)


@dataclass
class ManagedPersistenceMonitoringConfiguration(PropertyType):
    enabled: bool | None = None
    encryption_key_arn: str | None = None


@dataclass
class MaximumAllowedResources(PropertyType):
    cpu: str | None = None
    memory: str | None = None
    disk: str | None = None


@dataclass
class MonitoringConfiguration(PropertyType):
    cloud_watch_logging_configuration: CloudWatchLoggingConfiguration | None = None
    managed_persistence_monitoring_configuration: (
        ManagedPersistenceMonitoringConfiguration | None
    ) = None
    prometheus_monitoring_configuration: PrometheusMonitoringConfiguration | None = None
    s3_monitoring_configuration: S3MonitoringConfiguration | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class PrometheusMonitoringConfiguration(PropertyType):
    remote_write_url: str | None = None


@dataclass
class S3MonitoringConfiguration(PropertyType):
    encryption_key_arn: str | None = None
    log_uri: str | None = None


@dataclass
class SchedulerConfiguration(PropertyType):
    max_concurrent_runs: int | None = None
    queue_timeout_minutes: int | None = None


@dataclass
class WorkerConfiguration(PropertyType):
    cpu: str | None = None
    memory: str | None = None
    disk: str | None = None
    disk_type: str | None = None


@dataclass
class WorkerTypeSpecificationInput(PropertyType):
    image_configuration: ImageConfigurationInput | None = None
