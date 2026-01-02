"""PropertyTypes for AWS::AppFlow::Flow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AggregationConfig(PropertyType):
    aggregation_type: str | None = None
    target_file_size: int | None = None


@dataclass
class AmplitudeSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class ConnectorOperator(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    amplitude: str | None = None
    custom_connector: str | None = None
    datadog: str | None = None
    dynatrace: str | None = None
    google_analytics: str | None = None
    infor_nexus: str | None = None
    marketo: str | None = None
    pardot: str | None = None
    s3: str | None = None
    salesforce: str | None = None
    sapo_data: str | None = None
    service_now: str | None = None
    singular: str | None = None
    slack: str | None = None
    trendmicro: str | None = None
    veeva: str | None = None
    zendesk: str | None = None


@dataclass
class CustomConnectorDestinationProperties(PropertyType):
    entity_name: str | None = None
    custom_properties: dict[str, String] = field(default_factory=dict)
    error_handling_config: ErrorHandlingConfig | None = None
    id_field_names: list[String] = field(default_factory=list)
    write_operation_type: str | None = None


@dataclass
class CustomConnectorSourceProperties(PropertyType):
    entity_name: str | None = None
    custom_properties: dict[str, String] = field(default_factory=dict)
    data_transfer_api: DataTransferApi | None = None


@dataclass
class DataTransferApi(PropertyType):
    name: str | None = None
    type_: str | None = None


@dataclass
class DatadogSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class DestinationConnectorProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    custom_connector: CustomConnectorDestinationProperties | None = None
    event_bridge: EventBridgeDestinationProperties | None = None
    lookout_metrics: LookoutMetricsDestinationProperties | None = None
    marketo: MarketoDestinationProperties | None = None
    redshift: RedshiftDestinationProperties | None = None
    s3: S3DestinationProperties | None = None
    salesforce: SalesforceDestinationProperties | None = None
    sapo_data: SAPODataDestinationProperties | None = None
    snowflake: SnowflakeDestinationProperties | None = None
    upsolver: UpsolverDestinationProperties | None = None
    zendesk: ZendeskDestinationProperties | None = None


@dataclass
class DestinationFlowConfig(PropertyType):
    connector_type: str | None = None
    destination_connector_properties: DestinationConnectorProperties | None = None
    api_version: str | None = None
    connector_profile_name: str | None = None


@dataclass
class DynatraceSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class ErrorHandlingConfig(PropertyType):
    bucket_name: str | None = None
    bucket_prefix: str | None = None
    fail_on_first_error: bool | None = None


@dataclass
class EventBridgeDestinationProperties(PropertyType):
    object: str | None = None
    error_handling_config: ErrorHandlingConfig | None = None


@dataclass
class GlueDataCatalog(PropertyType):
    database_name: str | None = None
    role_arn: str | None = None
    table_prefix: str | None = None


@dataclass
class GoogleAnalyticsSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class IncrementalPullConfig(PropertyType):
    datetime_type_field_name: str | None = None


@dataclass
class InforNexusSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class LookoutMetricsDestinationProperties(PropertyType):
    object: str | None = None


@dataclass
class MarketoDestinationProperties(PropertyType):
    object: str | None = None
    error_handling_config: ErrorHandlingConfig | None = None


@dataclass
class MarketoSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class MetadataCatalogConfig(PropertyType):
    glue_data_catalog: GlueDataCatalog | None = None


@dataclass
class PardotSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class PrefixConfig(PropertyType):
    path_prefix_hierarchy: list[String] = field(default_factory=list)
    prefix_format: str | None = None
    prefix_type: str | None = None


@dataclass
class RedshiftDestinationProperties(PropertyType):
    intermediate_bucket_name: str | None = None
    object: str | None = None
    bucket_prefix: str | None = None
    error_handling_config: ErrorHandlingConfig | None = None


@dataclass
class S3DestinationProperties(PropertyType):
    bucket_name: str | None = None
    bucket_prefix: str | None = None
    s3_output_format_config: S3OutputFormatConfig | None = None


@dataclass
class S3InputFormatConfig(PropertyType):
    s3_input_file_type: str | None = None


@dataclass
class S3OutputFormatConfig(PropertyType):
    aggregation_config: AggregationConfig | None = None
    file_type: str | None = None
    prefix_config: PrefixConfig | None = None
    preserve_source_data_typing: bool | None = None


@dataclass
class S3SourceProperties(PropertyType):
    bucket_name: str | None = None
    bucket_prefix: str | None = None
    s3_input_format_config: S3InputFormatConfig | None = None


@dataclass
class SAPODataDestinationProperties(PropertyType):
    object_path: str | None = None
    error_handling_config: ErrorHandlingConfig | None = None
    id_field_names: list[String] = field(default_factory=list)
    success_response_handling_config: SuccessResponseHandlingConfig | None = None
    write_operation_type: str | None = None


@dataclass
class SAPODataPaginationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_page_size": "maxPageSize",
    }

    max_page_size: int | None = None


@dataclass
class SAPODataParallelismConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_parallelism": "maxParallelism",
    }

    max_parallelism: int | None = None


@dataclass
class SAPODataSourceProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pagination_config": "paginationConfig",
        "parallelism_config": "parallelismConfig",
    }

    object_path: str | None = None
    pagination_config: SAPODataPaginationConfig | None = None
    parallelism_config: SAPODataParallelismConfig | None = None


@dataclass
class SalesforceDestinationProperties(PropertyType):
    object: str | None = None
    data_transfer_api: str | None = None
    error_handling_config: ErrorHandlingConfig | None = None
    id_field_names: list[String] = field(default_factory=list)
    write_operation_type: str | None = None


@dataclass
class SalesforceSourceProperties(PropertyType):
    object: str | None = None
    data_transfer_api: str | None = None
    enable_dynamic_field_update: bool | None = None
    include_deleted_records: bool | None = None


@dataclass
class ScheduledTriggerProperties(PropertyType):
    schedule_expression: str | None = None
    data_pull_mode: str | None = None
    first_execution_from: float | None = None
    flow_error_deactivation_threshold: int | None = None
    schedule_end_time: float | None = None
    schedule_offset: float | None = None
    schedule_start_time: float | None = None
    time_zone: str | None = None


@dataclass
class ServiceNowSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class SingularSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class SlackSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class SnowflakeDestinationProperties(PropertyType):
    intermediate_bucket_name: str | None = None
    object: str | None = None
    bucket_prefix: str | None = None
    error_handling_config: ErrorHandlingConfig | None = None


@dataclass
class SourceConnectorProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    amplitude: AmplitudeSourceProperties | None = None
    custom_connector: CustomConnectorSourceProperties | None = None
    datadog: DatadogSourceProperties | None = None
    dynatrace: DynatraceSourceProperties | None = None
    google_analytics: GoogleAnalyticsSourceProperties | None = None
    infor_nexus: InforNexusSourceProperties | None = None
    marketo: MarketoSourceProperties | None = None
    pardot: PardotSourceProperties | None = None
    s3: S3SourceProperties | None = None
    salesforce: SalesforceSourceProperties | None = None
    sapo_data: SAPODataSourceProperties | None = None
    service_now: ServiceNowSourceProperties | None = None
    singular: SingularSourceProperties | None = None
    slack: SlackSourceProperties | None = None
    trendmicro: TrendmicroSourceProperties | None = None
    veeva: VeevaSourceProperties | None = None
    zendesk: ZendeskSourceProperties | None = None


@dataclass
class SourceFlowConfig(PropertyType):
    connector_type: str | None = None
    source_connector_properties: SourceConnectorProperties | None = None
    api_version: str | None = None
    connector_profile_name: str | None = None
    incremental_pull_config: IncrementalPullConfig | None = None


@dataclass
class SuccessResponseHandlingConfig(PropertyType):
    bucket_name: str | None = None
    bucket_prefix: str | None = None


@dataclass
class Task(PropertyType):
    source_fields: list[String] = field(default_factory=list)
    task_type: str | None = None
    connector_operator: ConnectorOperator | None = None
    destination_field: str | None = None
    task_properties: list[TaskPropertiesObject] = field(default_factory=list)


@dataclass
class TaskPropertiesObject(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class TrendmicroSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class TriggerConfig(PropertyType):
    trigger_type: str | None = None
    trigger_properties: ScheduledTriggerProperties | None = None


@dataclass
class UpsolverDestinationProperties(PropertyType):
    bucket_name: str | None = None
    s3_output_format_config: UpsolverS3OutputFormatConfig | None = None
    bucket_prefix: str | None = None


@dataclass
class UpsolverS3OutputFormatConfig(PropertyType):
    prefix_config: PrefixConfig | None = None
    aggregation_config: AggregationConfig | None = None
    file_type: str | None = None


@dataclass
class VeevaSourceProperties(PropertyType):
    object: str | None = None
    document_type: str | None = None
    include_all_versions: bool | None = None
    include_renditions: bool | None = None
    include_source_files: bool | None = None


@dataclass
class ZendeskDestinationProperties(PropertyType):
    object: str | None = None
    error_handling_config: ErrorHandlingConfig | None = None
    id_field_names: list[String] = field(default_factory=list)
    write_operation_type: str | None = None


@dataclass
class ZendeskSourceProperties(PropertyType):
    object: str | None = None
