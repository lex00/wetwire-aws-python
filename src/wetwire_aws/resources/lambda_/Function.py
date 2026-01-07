"""PropertyTypes for AWS::Lambda::Function."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapacityProviderConfig(PropertyType):
    lambda_managed_instances_capacity_provider_config: (
        DslValue[LambdaManagedInstancesCapacityProviderConfig] | None
    ) = None


@dataclass
class Code(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "source_kms_key_arn": "SourceKMSKeyArn",
    }

    image_uri: DslValue[str] | None = None
    s3_bucket: DslValue[str] | None = None
    s3_key: DslValue[str] | None = None
    s3_object_version: DslValue[str] | None = None
    source_kms_key_arn: DslValue[str] | None = None
    zip_file: DslValue[str] | None = None


@dataclass
class DeadLetterConfig(PropertyType):
    target_arn: DslValue[str] | None = None


@dataclass
class DurableConfig(PropertyType):
    execution_timeout: DslValue[int] | None = None
    retention_period_in_days: DslValue[int] | None = None


@dataclass
class Environment(PropertyType):
    variables: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class EphemeralStorage(PropertyType):
    size: DslValue[int] | None = None


@dataclass
class FileSystemConfig(PropertyType):
    arn: DslValue[str] | None = None
    local_mount_path: DslValue[str] | None = None


@dataclass
class FunctionScalingConfig(PropertyType):
    max_execution_environments: DslValue[int] | None = None
    min_execution_environments: DslValue[int] | None = None


@dataclass
class ImageConfig(PropertyType):
    command: list[DslValue[str]] = field(default_factory=list)
    entry_point: list[DslValue[str]] = field(default_factory=list)
    working_directory: DslValue[str] | None = None


@dataclass
class LambdaManagedInstancesCapacityProviderConfig(PropertyType):
    capacity_provider_arn: DslValue[str] | None = None
    execution_environment_memory_gi_b_per_v_cpu: DslValue[float] | None = None
    per_execution_environment_max_concurrency: DslValue[int] | None = None


@dataclass
class LoggingConfig(PropertyType):
    application_log_level: DslValue[str] | None = None
    log_format: DslValue[str] | None = None
    log_group: DslValue[str] | None = None
    system_log_level: DslValue[str] | None = None


@dataclass
class RuntimeManagementConfig(PropertyType):
    update_runtime_on: DslValue[str] | None = None
    runtime_version_arn: DslValue[str] | None = None


@dataclass
class SnapStart(PropertyType):
    apply_on: DslValue[str] | None = None


@dataclass
class SnapStartResponse(PropertyType):
    apply_on: DslValue[str] | None = None
    optimization_status: DslValue[str] | None = None


@dataclass
class TenancyConfig(PropertyType):
    tenant_isolation_mode: DslValue[str] | None = None


@dataclass
class TracingConfig(PropertyType):
    mode: DslValue[str] | None = None


@dataclass
class VpcConfig(PropertyType):
    ipv6_allowed_for_dual_stack: DslValue[bool] | None = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
