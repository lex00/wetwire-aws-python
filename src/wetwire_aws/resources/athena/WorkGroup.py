"""PropertyTypes for AWS::Athena::WorkGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AclConfiguration(PropertyType):
    s3_acl_option: DslValue[str] | None = None


@dataclass
class Classification(PropertyType):
    name: DslValue[str] | None = None
    properties: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class CloudWatchLoggingConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    log_group: DslValue[str] | None = None
    log_stream_name_prefix: DslValue[str] | None = None
    log_types: DslValue[dict[str, Any]] | None = None


@dataclass
class CustomerContentEncryptionConfiguration(PropertyType):
    kms_key: DslValue[str] | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    encryption_option: DslValue[str] | None = None
    kms_key: DslValue[str] | None = None


@dataclass
class EngineConfiguration(PropertyType):
    additional_configs: dict[str, DslValue[str]] = field(default_factory=dict)
    classifications: list[DslValue[Classification]] = field(default_factory=list)
    coordinator_dpu_size: DslValue[int] | None = None
    default_executor_dpu_size: DslValue[int] | None = None
    max_concurrent_dpus: DslValue[int] | None = None
    spark_properties: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class EngineVersion(PropertyType):
    effective_engine_version: DslValue[str] | None = None
    selected_engine_version: DslValue[str] | None = None


@dataclass
class ManagedLoggingConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    kms_key: DslValue[str] | None = None


@dataclass
class ManagedQueryResultsConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    encryption_configuration: DslValue[ManagedStorageEncryptionConfiguration] | None = (
        None
    )


@dataclass
class ManagedStorageEncryptionConfiguration(PropertyType):
    kms_key: DslValue[str] | None = None


@dataclass
class MonitoringConfiguration(PropertyType):
    cloud_watch_logging_configuration: (
        DslValue[CloudWatchLoggingConfiguration] | None
    ) = None
    managed_logging_configuration: DslValue[ManagedLoggingConfiguration] | None = None
    s3_logging_configuration: DslValue[S3LoggingConfiguration] | None = None


@dataclass
class ResultConfiguration(PropertyType):
    acl_configuration: DslValue[AclConfiguration] | None = None
    encryption_configuration: DslValue[EncryptionConfiguration] | None = None
    expected_bucket_owner: DslValue[str] | None = None
    output_location: DslValue[str] | None = None


@dataclass
class S3LoggingConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    kms_key: DslValue[str] | None = None
    log_location: DslValue[str] | None = None


@dataclass
class WorkGroupConfiguration(PropertyType):
    additional_configuration: DslValue[str] | None = None
    bytes_scanned_cutoff_per_query: DslValue[int] | None = None
    customer_content_encryption_configuration: (
        DslValue[CustomerContentEncryptionConfiguration] | None
    ) = None
    enforce_work_group_configuration: DslValue[bool] | None = None
    engine_configuration: DslValue[EngineConfiguration] | None = None
    engine_version: DslValue[EngineVersion] | None = None
    execution_role: DslValue[str] | None = None
    managed_query_results_configuration: (
        DslValue[ManagedQueryResultsConfiguration] | None
    ) = None
    monitoring_configuration: DslValue[MonitoringConfiguration] | None = None
    publish_cloud_watch_metrics_enabled: DslValue[bool] | None = None
    requester_pays_enabled: DslValue[bool] | None = None
    result_configuration: DslValue[ResultConfiguration] | None = None
