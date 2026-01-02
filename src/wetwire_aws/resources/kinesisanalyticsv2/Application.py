"""PropertyTypes for AWS::KinesisAnalyticsV2::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApplicationCodeConfiguration(PropertyType):
    code_content: CodeContent | None = None
    code_content_type: str | None = None


@dataclass
class ApplicationConfiguration(PropertyType):
    application_code_configuration: ApplicationCodeConfiguration | None = None
    application_encryption_configuration: ApplicationEncryptionConfiguration | None = (
        None
    )
    application_snapshot_configuration: ApplicationSnapshotConfiguration | None = None
    application_system_rollback_configuration: (
        ApplicationSystemRollbackConfiguration | None
    ) = None
    environment_properties: EnvironmentProperties | None = None
    flink_application_configuration: FlinkApplicationConfiguration | None = None
    sql_application_configuration: SqlApplicationConfiguration | None = None
    vpc_configurations: list[VpcConfiguration] = field(default_factory=list)
    zeppelin_application_configuration: ZeppelinApplicationConfiguration | None = None


@dataclass
class ApplicationEncryptionConfiguration(PropertyType):
    key_type: str | None = None
    key_id: str | None = None


@dataclass
class ApplicationMaintenanceConfiguration(PropertyType):
    application_maintenance_window_start_time: str | None = None


@dataclass
class ApplicationRestoreConfiguration(PropertyType):
    application_restore_type: str | None = None
    snapshot_name: str | None = None


@dataclass
class ApplicationSnapshotConfiguration(PropertyType):
    snapshots_enabled: bool | None = None


@dataclass
class ApplicationSystemRollbackConfiguration(PropertyType):
    rollback_enabled: bool | None = None


@dataclass
class CSVMappingParameters(PropertyType):
    record_column_delimiter: str | None = None
    record_row_delimiter: str | None = None


@dataclass
class CatalogConfiguration(PropertyType):
    glue_data_catalog_configuration: GlueDataCatalogConfiguration | None = None


@dataclass
class CheckpointConfiguration(PropertyType):
    configuration_type: str | None = None
    checkpoint_interval: int | None = None
    checkpointing_enabled: bool | None = None
    min_pause_between_checkpoints: int | None = None


@dataclass
class CodeContent(PropertyType):
    s3_content_location: S3ContentLocation | None = None
    text_content: str | None = None
    zip_file_content: str | None = None


@dataclass
class CustomArtifactConfiguration(PropertyType):
    artifact_type: str | None = None
    maven_reference: MavenReference | None = None
    s3_content_location: S3ContentLocation | None = None


@dataclass
class DeployAsApplicationConfiguration(PropertyType):
    s3_content_location: S3ContentBaseLocation | None = None


@dataclass
class EnvironmentProperties(PropertyType):
    property_groups: list[PropertyGroup] = field(default_factory=list)


@dataclass
class FlinkApplicationConfiguration(PropertyType):
    checkpoint_configuration: CheckpointConfiguration | None = None
    monitoring_configuration: MonitoringConfiguration | None = None
    parallelism_configuration: ParallelismConfiguration | None = None


@dataclass
class FlinkRunConfiguration(PropertyType):
    allow_non_restored_state: bool | None = None


@dataclass
class GlueDataCatalogConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_arn": "DatabaseARN",
    }

    database_arn: str | None = None


@dataclass
class Input(PropertyType):
    input_schema: InputSchema | None = None
    name_prefix: str | None = None
    input_parallelism: InputParallelism | None = None
    input_processing_configuration: InputProcessingConfiguration | None = None
    kinesis_firehose_input: KinesisFirehoseInput | None = None
    kinesis_streams_input: KinesisStreamsInput | None = None


@dataclass
class InputLambdaProcessor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: str | None = None


@dataclass
class InputParallelism(PropertyType):
    count: int | None = None


@dataclass
class InputProcessingConfiguration(PropertyType):
    input_lambda_processor: InputLambdaProcessor | None = None


@dataclass
class InputSchema(PropertyType):
    record_columns: list[RecordColumn] = field(default_factory=list)
    record_format: RecordFormat | None = None
    record_encoding: str | None = None


@dataclass
class JSONMappingParameters(PropertyType):
    record_row_path: str | None = None


@dataclass
class KinesisFirehoseInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: str | None = None


@dataclass
class KinesisStreamsInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    resource_arn: str | None = None


@dataclass
class MappingParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "csv_mapping_parameters": "CSVMappingParameters",
        "json_mapping_parameters": "JSONMappingParameters",
    }

    csv_mapping_parameters: CSVMappingParameters | None = None
    json_mapping_parameters: JSONMappingParameters | None = None


@dataclass
class MavenReference(PropertyType):
    artifact_id: str | None = None
    group_id: str | None = None
    version: str | None = None


@dataclass
class MonitoringConfiguration(PropertyType):
    configuration_type: str | None = None
    log_level: str | None = None
    metrics_level: str | None = None


@dataclass
class ParallelismConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "parallelism_per_kpu": "ParallelismPerKPU",
    }

    configuration_type: str | None = None
    auto_scaling_enabled: bool | None = None
    parallelism: int | None = None
    parallelism_per_kpu: int | None = None


@dataclass
class PropertyGroup(PropertyType):
    property_group_id: str | None = None
    property_map: dict[str, String] = field(default_factory=dict)


@dataclass
class RecordColumn(PropertyType):
    name: str | None = None
    sql_type: str | None = None
    mapping: str | None = None


@dataclass
class RecordFormat(PropertyType):
    record_format_type: str | None = None
    mapping_parameters: MappingParameters | None = None


@dataclass
class RunConfiguration(PropertyType):
    application_restore_configuration: ApplicationRestoreConfiguration | None = None
    flink_run_configuration: FlinkRunConfiguration | None = None


@dataclass
class S3ContentBaseLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
    }

    bucket_arn: str | None = None
    base_path: str | None = None


@dataclass
class S3ContentLocation(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
    }

    bucket_arn: str | None = None
    file_key: str | None = None
    object_version: str | None = None


@dataclass
class SqlApplicationConfiguration(PropertyType):
    inputs: list[Input] = field(default_factory=list)


@dataclass
class VpcConfiguration(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)


@dataclass
class ZeppelinApplicationConfiguration(PropertyType):
    catalog_configuration: CatalogConfiguration | None = None
    custom_artifacts_configuration: list[CustomArtifactConfiguration] = field(
        default_factory=list
    )
    deploy_as_application_configuration: DeployAsApplicationConfiguration | None = None
    monitoring_configuration: ZeppelinMonitoringConfiguration | None = None


@dataclass
class ZeppelinMonitoringConfiguration(PropertyType):
    log_level: str | None = None
