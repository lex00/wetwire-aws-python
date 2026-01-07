"""PropertyTypes for AWS::CustomerProfiles::Integration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectorOperator(PropertyType):
    marketo: DslValue[str] | None = None
    s3: DslValue[str] | None = None
    salesforce: DslValue[str] | None = None
    service_now: DslValue[str] | None = None
    zendesk: DslValue[str] | None = None


@dataclass
class FlowDefinition(PropertyType):
    flow_name: DslValue[str] | None = None
    kms_arn: DslValue[str] | None = None
    source_flow_config: DslValue[SourceFlowConfig] | None = None
    tasks: list[DslValue[Task]] = field(default_factory=list)
    trigger_config: DslValue[TriggerConfig] | None = None
    description: DslValue[str] | None = None


@dataclass
class IncrementalPullConfig(PropertyType):
    datetime_type_field_name: DslValue[str] | None = None


@dataclass
class MarketoSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class ObjectTypeMapping(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class S3SourceProperties(PropertyType):
    bucket_name: DslValue[str] | None = None
    bucket_prefix: DslValue[str] | None = None


@dataclass
class SalesforceSourceProperties(PropertyType):
    object: DslValue[str] | None = None
    enable_dynamic_field_update: DslValue[bool] | None = None
    include_deleted_records: DslValue[bool] | None = None


@dataclass
class ScheduledTriggerProperties(PropertyType):
    schedule_expression: DslValue[str] | None = None
    data_pull_mode: DslValue[str] | None = None
    first_execution_from: DslValue[float] | None = None
    schedule_end_time: DslValue[float] | None = None
    schedule_offset: DslValue[int] | None = None
    schedule_start_time: DslValue[float] | None = None
    timezone: DslValue[str] | None = None


@dataclass
class ServiceNowSourceProperties(PropertyType):
    object: DslValue[str] | None = None


@dataclass
class SourceConnectorProperties(PropertyType):
    marketo: DslValue[MarketoSourceProperties] | None = None
    s3: DslValue[S3SourceProperties] | None = None
    salesforce: DslValue[SalesforceSourceProperties] | None = None
    service_now: DslValue[ServiceNowSourceProperties] | None = None
    zendesk: DslValue[ZendeskSourceProperties] | None = None


@dataclass
class SourceFlowConfig(PropertyType):
    connector_type: DslValue[str] | None = None
    source_connector_properties: DslValue[SourceConnectorProperties] | None = None
    connector_profile_name: DslValue[str] | None = None
    incremental_pull_config: DslValue[IncrementalPullConfig] | None = None


@dataclass
class Task(PropertyType):
    source_fields: list[DslValue[str]] = field(default_factory=list)
    task_type: DslValue[str] | None = None
    connector_operator: DslValue[ConnectorOperator] | None = None
    destination_field: DslValue[str] | None = None
    task_properties: list[DslValue[TaskPropertiesMap]] = field(default_factory=list)


@dataclass
class TaskPropertiesMap(PropertyType):
    operator_property_key: DslValue[str] | None = None
    property: DslValue[str] | None = None


@dataclass
class TriggerConfig(PropertyType):
    trigger_type: DslValue[str] | None = None
    trigger_properties: DslValue[TriggerProperties] | None = None


@dataclass
class TriggerProperties(PropertyType):
    scheduled: DslValue[ScheduledTriggerProperties] | None = None


@dataclass
class ZendeskSourceProperties(PropertyType):
    object: DslValue[str] | None = None
