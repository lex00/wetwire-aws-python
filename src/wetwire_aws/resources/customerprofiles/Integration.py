"""PropertyTypes for AWS::CustomerProfiles::Integration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConnectorOperator(PropertyType):
    marketo: str | None = None
    s3: str | None = None
    salesforce: str | None = None
    service_now: str | None = None
    zendesk: str | None = None


@dataclass
class FlowDefinition(PropertyType):
    flow_name: str | None = None
    kms_arn: str | None = None
    source_flow_config: SourceFlowConfig | None = None
    tasks: list[Task] = field(default_factory=list)
    trigger_config: TriggerConfig | None = None
    description: str | None = None


@dataclass
class IncrementalPullConfig(PropertyType):
    datetime_type_field_name: str | None = None


@dataclass
class MarketoSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class ObjectTypeMapping(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class S3SourceProperties(PropertyType):
    bucket_name: str | None = None
    bucket_prefix: str | None = None


@dataclass
class SalesforceSourceProperties(PropertyType):
    object: str | None = None
    enable_dynamic_field_update: bool | None = None
    include_deleted_records: bool | None = None


@dataclass
class ScheduledTriggerProperties(PropertyType):
    schedule_expression: str | None = None
    data_pull_mode: str | None = None
    first_execution_from: float | None = None
    schedule_end_time: float | None = None
    schedule_offset: int | None = None
    schedule_start_time: float | None = None
    timezone: str | None = None


@dataclass
class ServiceNowSourceProperties(PropertyType):
    object: str | None = None


@dataclass
class SourceConnectorProperties(PropertyType):
    marketo: MarketoSourceProperties | None = None
    s3: S3SourceProperties | None = None
    salesforce: SalesforceSourceProperties | None = None
    service_now: ServiceNowSourceProperties | None = None
    zendesk: ZendeskSourceProperties | None = None


@dataclass
class SourceFlowConfig(PropertyType):
    connector_type: str | None = None
    source_connector_properties: SourceConnectorProperties | None = None
    connector_profile_name: str | None = None
    incremental_pull_config: IncrementalPullConfig | None = None


@dataclass
class Task(PropertyType):
    source_fields: list[String] = field(default_factory=list)
    task_type: str | None = None
    connector_operator: ConnectorOperator | None = None
    destination_field: str | None = None
    task_properties: list[TaskPropertiesMap] = field(default_factory=list)


@dataclass
class TaskPropertiesMap(PropertyType):
    operator_property_key: str | None = None
    property: str | None = None


@dataclass
class TriggerConfig(PropertyType):
    trigger_type: str | None = None
    trigger_properties: TriggerProperties | None = None


@dataclass
class TriggerProperties(PropertyType):
    scheduled: ScheduledTriggerProperties | None = None


@dataclass
class ZendeskSourceProperties(PropertyType):
    object: str | None = None
