"""PropertyTypes for AWS::ECS::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapacityProviderStrategyItem(PropertyType):
    base: int | None = None
    capacity_provider: str | None = None
    weight: int | None = None


@dataclass
class ClusterConfiguration(PropertyType):
    execute_command_configuration: ExecuteCommandConfiguration | None = None
    managed_storage_configuration: ManagedStorageConfiguration | None = None


@dataclass
class ClusterSettings(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class ExecuteCommandConfiguration(PropertyType):
    kms_key_id: str | None = None
    log_configuration: ExecuteCommandLogConfiguration | None = None
    logging: str | None = None


@dataclass
class ExecuteCommandLogConfiguration(PropertyType):
    cloud_watch_encryption_enabled: bool | None = None
    cloud_watch_log_group_name: str | None = None
    s3_bucket_name: str | None = None
    s3_encryption_enabled: bool | None = None
    s3_key_prefix: str | None = None


@dataclass
class ManagedStorageConfiguration(PropertyType):
    fargate_ephemeral_storage_kms_key_id: str | None = None
    kms_key_id: str | None = None


@dataclass
class ServiceConnectDefaults(PropertyType):
    namespace: str | None = None
