"""PropertyTypes for AWS::IoTAnalytics::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    action_name: DslValue[str] | None = None
    container_action: DslValue[ContainerAction] | None = None
    query_action: DslValue[QueryAction] | None = None


@dataclass
class ContainerAction(PropertyType):
    execution_role_arn: DslValue[str] | None = None
    image: DslValue[str] | None = None
    resource_configuration: DslValue[ResourceConfiguration] | None = None
    variables: list[DslValue[Variable]] = field(default_factory=list)


@dataclass
class DatasetContentDeliveryRule(PropertyType):
    destination: DslValue[DatasetContentDeliveryRuleDestination] | None = None
    entry_name: DslValue[str] | None = None


@dataclass
class DatasetContentDeliveryRuleDestination(PropertyType):
    iot_events_destination_configuration: (
        DslValue[IotEventsDestinationConfiguration] | None
    ) = None
    s3_destination_configuration: DslValue[S3DestinationConfiguration] | None = None


@dataclass
class DatasetContentVersionValue(PropertyType):
    dataset_name: DslValue[str] | None = None


@dataclass
class DeltaTime(PropertyType):
    offset_seconds: DslValue[int] | None = None
    time_expression: DslValue[str] | None = None


@dataclass
class DeltaTimeSessionWindowConfiguration(PropertyType):
    timeout_in_minutes: DslValue[int] | None = None


@dataclass
class Filter(PropertyType):
    delta_time: DslValue[DeltaTime] | None = None


@dataclass
class GlueConfiguration(PropertyType):
    database_name: DslValue[str] | None = None
    table_name: DslValue[str] | None = None


@dataclass
class IotEventsDestinationConfiguration(PropertyType):
    input_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class LateDataRule(PropertyType):
    rule_configuration: DslValue[LateDataRuleConfiguration] | None = None
    rule_name: DslValue[str] | None = None


@dataclass
class LateDataRuleConfiguration(PropertyType):
    delta_time_session_window_configuration: (
        DslValue[DeltaTimeSessionWindowConfiguration] | None
    ) = None


@dataclass
class OutputFileUriValue(PropertyType):
    file_name: DslValue[str] | None = None


@dataclass
class QueryAction(PropertyType):
    sql_query: DslValue[str] | None = None
    filters: list[DslValue[Filter]] = field(default_factory=list)


@dataclass
class ResourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_size_in_gb": "VolumeSizeInGB",
    }

    compute_type: DslValue[str] | None = None
    volume_size_in_gb: DslValue[int] | None = None


@dataclass
class RetentionPeriod(PropertyType):
    number_of_days: DslValue[int] | None = None
    unlimited: DslValue[bool] | None = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    glue_configuration: DslValue[GlueConfiguration] | None = None


@dataclass
class Schedule(PropertyType):
    schedule_expression: DslValue[str] | None = None


@dataclass
class Trigger(PropertyType):
    schedule: DslValue[Schedule] | None = None
    triggering_dataset: DslValue[TriggeringDataset] | None = None


@dataclass
class TriggeringDataset(PropertyType):
    dataset_name: DslValue[str] | None = None


@dataclass
class Variable(PropertyType):
    variable_name: DslValue[str] | None = None
    dataset_content_version_value: DslValue[DatasetContentVersionValue] | None = None
    double_value: DslValue[float] | None = None
    output_file_uri_value: DslValue[OutputFileUriValue] | None = None
    string_value: DslValue[str] | None = None


@dataclass
class VersioningConfiguration(PropertyType):
    max_versions: DslValue[int] | None = None
    unlimited: DslValue[bool] | None = None
