"""PropertyTypes for AWS::KinesisFirehose::DeliveryStream."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AmazonOpenSearchServerlessBufferingHints(PropertyType):
    interval_in_seconds: DslValue[int] | None = None
    size_in_m_bs: DslValue[int] | None = None


@dataclass
class AmazonOpenSearchServerlessDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    index_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    s3_configuration: DslValue[S3DestinationConfiguration] | None = None
    buffering_hints: DslValue[AmazonOpenSearchServerlessBufferingHints] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    collection_endpoint: DslValue[str] | None = None
    processing_configuration: DslValue[ProcessingConfiguration] | None = None
    retry_options: DslValue[AmazonOpenSearchServerlessRetryOptions] | None = None
    s3_backup_mode: DslValue[str] | None = None
    vpc_configuration: DslValue[VpcConfiguration] | None = None


@dataclass
class AmazonOpenSearchServerlessRetryOptions(PropertyType):
    duration_in_seconds: DslValue[int] | None = None


@dataclass
class AmazonopensearchserviceBufferingHints(PropertyType):
    interval_in_seconds: DslValue[int] | None = None
    size_in_m_bs: DslValue[int] | None = None


@dataclass
class AmazonopensearchserviceDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_arn": "DomainARN",
        "role_arn": "RoleARN",
    }

    index_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    s3_configuration: DslValue[S3DestinationConfiguration] | None = None
    buffering_hints: DslValue[AmazonopensearchserviceBufferingHints] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    cluster_endpoint: DslValue[str] | None = None
    document_id_options: DslValue[DocumentIdOptions] | None = None
    domain_arn: DslValue[str] | None = None
    index_rotation_period: DslValue[str] | None = None
    processing_configuration: DslValue[ProcessingConfiguration] | None = None
    retry_options: DslValue[AmazonopensearchserviceRetryOptions] | None = None
    s3_backup_mode: DslValue[str] | None = None
    type_name: DslValue[str] | None = None
    vpc_configuration: DslValue[VpcConfiguration] | None = None


@dataclass
class AmazonopensearchserviceRetryOptions(PropertyType):
    duration_in_seconds: DslValue[int] | None = None


@dataclass
class AuthenticationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    connectivity: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class BufferingHints(PropertyType):
    interval_in_seconds: DslValue[int] | None = None
    size_in_m_bs: DslValue[int] | None = None


@dataclass
class CatalogConfiguration(PropertyType):
    catalog_arn: DslValue[str] | None = None
    warehouse_location: DslValue[str] | None = None


@dataclass
class CloudWatchLoggingOptions(PropertyType):
    enabled: DslValue[bool] | None = None
    log_group_name: DslValue[str] | None = None
    log_stream_name: DslValue[str] | None = None


@dataclass
class CopyCommand(PropertyType):
    data_table_name: DslValue[str] | None = None
    copy_options: DslValue[str] | None = None
    data_table_columns: DslValue[str] | None = None


@dataclass
class DataFormatConversionConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    input_format_configuration: DslValue[InputFormatConfiguration] | None = None
    output_format_configuration: DslValue[OutputFormatConfiguration] | None = None
    schema_configuration: DslValue[SchemaConfiguration] | None = None


@dataclass
class DatabaseColumns(PropertyType):
    exclude: list[DslValue[str]] = field(default_factory=list)
    include: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DatabaseSourceAuthenticationConfiguration(PropertyType):
    secrets_manager_configuration: DslValue[SecretsManagerConfiguration] | None = None


@dataclass
class DatabaseSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "database_source_vpc_configuration": "DatabaseSourceVPCConfiguration",
        "ssl_mode": "SSLMode",
    }

    database_source_authentication_configuration: (
        DslValue[DatabaseSourceAuthenticationConfiguration] | None
    ) = None
    database_source_vpc_configuration: (
        DslValue[DatabaseSourceVPCConfiguration] | None
    ) = None
    databases: DslValue[Databases] | None = None
    endpoint: DslValue[str] | None = None
    port: DslValue[int] | None = None
    snapshot_watermark_table: DslValue[str] | None = None
    tables: DslValue[DatabaseTables] | None = None
    type_: DslValue[str] | None = None
    columns: DslValue[DatabaseColumns] | None = None
    digest: DslValue[str] | None = None
    public_certificate: DslValue[str] | None = None
    ssl_mode: DslValue[str] | None = None
    surrogate_keys: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DatabaseSourceVPCConfiguration(PropertyType):
    vpc_endpoint_service_name: DslValue[str] | None = None


@dataclass
class DatabaseTables(PropertyType):
    exclude: list[DslValue[str]] = field(default_factory=list)
    include: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Databases(PropertyType):
    exclude: list[DslValue[str]] = field(default_factory=list)
    include: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DeliveryStreamEncryptionConfigurationInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "key_arn": "KeyARN",
    }

    key_type: DslValue[str] | None = None
    key_arn: DslValue[str] | None = None


@dataclass
class Deserializer(PropertyType):
    hive_json_ser_de: DslValue[HiveJsonSerDe] | None = None
    open_x_json_ser_de: DslValue[OpenXJsonSerDe] | None = None


@dataclass
class DestinationTableConfiguration(PropertyType):
    destination_database_name: DslValue[str] | None = None
    destination_table_name: DslValue[str] | None = None
    partition_spec: DslValue[PartitionSpec] | None = None
    s3_error_output_prefix: DslValue[str] | None = None
    unique_keys: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DirectPutSourceConfiguration(PropertyType):
    throughput_hint_in_m_bs: DslValue[int] | None = None


@dataclass
class DocumentIdOptions(PropertyType):
    default_document_id_format: DslValue[str] | None = None


@dataclass
class DynamicPartitioningConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    retry_options: DslValue[RetryOptions] | None = None


@dataclass
class ElasticsearchBufferingHints(PropertyType):
    interval_in_seconds: DslValue[int] | None = None
    size_in_m_bs: DslValue[int] | None = None


@dataclass
class ElasticsearchDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "domain_arn": "DomainARN",
        "role_arn": "RoleARN",
    }

    index_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    s3_configuration: DslValue[S3DestinationConfiguration] | None = None
    buffering_hints: DslValue[ElasticsearchBufferingHints] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    cluster_endpoint: DslValue[str] | None = None
    document_id_options: DslValue[DocumentIdOptions] | None = None
    domain_arn: DslValue[str] | None = None
    index_rotation_period: DslValue[str] | None = None
    processing_configuration: DslValue[ProcessingConfiguration] | None = None
    retry_options: DslValue[ElasticsearchRetryOptions] | None = None
    s3_backup_mode: DslValue[str] | None = None
    type_name: DslValue[str] | None = None
    vpc_configuration: DslValue[VpcConfiguration] | None = None


@dataclass
class ElasticsearchRetryOptions(PropertyType):
    duration_in_seconds: DslValue[int] | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_encryption_config": "KMSEncryptionConfig",
    }

    kms_encryption_config: DslValue[KMSEncryptionConfig] | None = None
    no_encryption_config: DslValue[str] | None = None


@dataclass
class ExtendedS3DestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
        "role_arn": "RoleARN",
    }

    bucket_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    buffering_hints: DslValue[BufferingHints] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    compression_format: DslValue[str] | None = None
    custom_time_zone: DslValue[str] | None = None
    data_format_conversion_configuration: (
        DslValue[DataFormatConversionConfiguration] | None
    ) = None
    dynamic_partitioning_configuration: (
        DslValue[DynamicPartitioningConfiguration] | None
    ) = None
    encryption_configuration: DslValue[EncryptionConfiguration] | None = None
    error_output_prefix: DslValue[str] | None = None
    file_extension: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    processing_configuration: DslValue[ProcessingConfiguration] | None = None
    s3_backup_configuration: DslValue[S3DestinationConfiguration] | None = None
    s3_backup_mode: DslValue[str] | None = None


@dataclass
class HiveJsonSerDe(PropertyType):
    timestamp_formats: list[DslValue[str]] = field(default_factory=list)


@dataclass
class HttpEndpointCommonAttribute(PropertyType):
    attribute_name: DslValue[str] | None = None
    attribute_value: DslValue[str] | None = None


@dataclass
class HttpEndpointConfiguration(PropertyType):
    url: DslValue[str] | None = None
    access_key: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class HttpEndpointDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    endpoint_configuration: DslValue[HttpEndpointConfiguration] | None = None
    s3_configuration: DslValue[S3DestinationConfiguration] | None = None
    buffering_hints: DslValue[BufferingHints] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    processing_configuration: DslValue[ProcessingConfiguration] | None = None
    request_configuration: DslValue[HttpEndpointRequestConfiguration] | None = None
    retry_options: DslValue[RetryOptions] | None = None
    role_arn: DslValue[str] | None = None
    s3_backup_mode: DslValue[str] | None = None
    secrets_manager_configuration: DslValue[SecretsManagerConfiguration] | None = None


@dataclass
class HttpEndpointRequestConfiguration(PropertyType):
    common_attributes: list[DslValue[HttpEndpointCommonAttribute]] = field(
        default_factory=list
    )
    content_encoding: DslValue[str] | None = None


@dataclass
class IcebergDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
        "s3_backup_mode": "s3BackupMode",
    }

    catalog_configuration: DslValue[CatalogConfiguration] | None = None
    role_arn: DslValue[str] | None = None
    s3_configuration: DslValue[S3DestinationConfiguration] | None = None
    append_only: DslValue[bool] | None = None
    buffering_hints: DslValue[BufferingHints] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    destination_table_configuration_list: list[
        DslValue[DestinationTableConfiguration]
    ] = field(default_factory=list)
    processing_configuration: DslValue[ProcessingConfiguration] | None = None
    retry_options: DslValue[RetryOptions] | None = None
    s3_backup_mode: DslValue[str] | None = None
    schema_evolution_configuration: DslValue[SchemaEvolutionConfiguration] | None = None
    table_creation_configuration: DslValue[TableCreationConfiguration] | None = None


@dataclass
class InputFormatConfiguration(PropertyType):
    deserializer: DslValue[Deserializer] | None = None


@dataclass
class KMSEncryptionConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "awskms_key_arn": "AWSKMSKeyARN",
    }

    awskms_key_arn: DslValue[str] | None = None


@dataclass
class KinesisStreamSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kinesis_stream_arn": "KinesisStreamARN",
        "role_arn": "RoleARN",
    }

    kinesis_stream_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class MSKSourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "msk_cluster_arn": "MSKClusterARN",
    }

    authentication_configuration: DslValue[AuthenticationConfiguration] | None = None
    msk_cluster_arn: DslValue[str] | None = None
    topic_name: DslValue[str] | None = None
    read_from_timestamp: DslValue[str] | None = None


@dataclass
class OpenXJsonSerDe(PropertyType):
    case_insensitive: DslValue[bool] | None = None
    column_to_json_key_mappings: dict[str, DslValue[str]] = field(default_factory=dict)
    convert_dots_in_json_keys_to_underscores: DslValue[bool] | None = None


@dataclass
class OrcSerDe(PropertyType):
    block_size_bytes: DslValue[int] | None = None
    bloom_filter_columns: list[DslValue[str]] = field(default_factory=list)
    bloom_filter_false_positive_probability: DslValue[float] | None = None
    compression: DslValue[str] | None = None
    dictionary_key_threshold: DslValue[float] | None = None
    enable_padding: DslValue[bool] | None = None
    format_version: DslValue[str] | None = None
    padding_tolerance: DslValue[float] | None = None
    row_index_stride: DslValue[int] | None = None
    stripe_size_bytes: DslValue[int] | None = None


@dataclass
class OutputFormatConfiguration(PropertyType):
    serializer: DslValue[Serializer] | None = None


@dataclass
class ParquetSerDe(PropertyType):
    block_size_bytes: DslValue[int] | None = None
    compression: DslValue[str] | None = None
    enable_dictionary_compression: DslValue[bool] | None = None
    max_padding_bytes: DslValue[int] | None = None
    page_size_bytes: DslValue[int] | None = None
    writer_version: DslValue[str] | None = None


@dataclass
class PartitionField(PropertyType):
    source_name: DslValue[str] | None = None


@dataclass
class PartitionSpec(PropertyType):
    identity: list[DslValue[PartitionField]] = field(default_factory=list)


@dataclass
class ProcessingConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    processors: list[DslValue[Processor]] = field(default_factory=list)


@dataclass
class Processor(PropertyType):
    type_: DslValue[str] | None = None
    parameters: list[DslValue[ProcessorParameter]] = field(default_factory=list)


@dataclass
class ProcessorParameter(PropertyType):
    parameter_name: DslValue[str] | None = None
    parameter_value: DslValue[str] | None = None


@dataclass
class RedshiftDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cluster_jdbcurl": "ClusterJDBCURL",
        "role_arn": "RoleARN",
    }

    cluster_jdbcurl: DslValue[str] | None = None
    copy_command: DslValue[CopyCommand] | None = None
    role_arn: DslValue[str] | None = None
    s3_configuration: DslValue[S3DestinationConfiguration] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    password: DslValue[str] | None = None
    processing_configuration: DslValue[ProcessingConfiguration] | None = None
    retry_options: DslValue[RedshiftRetryOptions] | None = None
    s3_backup_configuration: DslValue[S3DestinationConfiguration] | None = None
    s3_backup_mode: DslValue[str] | None = None
    secrets_manager_configuration: DslValue[SecretsManagerConfiguration] | None = None
    username: DslValue[str] | None = None


@dataclass
class RedshiftRetryOptions(PropertyType):
    duration_in_seconds: DslValue[int] | None = None


@dataclass
class RetryOptions(PropertyType):
    duration_in_seconds: DslValue[int] | None = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
        "role_arn": "RoleARN",
    }

    bucket_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    buffering_hints: DslValue[BufferingHints] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    compression_format: DslValue[str] | None = None
    encryption_configuration: DslValue[EncryptionConfiguration] | None = None
    error_output_prefix: DslValue[str] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class SchemaConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    catalog_id: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    region: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    version_id: DslValue[str] | None = None


@dataclass
class SchemaEvolutionConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class SecretsManagerConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
        "secret_arn": "SecretARN",
    }

    enabled: DslValue[bool] | None = None
    role_arn: DslValue[str] | None = None
    secret_arn: DslValue[str] | None = None


@dataclass
class Serializer(PropertyType):
    orc_ser_de: DslValue[OrcSerDe] | None = None
    parquet_ser_de: DslValue[ParquetSerDe] | None = None


@dataclass
class SnowflakeBufferingHints(PropertyType):
    interval_in_seconds: DslValue[int] | None = None
    size_in_m_bs: DslValue[int] | None = None


@dataclass
class SnowflakeDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    account_url: DslValue[str] | None = None
    database: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    s3_configuration: DslValue[S3DestinationConfiguration] | None = None
    schema: DslValue[str] | None = None
    table: DslValue[str] | None = None
    buffering_hints: DslValue[SnowflakeBufferingHints] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    content_column_name: DslValue[str] | None = None
    data_loading_option: DslValue[str] | None = None
    key_passphrase: DslValue[str] | None = None
    meta_data_column_name: DslValue[str] | None = None
    private_key: DslValue[str] | None = None
    processing_configuration: DslValue[ProcessingConfiguration] | None = None
    retry_options: DslValue[SnowflakeRetryOptions] | None = None
    s3_backup_mode: DslValue[str] | None = None
    secrets_manager_configuration: DslValue[SecretsManagerConfiguration] | None = None
    snowflake_role_configuration: DslValue[SnowflakeRoleConfiguration] | None = None
    snowflake_vpc_configuration: DslValue[SnowflakeVpcConfiguration] | None = None
    user: DslValue[str] | None = None


@dataclass
class SnowflakeRetryOptions(PropertyType):
    duration_in_seconds: DslValue[int] | None = None


@dataclass
class SnowflakeRoleConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    snowflake_role: DslValue[str] | None = None


@dataclass
class SnowflakeVpcConfiguration(PropertyType):
    private_link_vpce_id: DslValue[str] | None = None


@dataclass
class SplunkBufferingHints(PropertyType):
    interval_in_seconds: DslValue[int] | None = None
    size_in_m_bs: DslValue[int] | None = None


@dataclass
class SplunkDestinationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "hec_acknowledgment_timeout_in_seconds": "HECAcknowledgmentTimeoutInSeconds",
        "hec_endpoint": "HECEndpoint",
        "hec_endpoint_type": "HECEndpointType",
        "hec_token": "HECToken",
    }

    hec_endpoint: DslValue[str] | None = None
    hec_endpoint_type: DslValue[str] | None = None
    s3_configuration: DslValue[S3DestinationConfiguration] | None = None
    buffering_hints: DslValue[SplunkBufferingHints] | None = None
    cloud_watch_logging_options: DslValue[CloudWatchLoggingOptions] | None = None
    hec_acknowledgment_timeout_in_seconds: DslValue[int] | None = None
    hec_token: DslValue[str] | None = None
    processing_configuration: DslValue[ProcessingConfiguration] | None = None
    retry_options: DslValue[SplunkRetryOptions] | None = None
    s3_backup_mode: DslValue[str] | None = None
    secrets_manager_configuration: DslValue[SecretsManagerConfiguration] | None = None


@dataclass
class SplunkRetryOptions(PropertyType):
    duration_in_seconds: DslValue[int] | None = None


@dataclass
class TableCreationConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class VpcConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "role_arn": "RoleARN",
    }

    role_arn: DslValue[str] | None = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
