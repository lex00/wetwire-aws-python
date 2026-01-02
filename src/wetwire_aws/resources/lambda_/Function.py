"""PropertyTypes for AWS::Lambda::Function."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapacityProviderConfig(PropertyType):
    lambda_managed_instances_capacity_provider_config: (
        LambdaManagedInstancesCapacityProviderConfig | None
    ) = None


@dataclass
class Code(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_kms_key_arn": "SourceKMSKeyArn",
    }

    image_uri: str | None = None
    s3_bucket: str | None = None
    s3_key: str | None = None
    s3_object_version: str | None = None
    source_kms_key_arn: str | None = None
    zip_file: str | None = None


@dataclass
class DeadLetterConfig(PropertyType):
    target_arn: str | None = None


@dataclass
class DurableConfig(PropertyType):
    execution_timeout: int | None = None
    retention_period_in_days: int | None = None


@dataclass
class Environment(PropertyType):
    variables: dict[str, String] = field(default_factory=dict)


@dataclass
class EphemeralStorage(PropertyType):
    size: int | None = None


@dataclass
class FileSystemConfig(PropertyType):
    arn: str | None = None
    local_mount_path: str | None = None


@dataclass
class FunctionScalingConfig(PropertyType):
    max_execution_environments: int | None = None
    min_execution_environments: int | None = None


@dataclass
class ImageConfig(PropertyType):
    command: list[String] = field(default_factory=list)
    entry_point: list[String] = field(default_factory=list)
    working_directory: str | None = None


@dataclass
class LambdaManagedInstancesCapacityProviderConfig(PropertyType):
    capacity_provider_arn: str | None = None
    execution_environment_memory_gi_b_per_v_cpu: float | None = None
    per_execution_environment_max_concurrency: int | None = None


@dataclass
class LoggingConfig(PropertyType):
    application_log_level: str | None = None
    log_format: str | None = None
    log_group: str | None = None
    system_log_level: str | None = None


@dataclass
class RuntimeManagementConfig(PropertyType):
    update_runtime_on: str | None = None
    runtime_version_arn: str | None = None


@dataclass
class SnapStart(PropertyType):
    apply_on: str | None = None


@dataclass
class SnapStartResponse(PropertyType):
    apply_on: str | None = None
    optimization_status: str | None = None


@dataclass
class TenancyConfig(PropertyType):
    tenant_isolation_mode: str | None = None


@dataclass
class TracingConfig(PropertyType):
    mode: str | None = None


@dataclass
class VpcConfig(PropertyType):
    ipv6_allowed_for_dual_stack: bool | None = None
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
