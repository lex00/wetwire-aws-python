"""PropertyTypes for AWS::KinesisAnalyticsV2::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApplicationCodeConfiguration(PropertyType):
    code_content: DslValue[CodeContent] | None = None
    code_content_type: DslValue[str] | None = None


@dataclass
class ApplicationConfiguration(PropertyType):
    application_code_configuration: DslValue[ApplicationCodeConfiguration] | None = None
    application_encryption_configuration: (
        DslValue[ApplicationEncryptionConfiguration] | None
    ) = None
    application_snapshot_configuration: (
        DslValue[ApplicationSnapshotConfiguration] | None
    ) = None
    application_system_rollback_configuration: (
        DslValue[ApplicationSystemRollbackConfiguration] | None
    ) = None
    environment_properties: DslValue[EnvironmentProperties] | None = None
    flink_application_configuration: DslValue[FlinkApplicationConfiguration] | None = (
        None
    )
    sql_application_configuration: DslValue[SqlApplicationConfiguration] | None = None
    vpc_configurations: list[DslValue[VpcConfiguration]] = field(default_factory=list)
    zeppelin_application_configuration: (
        DslValue[ZeppelinApplicationConfiguration] | None
    ) = None


@dataclass
class ApplicationEncryptionConfiguration(PropertyType):
    key_type: DslValue[str] | None = None
    key_id: DslValue[str] | None = None


@dataclass
class ApplicationMaintenanceConfiguration(PropertyType):
    application_maintenance_window_start_time: DslValue[str] | None = None


@dataclass
class ApplicationRestoreConfiguration(PropertyType):
    application_restore_type: DslValue[str] | None = None
    snapshot_name: DslValue[str] | None = None


@dataclass
class ApplicationSnapshotConfiguration(PropertyType):
    snapshots_enabled: DslValue[bool] | None = None


@dataclass
class ApplicationSystemRollbackConfiguration(PropertyType):
    rollback_enabled: DslValue[bool] | None = None


@dataclass
class CSVMappingParameters(PropertyType):
    record_column_delimiter: DslValue[str] | None = None
    record_row_delimiter: DslValue[str] | None = None


@dataclass
class CatalogConfiguration(PropertyType):
    glue_data_catalog_configuration: DslValue[GlueDataCatalogConfiguration] | None = (
        None
    )


@dataclass
class CheckpointConfiguration(PropertyType):
    configuration_type: DslValue[str] | None = None
    checkpoint_interval: DslValue[int] | None = None
    checkpointing_enabled: DslValue[bool] | None = None
    min_pause_between_checkpoints: DslValue[int] | None = None


@dataclass
class CodeContent(PropertyType):
    s3_content_location: DslValue[S3ContentLocation] | None = None
    text_content: DslValue[str] | None = None
    zip_file_content: DslValue[str] | None = None


@dataclass
class CustomArtifactConfiguration(PropertyType):
    artifact_type: DslValue[str] | None = None
    maven_reference: DslValue[MavenReference] | None = None
    s3_content_location: DslValue[S3ContentLocation] | None = None


@dataclass
class DeployAsApplicationConfiguration(PropertyType):
    s3_content_location: DslValue[S3ContentBaseLocation] | None = None


@dataclass
class EnvironmentProperties(PropertyType):
    property_groups: list[DslValue[PropertyGroup]] = field(default_factory=list)


@dataclass
class FlinkApplicationConfiguration(PropertyType):
    checkpoint_configuration: DslValue[CheckpointConfiguration] | None = None
    monitoring_configuration: DslValue[MonitoringConfiguration] | None = None
    parallelism_configuration: DslValue[ParallelismConfiguration] | None = None


@dataclass
class FlinkRunConfiguration(PropertyType):
    allow_non_restored_state: DslValue[bool] | None = None


@dataclass
class GlueDataCatalogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_arn": "DatabaseARN",
    }

    database_arn: DslValue[str] | None = None


@dataclass
class Input(PropertyType):
    input_schema: DslValue[InputSchema] | None = None
    name_prefix: DslValue[str] | None = None
    input_parallelism: DslValue[InputParallelism] | None = None
    input_processing_configuration: DslValue[InputProcessingConfiguration] | None = None
    kinesis_firehose_input: DslValue[KinesisFirehoseInput] | None = None
    kinesis_streams_input: DslValue[KinesisStreamsInput] | None = None


@dataclass
class InputLambdaProcessor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: DslValue[str] | None = None


@dataclass
class InputParallelism(PropertyType):
    count: DslValue[int] | None = None


@dataclass
class InputProcessingConfiguration(PropertyType):
    input_lambda_processor: DslValue[InputLambdaProcessor] | None = None


@dataclass
class InputSchema(PropertyType):
    record_columns: list[DslValue[RecordColumn]] = field(default_factory=list)
    record_format: DslValue[RecordFormat] | None = None
    record_encoding: DslValue[str] | None = None


@dataclass
class JSONMappingParameters(PropertyType):
    record_row_path: DslValue[str] | None = None


@dataclass
class KinesisFirehoseInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: DslValue[str] | None = None


@dataclass
class KinesisStreamsInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: DslValue[str] | None = None


@dataclass
class MappingParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "csv_mapping_parameters": "CSVMappingParameters",
        "json_mapping_parameters": "JSONMappingParameters",
    }

    csv_mapping_parameters: DslValue[CSVMappingParameters] | None = None
    json_mapping_parameters: DslValue[JSONMappingParameters] | None = None


@dataclass
class MavenReference(PropertyType):
    artifact_id: DslValue[str] | None = None
    group_id: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class MonitoringConfiguration(PropertyType):
    configuration_type: DslValue[str] | None = None
    log_level: DslValue[str] | None = None
    metrics_level: DslValue[str] | None = None


@dataclass
class ParallelismConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parallelism_per_kpu": "ParallelismPerKPU",
    }

    configuration_type: DslValue[str] | None = None
    auto_scaling_enabled: DslValue[bool] | None = None
    parallelism: DslValue[int] | None = None
    parallelism_per_kpu: DslValue[int] | None = None


@dataclass
class PropertyGroup(PropertyType):
    property_group_id: DslValue[str] | None = None
    property_map: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class RecordColumn(PropertyType):
    name: DslValue[str] | None = None
    sql_type: DslValue[str] | None = None
    mapping: DslValue[str] | None = None


@dataclass
class RecordFormat(PropertyType):
    record_format_type: DslValue[str] | None = None
    mapping_parameters: DslValue[MappingParameters] | None = None


@dataclass
class RunConfiguration(PropertyType):
    application_restore_configuration: (
        DslValue[ApplicationRestoreConfiguration] | None
    ) = None
    flink_run_configuration: DslValue[FlinkRunConfiguration] | None = None


@dataclass
class S3ContentBaseLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
    }

    bucket_arn: DslValue[str] | None = None
    base_path: DslValue[str] | None = None


@dataclass
class S3ContentLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
    }

    bucket_arn: DslValue[str] | None = None
    file_key: DslValue[str] | None = None
    object_version: DslValue[str] | None = None


@dataclass
class SqlApplicationConfiguration(PropertyType):
    inputs: list[DslValue[Input]] = field(default_factory=list)


@dataclass
class VpcConfiguration(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ZeppelinApplicationConfiguration(PropertyType):
    catalog_configuration: DslValue[CatalogConfiguration] | None = None
    custom_artifacts_configuration: list[DslValue[CustomArtifactConfiguration]] = field(
        default_factory=list
    )
    deploy_as_application_configuration: (
        DslValue[DeployAsApplicationConfiguration] | None
    ) = None
    monitoring_configuration: DslValue[ZeppelinMonitoringConfiguration] | None = None


@dataclass
class ZeppelinMonitoringConfiguration(PropertyType):
    log_level: DslValue[str] | None = None
