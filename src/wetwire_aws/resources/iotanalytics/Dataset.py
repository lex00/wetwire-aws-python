"""PropertyTypes for AWS::IoTAnalytics::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    action_name: str | None = None
    container_action: ContainerAction | None = None
    query_action: QueryAction | None = None


@dataclass
class ContainerAction(PropertyType):
    execution_role_arn: str | None = None
    image: str | None = None
    resource_configuration: ResourceConfiguration | None = None
    variables: list[Variable] = field(default_factory=list)


@dataclass
class DatasetContentDeliveryRule(PropertyType):
    destination: DatasetContentDeliveryRuleDestination | None = None
    entry_name: str | None = None


@dataclass
class DatasetContentDeliveryRuleDestination(PropertyType):
    iot_events_destination_configuration: IotEventsDestinationConfiguration | None = (
        None
    )
    s3_destination_configuration: S3DestinationConfiguration | None = None


@dataclass
class DatasetContentVersionValue(PropertyType):
    dataset_name: str | None = None


@dataclass
class DeltaTime(PropertyType):
    offset_seconds: int | None = None
    time_expression: str | None = None


@dataclass
class DeltaTimeSessionWindowConfiguration(PropertyType):
    timeout_in_minutes: int | None = None


@dataclass
class Filter(PropertyType):
    delta_time: DeltaTime | None = None


@dataclass
class GlueConfiguration(PropertyType):
    database_name: str | None = None
    table_name: str | None = None


@dataclass
class IotEventsDestinationConfiguration(PropertyType):
    input_name: str | None = None
    role_arn: str | None = None


@dataclass
class LateDataRule(PropertyType):
    rule_configuration: LateDataRuleConfiguration | None = None
    rule_name: str | None = None


@dataclass
class LateDataRuleConfiguration(PropertyType):
    delta_time_session_window_configuration: (
        DeltaTimeSessionWindowConfiguration | None
    ) = None


@dataclass
class OutputFileUriValue(PropertyType):
    file_name: str | None = None


@dataclass
class QueryAction(PropertyType):
    sql_query: str | None = None
    filters: list[Filter] = field(default_factory=list)


@dataclass
class ResourceConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_size_in_gb": "VolumeSizeInGB",
    }

    compute_type: str | None = None
    volume_size_in_gb: int | None = None


@dataclass
class RetentionPeriod(PropertyType):
    number_of_days: int | None = None
    unlimited: bool | None = None


@dataclass
class S3DestinationConfiguration(PropertyType):
    bucket: str | None = None
    key: str | None = None
    role_arn: str | None = None
    glue_configuration: GlueConfiguration | None = None


@dataclass
class Schedule(PropertyType):
    schedule_expression: str | None = None


@dataclass
class Trigger(PropertyType):
    schedule: Schedule | None = None
    triggering_dataset: TriggeringDataset | None = None


@dataclass
class TriggeringDataset(PropertyType):
    dataset_name: str | None = None


@dataclass
class Variable(PropertyType):
    variable_name: str | None = None
    dataset_content_version_value: DatasetContentVersionValue | None = None
    double_value: float | None = None
    output_file_uri_value: OutputFileUriValue | None = None
    string_value: str | None = None


@dataclass
class VersioningConfiguration(PropertyType):
    max_versions: int | None = None
    unlimited: bool | None = None
