"""PropertyTypes for AWS::Athena::WorkGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AclConfiguration(PropertyType):
    s3_acl_option: str | None = None


@dataclass
class Classification(PropertyType):
    name: str | None = None
    properties: dict[str, String] = field(default_factory=dict)


@dataclass
class CloudWatchLoggingConfiguration(PropertyType):
    enabled: bool | None = None
    log_group: str | None = None
    log_stream_name_prefix: str | None = None
    log_types: dict[str, Any] | None = None


@dataclass
class CustomerContentEncryptionConfiguration(PropertyType):
    kms_key: str | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    encryption_option: str | None = None
    kms_key: str | None = None


@dataclass
class EngineConfiguration(PropertyType):
    additional_configs: dict[str, String] = field(default_factory=dict)
    classifications: list[Classification] = field(default_factory=list)
    coordinator_dpu_size: int | None = None
    default_executor_dpu_size: int | None = None
    max_concurrent_dpus: int | None = None
    spark_properties: dict[str, String] = field(default_factory=dict)


@dataclass
class EngineVersion(PropertyType):
    effective_engine_version: str | None = None
    selected_engine_version: str | None = None


@dataclass
class ManagedLoggingConfiguration(PropertyType):
    enabled: bool | None = None
    kms_key: str | None = None


@dataclass
class ManagedQueryResultsConfiguration(PropertyType):
    enabled: bool | None = None
    encryption_configuration: ManagedStorageEncryptionConfiguration | None = None


@dataclass
class ManagedStorageEncryptionConfiguration(PropertyType):
    kms_key: str | None = None


@dataclass
class MonitoringConfiguration(PropertyType):
    cloud_watch_logging_configuration: CloudWatchLoggingConfiguration | None = None
    managed_logging_configuration: ManagedLoggingConfiguration | None = None
    s3_logging_configuration: S3LoggingConfiguration | None = None


@dataclass
class ResultConfiguration(PropertyType):
    acl_configuration: AclConfiguration | None = None
    encryption_configuration: EncryptionConfiguration | None = None
    expected_bucket_owner: str | None = None
    output_location: str | None = None


@dataclass
class S3LoggingConfiguration(PropertyType):
    enabled: bool | None = None
    kms_key: str | None = None
    log_location: str | None = None


@dataclass
class WorkGroupConfiguration(PropertyType):
    additional_configuration: str | None = None
    bytes_scanned_cutoff_per_query: int | None = None
    customer_content_encryption_configuration: (
        CustomerContentEncryptionConfiguration | None
    ) = None
    enforce_work_group_configuration: bool | None = None
    engine_configuration: EngineConfiguration | None = None
    engine_version: EngineVersion | None = None
    execution_role: str | None = None
    managed_query_results_configuration: ManagedQueryResultsConfiguration | None = None
    monitoring_configuration: MonitoringConfiguration | None = None
    publish_cloud_watch_metrics_enabled: bool | None = None
    requester_pays_enabled: bool | None = None
    result_configuration: ResultConfiguration | None = None
