"""PropertyTypes for AWS::ECS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    base: DslValue[int] | None = None
    capacity_provider: DslValue[str] | None = None
    weight: DslValue[int] | None = None


@dataclass
class ClusterConfiguration(PropertyType):
    execute_command_configuration: DslValue[ExecuteCommandConfiguration] | None = None
    managed_storage_configuration: DslValue[ManagedStorageConfiguration] | None = None


@dataclass
class ClusterSettings(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ExecuteCommandConfiguration(PropertyType):
    kms_key_id: DslValue[str] | None = None
    log_configuration: DslValue[ExecuteCommandLogConfiguration] | None = None
    logging: DslValue[str] | None = None


@dataclass
class ExecuteCommandLogConfiguration(PropertyType):
    cloud_watch_encryption_enabled: DslValue[bool] | None = None
    cloud_watch_log_group_name: DslValue[str] | None = None
    s3_bucket_name: DslValue[str] | None = None
    s3_encryption_enabled: DslValue[bool] | None = None
    s3_key_prefix: DslValue[str] | None = None


@dataclass
class ManagedStorageConfiguration(PropertyType):
    fargate_ephemeral_storage_kms_key_id: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class ServiceConnectDefaults(PropertyType):
    namespace: DslValue[str] | None = None
