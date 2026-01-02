"""PropertyTypes for AWS::IoTEvents::AlarmModel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AcknowledgeFlow(PropertyType):
    enabled: bool | None = None


@dataclass
class AlarmAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamo_db": "DynamoDB",
    }

    dynamo_d_bv2: DynamoDBv2 | None = None
    dynamo_db: DynamoDB | None = None
    firehose: Firehose | None = None
    iot_events: IotEvents | None = None
    iot_site_wise: IotSiteWise | None = None
    iot_topic_publish: IotTopicPublish | None = None
    lambda_: Lambda | None = None
    sns: Sns | None = None
    sqs: Sqs | None = None


@dataclass
class AlarmCapabilities(PropertyType):
    acknowledge_flow: AcknowledgeFlow | None = None
    initialization_configuration: InitializationConfiguration | None = None


@dataclass
class AlarmEventActions(PropertyType):
    alarm_actions: list[AlarmAction] = field(default_factory=list)


@dataclass
class AlarmRule(PropertyType):
    simple_rule: SimpleRule | None = None


@dataclass
class AssetPropertyTimestamp(PropertyType):
    time_in_seconds: str | None = None
    offset_in_nanos: str | None = None


@dataclass
class AssetPropertyValue(PropertyType):
    value: AssetPropertyVariant | None = None
    quality: str | None = None
    timestamp: AssetPropertyTimestamp | None = None


@dataclass
class AssetPropertyVariant(PropertyType):
    boolean_value: str | None = None
    double_value: str | None = None
    integer_value: str | None = None
    string_value: str | None = None


@dataclass
class DynamoDB(PropertyType):
    hash_key_field: str | None = None
    hash_key_value: str | None = None
    table_name: str | None = None
    hash_key_type: str | None = None
    operation: str | None = None
    payload: Payload | None = None
    payload_field: str | None = None
    range_key_field: str | None = None
    range_key_type: str | None = None
    range_key_value: str | None = None


@dataclass
class DynamoDBv2(PropertyType):
    table_name: str | None = None
    payload: Payload | None = None


@dataclass
class Firehose(PropertyType):
    delivery_stream_name: str | None = None
    payload: Payload | None = None
    separator: str | None = None


@dataclass
class InitializationConfiguration(PropertyType):
    disabled_on_initialization: bool | None = None


@dataclass
class IotEvents(PropertyType):
    input_name: str | None = None
    payload: Payload | None = None


@dataclass
class IotSiteWise(PropertyType):
    asset_id: str | None = None
    entry_id: str | None = None
    property_alias: str | None = None
    property_id: str | None = None
    property_value: AssetPropertyValue | None = None


@dataclass
class IotTopicPublish(PropertyType):
    mqtt_topic: str | None = None
    payload: Payload | None = None


@dataclass
class Lambda(PropertyType):
    function_arn: str | None = None
    payload: Payload | None = None


@dataclass
class Payload(PropertyType):
    content_expression: str | None = None
    type_: str | None = None


@dataclass
class SimpleRule(PropertyType):
    comparison_operator: str | None = None
    input_property: str | None = None
    threshold: str | None = None


@dataclass
class Sns(PropertyType):
    target_arn: str | None = None
    payload: Payload | None = None


@dataclass
class Sqs(PropertyType):
    queue_url: str | None = None
    payload: Payload | None = None
    use_base64: bool | None = None
