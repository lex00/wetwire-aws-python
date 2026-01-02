"""PropertyTypes for AWS::DMS::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DocDbSettings(PropertyType):
    docs_to_investigate: int | None = None
    extract_doc_id: bool | None = None
    nesting_level: str | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None


@dataclass
class DynamoDbSettings(PropertyType):
    service_access_role_arn: str | None = None


@dataclass
class ElasticsearchSettings(PropertyType):
    endpoint_uri: str | None = None
    error_retry_duration: int | None = None
    full_load_error_percentage: int | None = None
    service_access_role_arn: str | None = None


@dataclass
class GcpMySQLSettings(PropertyType):
    after_connect_script: str | None = None
    clean_source_metadata_on_mismatch: bool | None = None
    database_name: str | None = None
    events_poll_interval: int | None = None
    max_file_size: int | None = None
    parallel_load_threads: int | None = None
    password: str | None = None
    port: int | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None
    server_name: str | None = None
    server_timezone: str | None = None
    username: str | None = None


@dataclass
class IbmDb2Settings(PropertyType):
    current_lsn: str | None = None
    keep_csv_files: bool | None = None
    load_timeout: int | None = None
    max_file_size: int | None = None
    max_k_bytes_per_read: int | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None
    set_data_capture_changes: bool | None = None
    write_buffer_size: int | None = None


@dataclass
class KafkaSettings(PropertyType):
    broker: str | None = None
    include_control_details: bool | None = None
    include_null_and_empty: bool | None = None
    include_partition_value: bool | None = None
    include_table_alter_operations: bool | None = None
    include_transaction_details: bool | None = None
    message_format: str | None = None
    message_max_bytes: int | None = None
    no_hex_prefix: bool | None = None
    partition_include_schema_table: bool | None = None
    sasl_password: str | None = None
    sasl_user_name: str | None = None
    security_protocol: str | None = None
    ssl_ca_certificate_arn: str | None = None
    ssl_client_certificate_arn: str | None = None
    ssl_client_key_arn: str | None = None
    ssl_client_key_password: str | None = None
    topic: str | None = None


@dataclass
class KinesisSettings(PropertyType):
    include_control_details: bool | None = None
    include_null_and_empty: bool | None = None
    include_partition_value: bool | None = None
    include_table_alter_operations: bool | None = None
    include_transaction_details: bool | None = None
    message_format: str | None = None
    no_hex_prefix: bool | None = None
    partition_include_schema_table: bool | None = None
    service_access_role_arn: str | None = None
    stream_arn: str | None = None


@dataclass
class MicrosoftSqlServerSettings(PropertyType):
    bcp_packet_size: int | None = None
    control_tables_file_group: str | None = None
    database_name: str | None = None
    force_lob_lookup: bool | None = None
    password: str | None = None
    port: int | None = None
    query_single_always_on_node: bool | None = None
    read_backup_only: bool | None = None
    safeguard_policy: str | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None
    server_name: str | None = None
    tlog_access_mode: str | None = None
    trim_space_in_char: bool | None = None
    use_bcp_full_load: bool | None = None
    use_third_party_backup_device: bool | None = None
    username: str | None = None


@dataclass
class MongoDbSettings(PropertyType):
    auth_mechanism: str | None = None
    auth_source: str | None = None
    auth_type: str | None = None
    database_name: str | None = None
    docs_to_investigate: str | None = None
    extract_doc_id: str | None = None
    nesting_level: str | None = None
    password: str | None = None
    port: int | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None
    server_name: str | None = None
    username: str | None = None


@dataclass
class MySqlSettings(PropertyType):
    after_connect_script: str | None = None
    clean_source_metadata_on_mismatch: bool | None = None
    events_poll_interval: int | None = None
    max_file_size: int | None = None
    parallel_load_threads: int | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None
    server_timezone: str | None = None
    target_db_type: str | None = None


@dataclass
class NeptuneSettings(PropertyType):
    error_retry_duration: int | None = None
    iam_auth_enabled: bool | None = None
    max_file_size: int | None = None
    max_retry_count: int | None = None
    s3_bucket_folder: str | None = None
    s3_bucket_name: str | None = None
    service_access_role_arn: str | None = None


@dataclass
class OracleSettings(PropertyType):
    access_alternate_directly: bool | None = None
    add_supplemental_logging: bool | None = None
    additional_archived_log_dest_id: int | None = None
    allow_select_nested_tables: bool | None = None
    archived_log_dest_id: int | None = None
    archived_logs_only: bool | None = None
    asm_password: str | None = None
    asm_server: str | None = None
    asm_user: str | None = None
    char_length_semantics: str | None = None
    direct_path_no_log: bool | None = None
    direct_path_parallel_load: bool | None = None
    enable_homogenous_tablespace: bool | None = None
    extra_archived_log_dest_ids: list[Integer] = field(default_factory=list)
    fail_tasks_on_lob_truncation: bool | None = None
    number_datatype_scale: int | None = None
    oracle_path_prefix: str | None = None
    parallel_asm_read_threads: int | None = None
    read_ahead_blocks: int | None = None
    read_table_space_name: bool | None = None
    replace_path_prefix: bool | None = None
    retry_interval: int | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_oracle_asm_access_role_arn: str | None = None
    secrets_manager_oracle_asm_secret_id: str | None = None
    secrets_manager_secret_id: str | None = None
    security_db_encryption: str | None = None
    security_db_encryption_name: str | None = None
    spatial_data_option_to_geo_json_function_name: str | None = None
    standby_delay_time: int | None = None
    use_alternate_folder_for_online: bool | None = None
    use_b_file: bool | None = None
    use_direct_path_full_load: bool | None = None
    use_logminer_reader: bool | None = None
    use_path_prefix: str | None = None


@dataclass
class PostgreSqlSettings(PropertyType):
    after_connect_script: str | None = None
    babelfish_database_name: str | None = None
    capture_ddls: bool | None = None
    database_mode: str | None = None
    ddl_artifacts_schema: str | None = None
    execute_timeout: int | None = None
    fail_tasks_on_lob_truncation: bool | None = None
    heartbeat_enable: bool | None = None
    heartbeat_frequency: int | None = None
    heartbeat_schema: str | None = None
    map_boolean_as_boolean: bool | None = None
    max_file_size: int | None = None
    plugin_name: str | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None
    slot_name: str | None = None


@dataclass
class RedisSettings(PropertyType):
    auth_password: str | None = None
    auth_type: str | None = None
    auth_user_name: str | None = None
    port: float | None = None
    server_name: str | None = None
    ssl_ca_certificate_arn: str | None = None
    ssl_security_protocol: str | None = None


@dataclass
class RedshiftSettings(PropertyType):
    accept_any_date: bool | None = None
    after_connect_script: str | None = None
    bucket_folder: str | None = None
    bucket_name: str | None = None
    case_sensitive_names: bool | None = None
    comp_update: bool | None = None
    connection_timeout: int | None = None
    date_format: str | None = None
    empty_as_null: bool | None = None
    encryption_mode: str | None = None
    explicit_ids: bool | None = None
    file_transfer_upload_streams: int | None = None
    load_timeout: int | None = None
    map_boolean_as_boolean: bool | None = None
    max_file_size: int | None = None
    remove_quotes: bool | None = None
    replace_chars: str | None = None
    replace_invalid_chars: str | None = None
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None
    server_side_encryption_kms_key_id: str | None = None
    service_access_role_arn: str | None = None
    time_format: str | None = None
    trim_blanks: bool | None = None
    truncate_columns: bool | None = None
    write_buffer_size: int | None = None


@dataclass
class S3Settings(PropertyType):
    add_column_name: bool | None = None
    add_trailing_padding_character: bool | None = None
    bucket_folder: str | None = None
    bucket_name: str | None = None
    canned_acl_for_objects: str | None = None
    cdc_inserts_and_updates: bool | None = None
    cdc_inserts_only: bool | None = None
    cdc_max_batch_interval: int | None = None
    cdc_min_file_size: int | None = None
    cdc_path: str | None = None
    compression_type: str | None = None
    csv_delimiter: str | None = None
    csv_no_sup_value: str | None = None
    csv_null_value: str | None = None
    csv_row_delimiter: str | None = None
    data_format: str | None = None
    data_page_size: int | None = None
    date_partition_delimiter: str | None = None
    date_partition_enabled: bool | None = None
    date_partition_sequence: str | None = None
    date_partition_timezone: str | None = None
    dict_page_size_limit: int | None = None
    enable_statistics: bool | None = None
    encoding_type: str | None = None
    encryption_mode: str | None = None
    expected_bucket_owner: str | None = None
    external_table_definition: str | None = None
    glue_catalog_generation: bool | None = None
    ignore_header_rows: int | None = None
    include_op_for_full_load: bool | None = None
    max_file_size: int | None = None
    parquet_timestamp_in_millisecond: bool | None = None
    parquet_version: str | None = None
    preserve_transactions: bool | None = None
    rfc4180: bool | None = None
    row_group_length: int | None = None
    server_side_encryption_kms_key_id: str | None = None
    service_access_role_arn: str | None = None
    timestamp_column_name: str | None = None
    use_csv_no_sup_value: bool | None = None
    use_task_start_time_for_full_load_timestamp: bool | None = None


@dataclass
class SybaseSettings(PropertyType):
    secrets_manager_access_role_arn: str | None = None
    secrets_manager_secret_id: str | None = None
