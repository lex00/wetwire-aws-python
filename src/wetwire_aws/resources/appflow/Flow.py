"""PropertyTypes for AWS::AppFlow::Flow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AggregationConfig(PropertyType):
    aggregation_type: DslValue[str] | None = None
    target_file_size: DslValue[int] | None = None


@dataclass
class AmplitudeSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class ConnectorOperator(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    amplitude: DslValue[str] | None = None
    custom_connector: DslValue[str] | None = None
    datadog: DslValue[str] | None = None
    dynatrace: DslValue[str] | None = None
    google_analytics: DslValue[str] | None = None
    infor_nexus: DslValue[str] | None = None
    marketo: DslValue[str] | None = None
    pardot: DslValue[str] | None = None
    s3: DslValue[str] | None = None
    salesforce: DslValue[str] | None = None
    sapo_data: DslValue[str] | None = None
    service_now: DslValue[str] | None = None
    singular: DslValue[str] | None = None
    slack: DslValue[str] | None = None
    trendmicro: DslValue[str] | None = None
    veeva: DslValue[str] | None = None
    zendesk: DslValue[str] | None = None


@dataclass
class CustomConnectorDestinationProperties(PropertyType):
    entity_name: DslValue[str] | None = None
    custom_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    error_handling_config: DslValue[ErrorHandlingConfig] | None = None
    id_field_names: list[DslValue[str]] = field(default_factory=list)
    write_operation_type: DslValue[str] | None = None


@dataclass
class CustomConnectorSourceProperties(PropertyType):
    entity_name: DslValue[str] | None = None
    custom_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    data_transfer_api: DslValue[DataTransferApi] | None = None


@dataclass
class DataTransferApi(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DatadogSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class DestinationConnectorProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    custom_connector: DslValue[CustomConnectorDestinationProperties] | None = None
    event_bridge: DslValue[EventBridgeDestinationProperties] | None = None
    lookout_metrics: DslValue[LookoutMetricsDestinationProperties] | None = None
    marketo: DslValue[MarketoDestinationProperties] | None = None
    redshift: DslValue[RedshiftDestinationProperties] | None = None
    s3: DslValue[S3DestinationProperties] | None = None
    salesforce: DslValue[SalesforceDestinationProperties] | None = None
    sapo_data: DslValue[SAPODataDestinationProperties] | None = None
    snowflake: DslValue[SnowflakeDestinationProperties] | None = None
    upsolver: DslValue[UpsolverDestinationProperties] | None = None
    zendesk: DslValue[ZendeskDestinationProperties] | None = None


@dataclass
class DestinationFlowConfig(PropertyType):
    connector_type: DslValue[str] | None = None
    destination_connector_properties: (
        DslValue[DestinationConnectorProperties] | None
    ) = None
    api_version: DslValue[str] | None = None
    connector_profile_name: DslValue[str] | None = None


@dataclass
class DynatraceSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class ErrorHandlingConfig(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    fail_on_first_error: DslValue[bool] | None = None


@dataclass
class EventBridgeDestinationProperties(PropertyType):
    object: DslValue[str] | None = None
    error_handling_config: DslValue[ErrorHandlingConfig] | None = None


@dataclass
class GlueDataCatalog(PropertyType):
    database_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    table_prefix: DslValue[str] | None = None


@dataclass
class GoogleAnalyticsSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class IncrementalPullConfig(PropertyType):
    datetime_type_field_name: DslValue[str] | None = None


@dataclass
class InforNexusSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class LookoutMetricsDestinationProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class MarketoDestinationProperties(PropertyType):
    object: DslValue[str] | None = None
    error_handling_config: DslValue[ErrorHandlingConfig] | None = None


@dataclass
class MarketoSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class MetadataCatalogConfig(PropertyType):
    glue_data_catalog: DslValue[GlueDataCatalog] | None = None


@dataclass
class PardotSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class PrefixConfig(PropertyType):
    path_prefix_hierarchy: list[DslValue[str]] = field(default_factory=list)
    prefix_format: DslValue[str] | None = None
    prefix_type: DslValue[str] | None = None


@dataclass
class RedshiftDestinationProperties(PropertyType):
    intermediate_bucket_name: DslValue[str] | None = None
    object: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    error_handling_config: DslValue[ErrorHandlingConfig] | None = None


@dataclass
class S3DestinationProperties(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    s3_output_format_config: DslValue[S3OutputFormatConfig] | None = None


@dataclass
class S3InputFormatConfig(PropertyType):
    s3_input_file_type: DslValue[str] | None = None


@dataclass
class S3OutputFormatConfig(PropertyType):
    aggregation_config: DslValue[AggregationConfig] | None = None
    file_type: DslValue[str] | None = None
    prefix_config: DslValue[PrefixConfig] | None = None
    preserve_source_data_typing: DslValue[bool] | None = None


@dataclass
class S3SourceProperties(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    s3_input_format_config: DslValue[S3InputFormatConfig] | None = None


@dataclass
class SAPODataDestinationProperties(PropertyType):
    object_path: DslValue[str] | None = None
    error_handling_config: DslValue[ErrorHandlingConfig] | None = None
    id_field_names: list[DslValue[str]] = field(default_factory=list)
    success_response_handling_config: DslValue[SuccessResponseHandlingConfig] | None = (
        None
    )
    write_operation_type: DslValue[str] | None = None


@dataclass
class SAPODataPaginationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_page_size": "maxPageSize",
    }

    max_page_size: DslValue[int] | None = None


@dataclass
class SAPODataParallelismConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "max_parallelism": "maxParallelism",
    }

    max_parallelism: DslValue[int] | None = None


@dataclass
class SAPODataSourceProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "pagination_config": "paginationConfig",
        "parallelism_config": "parallelismConfig",
    }

    object_path: DslValue[str] | None = None
    pagination_config: DslValue[SAPODataPaginationConfig] | None = None
    parallelism_config: DslValue[SAPODataParallelismConfig] | None = None


@dataclass
class SalesforceDestinationProperties(PropertyType):
    object: DslValue[str] | None = None
    data_transfer_api: DslValue[str] | None = None
    error_handling_config: DslValue[ErrorHandlingConfig] | None = None
    id_field_names: list[DslValue[str]] = field(default_factory=list)
    write_operation_type: DslValue[str] | None = None


@dataclass
class SalesforceSourceProperties(PropertyType):
    object: DslValue[str] | None = None
    data_transfer_api: DslValue[str] | None = None
    enable_dynamic_field_update: DslValue[bool] | None = None
    include_deleted_records: DslValue[bool] | None = None


@dataclass
class ScheduledTriggerProperties(PropertyType):
    schedule_expression: DslValue[str] | None = None
    data_pull_mode: DslValue[str] | None = None
    first_execution_from: DslValue[float] | None = None
    flow_error_deactivation_threshold: DslValue[int] | None = None
    schedule_end_time: DslValue[float] | None = None
    schedule_offset: DslValue[float] | None = None
    schedule_start_time: DslValue[float] | None = None
    time_zone: DslValue[str] | None = None


@dataclass
class ServiceNowSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class SingularSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class SlackSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class SnowflakeDestinationProperties(PropertyType):
    intermediate_bucket_name: DslValue[str] | None = None
    object: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None
    error_handling_config: DslValue[ErrorHandlingConfig] | None = None


@dataclass
class SourceConnectorProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sapo_data": "SAPOData",
    }

    amplitude: DslValue[AmplitudeSourceProperties] | None = None
    custom_connector: DslValue[CustomConnectorSourceProperties] | None = None
    datadog: DslValue[DatadogSourceProperties] | None = None
    dynatrace: DslValue[DynatraceSourceProperties] | None = None
    google_analytics: DslValue[GoogleAnalyticsSourceProperties] | None = None
    infor_nexus: DslValue[InforNexusSourceProperties] | None = None
    marketo: DslValue[MarketoSourceProperties] | None = None
    pardot: DslValue[PardotSourceProperties] | None = None
    s3: DslValue[S3SourceProperties] | None = None
    salesforce: DslValue[SalesforceSourceProperties] | None = None
    sapo_data: DslValue[SAPODataSourceProperties] | None = None
    service_now: DslValue[ServiceNowSourceProperties] | None = None
    singular: DslValue[SingularSourceProperties] | None = None
    slack: DslValue[SlackSourceProperties] | None = None
    trendmicro: DslValue[TrendmicroSourceProperties] | None = None
    veeva: DslValue[VeevaSourceProperties] | None = None
    zendesk: DslValue[ZendeskSourceProperties] | None = None


@dataclass
class SourceFlowConfig(PropertyType):
    connector_type: DslValue[str] | None = None
    source_connector_properties: DslValue[SourceConnectorProperties] | None = None
    api_version: DslValue[str] | None = None
    connector_profile_name: DslValue[str] | None = None
    incremental_pull_config: DslValue[IncrementalPullConfig] | None = None


@dataclass
class SuccessResponseHandlingConfig(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None


@dataclass
class Task(PropertyType):
    source_fields: list[DslValue[str]] = field(default_factory=list)
    task_type: DslValue[str] | None = None
    connector_operator: DslValue[ConnectorOperator] | None = None
    destination_field: DslValue[str] | None = None
    task_properties: list[DslValue[TaskPropertiesObject]] = field(default_factory=list)


@dataclass
class TaskPropertiesObject(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TrendmicroSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class TriggerConfig(PropertyType):
    trigger_type: DslValue[str] | None = None
    trigger_properties: DslValue[ScheduledTriggerProperties] | None = None


@dataclass
class UpsolverDestinationProperties(PropertyType):
    bucket_name: DslValue[str] | None = None
    s3_output_format_config: DslValue[UpsolverS3OutputFormatConfig] | None = None
    bucket_prefix: DslValue[str] | None = None


@dataclass
class UpsolverS3OutputFormatConfig(PropertyType):
    prefix_config: DslValue[PrefixConfig] | None = None
    aggregation_config: DslValue[AggregationConfig] | None = None
    file_type: DslValue[str] | None = None


@dataclass
class VeevaSourceProperties(PropertyType):
    object: DslValue[str] | None = None
    document_type: DslValue[str] | None = None
    include_all_versions: DslValue[bool] | None = None
    include_renditions: DslValue[bool] | None = None
    include_source_files: DslValue[bool] | None = None


@dataclass
class ZendeskDestinationProperties(PropertyType):
    object: DslValue[str] | None = None
    error_handling_config: DslValue[ErrorHandlingConfig] | None = None
    id_field_names: list[DslValue[str]] = field(default_factory=list)
    write_operation_type: DslValue[str] | None = None


@dataclass
class ZendeskSourceProperties(PropertyType):
    object: DslValue[str] | None = None
