"""PropertyTypes for AWS::EMRServerless::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoStartConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class AutoStopConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    idle_timeout_minutes: DslValue[int] | None = None


@dataclass
class CloudWatchLoggingConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    encryption_key_arn: DslValue[str] | None = None
    log_group_name: DslValue[str] | None = None
    log_stream_name_prefix: DslValue[str] | None = None
    log_type_map: list[DslValue[LogTypeMapKeyValuePair]] = field(default_factory=list)


@dataclass
class ConfigurationObject(PropertyType):
    classification: DslValue[str] | None = None
    configurations: list[DslValue[ConfigurationObject]] = field(default_factory=list)
    properties: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class IdentityCenterConfiguration(PropertyType):
    identity_center_instance_arn: DslValue[str] | None = None


@dataclass
class ImageConfigurationInput(PropertyType):
    image_uri: DslValue[str] | None = None


@dataclass
class InitialCapacityConfig(PropertyType):
    worker_configuration: DslValue[WorkerConfiguration] | None = None
    worker_count: DslValue[int] | None = None


@dataclass
class InitialCapacityConfigKeyValuePair(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[InitialCapacityConfig] | None = None


@dataclass
class InteractiveConfiguration(PropertyType):
    livy_endpoint_enabled: DslValue[bool] | None = None
    studio_enabled: DslValue[bool] | None = None


@dataclass
class LogTypeMapKeyValuePair(PropertyType):
    key: DslValue[str] | None = None
    value: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ManagedPersistenceMonitoringConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    encryption_key_arn: DslValue[str] | None = None


@dataclass
class MaximumAllowedResources(PropertyType):
    cpu: DslValue[str] | None = None
    memory: DslValue[str] | None = None
    disk: DslValue[str] | None = None


@dataclass
class MonitoringConfiguration(PropertyType):
    cloud_watch_logging_configuration: (
        DslValue[CloudWatchLoggingConfiguration] | None
    ) = None
    managed_persistence_monitoring_configuration: (
        DslValue[ManagedPersistenceMonitoringConfiguration] | None
    ) = None
    prometheus_monitoring_configuration: (
        DslValue[PrometheusMonitoringConfiguration] | None
    ) = None
    s3_monitoring_configuration: DslValue[S3MonitoringConfiguration] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PrometheusMonitoringConfiguration(PropertyType):
    remote_write_url: DslValue[str] | None = None


@dataclass
class S3MonitoringConfiguration(PropertyType):
    encryption_key_arn: DslValue[str] | None = None
    log_uri: DslValue[str] | None = None


@dataclass
class SchedulerConfiguration(PropertyType):
    max_concurrent_runs: DslValue[int] | None = None
    queue_timeout_minutes: DslValue[int] | None = None


@dataclass
class WorkerConfiguration(PropertyType):
    cpu: DslValue[str] | None = None
    memory: DslValue[str] | None = None
    disk: DslValue[str] | None = None
    disk_type: DslValue[str] | None = None


@dataclass
class WorkerTypeSpecificationInput(PropertyType):
    image_configuration: DslValue[ImageConfigurationInput] | None = None
