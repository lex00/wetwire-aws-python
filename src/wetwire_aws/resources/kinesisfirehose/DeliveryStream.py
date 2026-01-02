"""PropertyTypes for AWS::KinesisFirehose::DeliveryStream."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AmazonOpenSearchServerlessBufferingHints(PropertyType):
    interval_in_seconds: int | None = None
    size_in_m_bs: int | None = None


@dataclass
class AmazonOpenSearchServerlessDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    index_name: str | None = None
    role_arn: str | None = None
    s3_configuration: S3DestinationConfiguration | None = None
    buffering_hints: AmazonOpenSearchServerlessBufferingHints | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    collection_endpoint: str | None = None
    processing_configuration: ProcessingConfiguration | None = None
    retry_options: AmazonOpenSearchServerlessRetryOptions | None = None
    s3_backup_mode: str | None = None
    vpc_configuration: VpcConfiguration | None = None


@dataclass
class AmazonOpenSearchServerlessRetryOptions(PropertyType):
    duration_in_seconds: int | None = None


@dataclass
class AmazonopensearchserviceBufferingHints(PropertyType):
    interval_in_seconds: int | None = None
    size_in_m_bs: int | None = None


@dataclass
class AmazonopensearchserviceDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_arn": "DomainARN",
        "role_arn": "RoleARN",
    }

    index_name: str | None = None
    role_arn: str | None = None
    s3_configuration: S3DestinationConfiguration | None = None
    buffering_hints: AmazonopensearchserviceBufferingHints | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    cluster_endpoint: str | None = None
    document_id_options: DocumentIdOptions | None = None
    domain_arn: str | None = None
    index_rotation_period: str | None = None
    processing_configuration: ProcessingConfiguration | None = None
    retry_options: AmazonopensearchserviceRetryOptions | None = None
    s3_backup_mode: str | None = None
    type_name: str | None = None
    vpc_configuration: VpcConfiguration | None = None


@dataclass
class AmazonopensearchserviceRetryOptions(PropertyType):
    duration_in_seconds: int | None = None


@dataclass
class AuthenticationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    connectivity: str | None = None
    role_arn: str | None = None


@dataclass
class BufferingHints(PropertyType):
    interval_in_seconds: int | None = None
    size_in_m_bs: int | None = None


@dataclass
class CatalogConfiguration(PropertyType):
    catalog_arn: str | None = None
    warehouse_location: str | None = None


@dataclass
class CloudWatchLoggingOptions(PropertyType):
    enabled: bool | None = None
    log_group_name: str | None = None
    log_stream_name: str | None = None


@dataclass
class CopyCommand(PropertyType):
    data_table_name: str | None = None
    copy_options: str | None = None
    data_table_columns: str | None = None


@dataclass
class DataFormatConversionConfiguration(PropertyType):
    enabled: bool | None = None
    input_format_configuration: InputFormatConfiguration | None = None
    output_format_configuration: OutputFormatConfiguration | None = None
    schema_configuration: SchemaConfiguration | None = None


@dataclass
class DatabaseColumns(PropertyType):
    exclude: list[String] = field(default_factory=list)
    include: list[String] = field(default_factory=list)


@dataclass
class DatabaseSourceAuthenticationConfiguration(PropertyType):
    secrets_manager_configuration: SecretsManagerConfiguration | None = None


@dataclass
class DatabaseSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_source_vpc_configuration": "DatabaseSourceVPCConfiguration",
        "ssl_mode": "SSLMode",
    }

    database_source_authentication_configuration: (
        DatabaseSourceAuthenticationConfiguration | None
    ) = None
    database_source_vpc_configuration: DatabaseSourceVPCConfiguration | None = None
    databases: Databases | None = None
    endpoint: str | None = None
    port: int | None = None
    snapshot_watermark_table: str | None = None
    tables: DatabaseTables | None = None
    type_: str | None = None
    columns: DatabaseColumns | None = None
    digest: str | None = None
    public_certificate: str | None = None
    ssl_mode: str | None = None
    surrogate_keys: list[String] = field(default_factory=list)


@dataclass
class DatabaseSourceVPCConfiguration(PropertyType):
    vpc_endpoint_service_name: str | None = None


@dataclass
class DatabaseTables(PropertyType):
    exclude: list[String] = field(default_factory=list)
    include: list[String] = field(default_factory=list)


@dataclass
class Databases(PropertyType):
    exclude: list[String] = field(default_factory=list)
    include: list[String] = field(default_factory=list)


@dataclass
class DeliveryStreamEncryptionConfigurationInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_arn": "KeyARN",
    }

    key_type: str | None = None
    key_arn: str | None = None


@dataclass
class Deserializer(PropertyType):
    hive_json_ser_de: HiveJsonSerDe | None = None
    open_x_json_ser_de: OpenXJsonSerDe | None = None


@dataclass
class DestinationTableConfiguration(PropertyType):
    destination_database_name: str | None = None
    destination_table_name: str | None = None
    partition_spec: PartitionSpec | None = None
    s3_error_output_prefix: str | None = None
    unique_keys: list[String] = field(default_factory=list)


@dataclass
class DirectPutSourceConfiguration(PropertyType):
    throughput_hint_in_m_bs: int | None = None


@dataclass
class DocumentIdOptions(PropertyType):
    default_document_id_format: str | None = None


@dataclass
class DynamicPartitioningConfiguration(PropertyType):
    enabled: bool | None = None
    retry_options: RetryOptions | None = None


@dataclass
class ElasticsearchBufferingHints(PropertyType):
    interval_in_seconds: int | None = None
    size_in_m_bs: int | None = None


@dataclass
class ElasticsearchDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_arn": "DomainARN",
        "role_arn": "RoleARN",
    }

    index_name: str | None = None
    role_arn: str | None = None
    s3_configuration: S3DestinationConfiguration | None = None
    buffering_hints: ElasticsearchBufferingHints | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    cluster_endpoint: str | None = None
    document_id_options: DocumentIdOptions | None = None
    domain_arn: str | None = None
    index_rotation_period: str | None = None
    processing_configuration: ProcessingConfiguration | None = None
    retry_options: ElasticsearchRetryOptions | None = None
    s3_backup_mode: str | None = None
    type_name: str | None = None
    vpc_configuration: VpcConfiguration | None = None


@dataclass
class ElasticsearchRetryOptions(PropertyType):
    duration_in_seconds: int | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_encryption_config": "KMSEncryptionConfig",
    }

    kms_encryption_config: KMSEncryptionConfig | None = None
    no_encryption_config: str | None = None


@dataclass
class ExtendedS3DestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
        "role_arn": "RoleARN",
    }

    bucket_arn: str | None = None
    role_arn: str | None = None
    buffering_hints: BufferingHints | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    compression_format: str | None = None
    custom_time_zone: str | None = None
    data_format_conversion_configuration: DataFormatConversionConfiguration | None = (
        None
    )
    dynamic_partitioning_configuration: DynamicPartitioningConfiguration | None = None
    encryption_configuration: EncryptionConfiguration | None = None
    error_output_prefix: str | None = None
    file_extension: str | None = None
    prefix: str | None = None
    processing_configuration: ProcessingConfiguration | None = None
    s3_backup_configuration: S3DestinationConfiguration | None = None
    s3_backup_mode: str | None = None


@dataclass
class HiveJsonSerDe(PropertyType):
    timestamp_formats: list[String] = field(default_factory=list)


@dataclass
class HttpEndpointCommonAttribute(PropertyType):
    attribute_name: str | None = None
    attribute_value: str | None = None


@dataclass
class HttpEndpointConfiguration(PropertyType):
    url: str | None = None
    access_key: str | None = None
    name: str | None = None


@dataclass
class HttpEndpointDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    endpoint_configuration: HttpEndpointConfiguration | None = None
    s3_configuration: S3DestinationConfiguration | None = None
    buffering_hints: BufferingHints | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    processing_configuration: ProcessingConfiguration | None = None
    request_configuration: HttpEndpointRequestConfiguration | None = None
    retry_options: RetryOptions | None = None
    role_arn: str | None = None
    s3_backup_mode: str | None = None
    secrets_manager_configuration: SecretsManagerConfiguration | None = None


@dataclass
class HttpEndpointRequestConfiguration(PropertyType):
    common_attributes: list[HttpEndpointCommonAttribute] = field(default_factory=list)
    content_encoding: str | None = None


@dataclass
class IcebergDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
        "s3_backup_mode": "s3BackupMode",
    }

    catalog_configuration: CatalogConfiguration | None = None
    role_arn: str | None = None
    s3_configuration: S3DestinationConfiguration | None = None
    append_only: bool | None = None
    buffering_hints: BufferingHints | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    destination_table_configuration_list: list[DestinationTableConfiguration] = field(
        default_factory=list
    )
    processing_configuration: ProcessingConfiguration | None = None
    retry_options: RetryOptions | None = None
    s3_backup_mode: str | None = None
    schema_evolution_configuration: SchemaEvolutionConfiguration | None = None
    table_creation_configuration: TableCreationConfiguration | None = None


@dataclass
class InputFormatConfiguration(PropertyType):
    deserializer: Deserializer | None = None


@dataclass
class KMSEncryptionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "awskms_key_arn": "AWSKMSKeyARN",
    }

    awskms_key_arn: str | None = None


@dataclass
class KinesisStreamSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kinesis_stream_arn": "KinesisStreamARN",
        "role_arn": "RoleARN",
    }

    kinesis_stream_arn: str | None = None
    role_arn: str | None = None


@dataclass
class MSKSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "msk_cluster_arn": "MSKClusterARN",
    }

    authentication_configuration: AuthenticationConfiguration | None = None
    msk_cluster_arn: str | None = None
    topic_name: str | None = None
    read_from_timestamp: str | None = None


@dataclass
class OpenXJsonSerDe(PropertyType):
    case_insensitive: bool | None = None
    column_to_json_key_mappings: dict[str, String] = field(default_factory=dict)
    convert_dots_in_json_keys_to_underscores: bool | None = None


@dataclass
class OrcSerDe(PropertyType):
    block_size_bytes: int | None = None
    bloom_filter_columns: list[String] = field(default_factory=list)
    bloom_filter_false_positive_probability: float | None = None
    compression: str | None = None
    dictionary_key_threshold: float | None = None
    enable_padding: bool | None = None
    format_version: str | None = None
    padding_tolerance: float | None = None
    row_index_stride: int | None = None
    stripe_size_bytes: int | None = None


@dataclass
class OutputFormatConfiguration(PropertyType):
    serializer: Serializer | None = None


@dataclass
class ParquetSerDe(PropertyType):
    block_size_bytes: int | None = None
    compression: str | None = None
    enable_dictionary_compression: bool | None = None
    max_padding_bytes: int | None = None
    page_size_bytes: int | None = None
    writer_version: str | None = None


@dataclass
class PartitionField(PropertyType):
    source_name: str | None = None


@dataclass
class PartitionSpec(PropertyType):
    identity: list[PartitionField] = field(default_factory=list)


@dataclass
class ProcessingConfiguration(PropertyType):
    enabled: bool | None = None
    processors: list[Processor] = field(default_factory=list)


@dataclass
class Processor(PropertyType):
    type_: str | None = None
    parameters: list[ProcessorParameter] = field(default_factory=list)


@dataclass
class ProcessorParameter(PropertyType):
    parameter_name: str | None = None
    parameter_value: str | None = None


@dataclass
class RedshiftDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_jdbcurl": "ClusterJDBCURL",
        "role_arn": "RoleARN",
    }

    cluster_jdbcurl: str | None = None
    copy_command: CopyCommand | None = None
    role_arn: str | None = None
    s3_configuration: S3DestinationConfiguration | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    password: str | None = None
    processing_configuration: ProcessingConfiguration | None = None
    retry_options: RedshiftRetryOptions | None = None
    s3_backup_configuration: S3DestinationConfiguration | None = None
    s3_backup_mode: str | None = None
    secrets_manager_configuration: SecretsManagerConfiguration | None = None
    username: str | None = None


@dataclass
class RedshiftRetryOptions(PropertyType):
    duration_in_seconds: int | None = None


@dataclass
class RetryOptions(PropertyType):
    duration_in_seconds: int | None = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
        "role_arn": "RoleARN",
    }

    bucket_arn: str | None = None
    role_arn: str | None = None
    buffering_hints: BufferingHints | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    compression_format: str | None = None
    encryption_configuration: EncryptionConfiguration | None = None
    error_output_prefix: str | None = None
    prefix: str | None = None


@dataclass
class SchemaConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    catalog_id: str | None = None
    database_name: str | None = None
    region: str | None = None
    role_arn: str | None = None
    table_name: str | None = None
    version_id: str | None = None


@dataclass
class SchemaEvolutionConfiguration(PropertyType):
    enabled: bool | None = None


@dataclass
class SecretsManagerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
        "secret_arn": "SecretARN",
    }

    enabled: bool | None = None
    role_arn: str | None = None
    secret_arn: str | None = None


@dataclass
class Serializer(PropertyType):
    orc_ser_de: OrcSerDe | None = None
    parquet_ser_de: ParquetSerDe | None = None


@dataclass
class SnowflakeBufferingHints(PropertyType):
    interval_in_seconds: int | None = None
    size_in_m_bs: int | None = None


@dataclass
class SnowflakeDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    account_url: str | None = None
    database: str | None = None
    role_arn: str | None = None
    s3_configuration: S3DestinationConfiguration | None = None
    schema: str | None = None
    table: str | None = None
    buffering_hints: SnowflakeBufferingHints | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    content_column_name: str | None = None
    data_loading_option: str | None = None
    key_passphrase: str | None = None
    meta_data_column_name: str | None = None
    private_key: str | None = None
    processing_configuration: ProcessingConfiguration | None = None
    retry_options: SnowflakeRetryOptions | None = None
    s3_backup_mode: str | None = None
    secrets_manager_configuration: SecretsManagerConfiguration | None = None
    snowflake_role_configuration: SnowflakeRoleConfiguration | None = None
    snowflake_vpc_configuration: SnowflakeVpcConfiguration | None = None
    user: str | None = None


@dataclass
class SnowflakeRetryOptions(PropertyType):
    duration_in_seconds: int | None = None


@dataclass
class SnowflakeRoleConfiguration(PropertyType):
    enabled: bool | None = None
    snowflake_role: str | None = None


@dataclass
class SnowflakeVpcConfiguration(PropertyType):
    private_link_vpce_id: str | None = None


@dataclass
class SplunkBufferingHints(PropertyType):
    interval_in_seconds: int | None = None
    size_in_m_bs: int | None = None


@dataclass
class SplunkDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hec_acknowledgment_timeout_in_seconds": "HECAcknowledgmentTimeoutInSeconds",
        "hec_endpoint": "HECEndpoint",
        "hec_endpoint_type": "HECEndpointType",
        "hec_token": "HECToken",
    }

    hec_endpoint: str | None = None
    hec_endpoint_type: str | None = None
    s3_configuration: S3DestinationConfiguration | None = None
    buffering_hints: SplunkBufferingHints | None = None
    cloud_watch_logging_options: CloudWatchLoggingOptions | None = None
    hec_acknowledgment_timeout_in_seconds: int | None = None
    hec_token: str | None = None
    processing_configuration: ProcessingConfiguration | None = None
    retry_options: SplunkRetryOptions | None = None
    s3_backup_mode: str | None = None
    secrets_manager_configuration: SecretsManagerConfiguration | None = None


@dataclass
class SplunkRetryOptions(PropertyType):
    duration_in_seconds: int | None = None


@dataclass
class TableCreationConfiguration(PropertyType):
    enabled: bool | None = None


@dataclass
class VpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    role_arn: str | None = None
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
