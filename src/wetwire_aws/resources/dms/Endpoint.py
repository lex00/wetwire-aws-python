"""PropertyTypes for AWS::DMS::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DocDbSettings(PropertyType):
    docs_to_investigate: DslValue[int] | None = None
    extract_doc_id: DslValue[bool] | None = None
    nesting_level: DslValue[str] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None


@dataclass
class DynamoDbSettings(PropertyType):
    service_access_role_arn: DslValue[str] | None = None


@dataclass
class ElasticsearchSettings(PropertyType):
    endpoint_uri: DslValue[str] | None = None
    error_retry_duration: DslValue[int] | None = None
    full_load_error_percentage: DslValue[int] | None = None
    service_access_role_arn: DslValue[str] | None = None


@dataclass
class GcpMySQLSettings(PropertyType):
    after_connect_script: DslValue[str] | None = None
    clean_source_metadata_on_mismatch: DslValue[bool] | None = None
    database_name: DslValue[str] | None = None
    events_poll_interval: DslValue[int] | None = None
    max_file_size: DslValue[int] | None = None
    parallel_load_threads: DslValue[int] | None = None
    password: DslValue[str] | None = None
    port: DslValue[int] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None
    server_name: DslValue[str] | None = None
    server_timezone: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class IbmDb2Settings(PropertyType):
    current_lsn: DslValue[str] | None = None
    keep_csv_files: DslValue[bool] | None = None
    load_timeout: DslValue[int] | None = None
    max_file_size: DslValue[int] | None = None
    max_k_bytes_per_read: DslValue[int] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None
    set_data_capture_changes: DslValue[bool] | None = None
    write_buffer_size: DslValue[int] | None = None


@dataclass
class KafkaSettings(PropertyType):
    broker: DslValue[str] | None = None
    include_control_details: DslValue[bool] | None = None
    include_null_and_empty: DslValue[bool] | None = None
    include_partition_value: DslValue[bool] | None = None
    include_table_alter_operations: DslValue[bool] | None = None
    include_transaction_details: DslValue[bool] | None = None
    message_format: DslValue[str] | None = None
    message_max_bytes: DslValue[int] | None = None
    no_hex_prefix: DslValue[bool] | None = None
    partition_include_schema_table: DslValue[bool] | None = None
    sasl_password: DslValue[str] | None = None
    sasl_user_name: DslValue[str] | None = None
    security_protocol: DslValue[str] | None = None
    ssl_ca_certificate_arn: DslValue[str] | None = None
    ssl_client_certificate_arn: DslValue[str] | None = None
    ssl_client_key_arn: DslValue[str] | None = None
    ssl_client_key_password: DslValue[str] | None = None
    topic: DslValue[str] | None = None


@dataclass
class KinesisSettings(PropertyType):
    include_control_details: DslValue[bool] | None = None
    include_null_and_empty: DslValue[bool] | None = None
    include_partition_value: DslValue[bool] | None = None
    include_table_alter_operations: DslValue[bool] | None = None
    include_transaction_details: DslValue[bool] | None = None
    message_format: DslValue[str] | None = None
    no_hex_prefix: DslValue[bool] | None = None
    partition_include_schema_table: DslValue[bool] | None = None
    service_access_role_arn: DslValue[str] | None = None
    stream_arn: DslValue[str] | None = None


@dataclass
class MicrosoftSqlServerSettings(PropertyType):
    bcp_packet_size: DslValue[int] | None = None
    control_tables_file_group: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    force_lob_lookup: DslValue[bool] | None = None
    password: DslValue[str] | None = None
    port: DslValue[int] | None = None
    query_single_always_on_node: DslValue[bool] | None = None
    read_backup_only: DslValue[bool] | None = None
    safeguard_policy: DslValue[str] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None
    server_name: DslValue[str] | None = None
    tlog_access_mode: DslValue[str] | None = None
    trim_space_in_char: DslValue[bool] | None = None
    use_bcp_full_load: DslValue[bool] | None = None
    use_third_party_backup_device: DslValue[bool] | None = None
    username: DslValue[str] | None = None


@dataclass
class MongoDbSettings(PropertyType):
    auth_mechanism: DslValue[str] | None = None
    auth_source: DslValue[str] | None = None
    auth_type: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    docs_to_investigate: DslValue[str] | None = None
    extract_doc_id: DslValue[str] | None = None
    nesting_level: DslValue[str] | None = None
    password: DslValue[str] | None = None
    port: DslValue[int] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None
    server_name: DslValue[str] | None = None
    username: DslValue[str] | None = None


@dataclass
class MySqlSettings(PropertyType):
    after_connect_script: DslValue[str] | None = None
    clean_source_metadata_on_mismatch: DslValue[bool] | None = None
    events_poll_interval: DslValue[int] | None = None
    max_file_size: DslValue[int] | None = None
    parallel_load_threads: DslValue[int] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None
    server_timezone: DslValue[str] | None = None
    target_db_type: DslValue[str] | None = None


@dataclass
class NeptuneSettings(PropertyType):
    error_retry_duration: DslValue[int] | None = None
    iam_auth_enabled: DslValue[bool] | None = None
    max_file_size: DslValue[int] | None = None
    max_retry_count: DslValue[int] | None = None
    s3_bucket_folder: DslValue[str] | None = None
    s3_bucket_name: DslValue[str] | None = None
    service_access_role_arn: DslValue[str] | None = None


@dataclass
class OracleSettings(PropertyType):
    access_alternate_directly: DslValue[bool] | None = None
    add_supplemental_logging: DslValue[bool] | None = None
    additional_archived_log_dest_id: DslValue[int] | None = None
    allow_select_nested_tables: DslValue[bool] | None = None
    archived_log_dest_id: DslValue[int] | None = None
    archived_logs_only: DslValue[bool] | None = None
    asm_password: DslValue[str] | None = None
    asm_server: DslValue[str] | None = None
    asm_user: DslValue[str] | None = None
    char_length_semantics: DslValue[str] | None = None
    direct_path_no_log: DslValue[bool] | None = None
    direct_path_parallel_load: DslValue[bool] | None = None
    enable_homogenous_tablespace: DslValue[bool] | None = None
    extra_archived_log_dest_ids: list[DslValue[int]] = field(default_factory=list)
    fail_tasks_on_lob_truncation: DslValue[bool] | None = None
    number_datatype_scale: DslValue[int] | None = None
    oracle_path_prefix: DslValue[str] | None = None
    parallel_asm_read_threads: DslValue[int] | None = None
    read_ahead_blocks: DslValue[int] | None = None
    read_table_space_name: DslValue[bool] | None = None
    replace_path_prefix: DslValue[bool] | None = None
    retry_interval: DslValue[int] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_oracle_asm_access_role_arn: DslValue[str] | None = None
    secrets_manager_oracle_asm_secret_id: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None
    security_db_encryption: DslValue[str] | None = None
    security_db_encryption_name: DslValue[str] | None = None
    spatial_data_option_to_geo_json_function_name: DslValue[str] | None = None
    standby_delay_time: DslValue[int] | None = None
    use_alternate_folder_for_online: DslValue[bool] | None = None
    use_b_file: DslValue[bool] | None = None
    use_direct_path_full_load: DslValue[bool] | None = None
    use_logminer_reader: DslValue[bool] | None = None
    use_path_prefix: DslValue[str] | None = None


@dataclass
class PostgreSqlSettings(PropertyType):
    after_connect_script: DslValue[str] | None = None
    babelfish_database_name: DslValue[str] | None = None
    capture_ddls: DslValue[bool] | None = None
    database_mode: DslValue[str] | None = None
    ddl_artifacts_schema: DslValue[str] | None = None
    execute_timeout: DslValue[int] | None = None
    fail_tasks_on_lob_truncation: DslValue[bool] | None = None
    heartbeat_enable: DslValue[bool] | None = None
    heartbeat_frequency: DslValue[int] | None = None
    heartbeat_schema: DslValue[str] | None = None
    map_boolean_as_boolean: DslValue[bool] | None = None
    max_file_size: DslValue[int] | None = None
    plugin_name: DslValue[str] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None
    slot_name: DslValue[str] | None = None


@dataclass
class RedisSettings(PropertyType):
    auth_password: DslValue[str] | None = None
    auth_type: DslValue[str] | None = None
    auth_user_name: DslValue[str] | None = None
    port: DslValue[float] | None = None
    server_name: DslValue[str] | None = None
    ssl_ca_certificate_arn: DslValue[str] | None = None
    ssl_security_protocol: DslValue[str] | None = None


@dataclass
class RedshiftSettings(PropertyType):
    accept_any_date: DslValue[bool] | None = None
    after_connect_script: DslValue[str] | None = None
    bucket_folder: DslValue[str] | None = None
    bucket_name: DslValue[str] | None = None
    case_sensitive_names: DslValue[bool] | None = None
    comp_update: DslValue[bool] | None = None
    connection_timeout: DslValue[int] | None = None
    date_format: DslValue[str] | None = None
    empty_as_null: DslValue[bool] | None = None
    encryption_mode: DslValue[str] | None = None
    explicit_ids: DslValue[bool] | None = None
    file_transfer_upload_streams: DslValue[int] | None = None
    load_timeout: DslValue[int] | None = None
    map_boolean_as_boolean: DslValue[bool] | None = None
    max_file_size: DslValue[int] | None = None
    remove_quotes: DslValue[bool] | None = None
    replace_chars: DslValue[str] | None = None
    replace_invalid_chars: DslValue[str] | None = None
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None
    server_side_encryption_kms_key_id: DslValue[str] | None = None
    service_access_role_arn: DslValue[str] | None = None
    time_format: DslValue[str] | None = None
    trim_blanks: DslValue[bool] | None = None
    truncate_columns: DslValue[bool] | None = None
    write_buffer_size: DslValue[int] | None = None


@dataclass
class S3Settings(PropertyType):
    add_column_name: DslValue[bool] | None = None
    add_trailing_padding_character: DslValue[bool] | None = None
    bucket_folder: DslValue[str] | None = None
    bucket_name: DslValue[str] | None = None
    canned_acl_for_objects: DslValue[str] | None = None
    cdc_inserts_and_updates: DslValue[bool] | None = None
    cdc_inserts_only: DslValue[bool] | None = None
    cdc_max_batch_interval: DslValue[int] | None = None
    cdc_min_file_size: DslValue[int] | None = None
    cdc_path: DslValue[str] | None = None
    compression_type: DslValue[str] | None = None
    csv_delimiter: DslValue[str] | None = None
    csv_no_sup_value: DslValue[str] | None = None
    csv_null_value: DslValue[str] | None = None
    csv_row_delimiter: DslValue[str] | None = None
    data_format: DslValue[str] | None = None
    data_page_size: DslValue[int] | None = None
    date_partition_delimiter: DslValue[str] | None = None
    date_partition_enabled: DslValue[bool] | None = None
    date_partition_sequence: DslValue[str] | None = None
    date_partition_timezone: DslValue[str] | None = None
    dict_page_size_limit: DslValue[int] | None = None
    enable_statistics: DslValue[bool] | None = None
    encoding_type: DslValue[str] | None = None
    encryption_mode: DslValue[str] | None = None
    expected_bucket_owner: DslValue[str] | None = None
    external_table_definition: DslValue[str] | None = None
    glue_catalog_generation: DslValue[bool] | None = None
    ignore_header_rows: DslValue[int] | None = None
    include_op_for_full_load: DslValue[bool] | None = None
    max_file_size: DslValue[int] | None = None
    parquet_timestamp_in_millisecond: DslValue[bool] | None = None
    parquet_version: DslValue[str] | None = None
    preserve_transactions: DslValue[bool] | None = None
    rfc4180: DslValue[bool] | None = None
    row_group_length: DslValue[int] | None = None
    server_side_encryption_kms_key_id: DslValue[str] | None = None
    service_access_role_arn: DslValue[str] | None = None
    timestamp_column_name: DslValue[str] | None = None
    use_csv_no_sup_value: DslValue[bool] | None = None
    use_task_start_time_for_full_load_timestamp: DslValue[bool] | None = None


@dataclass
class SybaseSettings(PropertyType):
    secrets_manager_access_role_arn: DslValue[str] | None = None
    secrets_manager_secret_id: DslValue[str] | None = None
