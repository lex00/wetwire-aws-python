"""PropertyTypes for AWS::IoTEvents::AlarmModel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AcknowledgeFlow(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class AlarmAction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamo_db": "DynamoDB",
    }

    dynamo_d_bv2: DslValue[DynamoDBv2] | None = None
    dynamo_db: DslValue[DynamoDB] | None = None
    firehose: DslValue[Firehose] | None = None
    iot_events: DslValue[IotEvents] | None = None
    iot_site_wise: DslValue[IotSiteWise] | None = None
    iot_topic_publish: DslValue[IotTopicPublish] | None = None
    lambda_: DslValue[Lambda] | None = None
    sns: DslValue[Sns] | None = None
    sqs: DslValue[Sqs] | None = None


@dataclass
class AlarmCapabilities(PropertyType):
    acknowledge_flow: DslValue[AcknowledgeFlow] | None = None
    initialization_configuration: DslValue[InitializationConfiguration] | None = None


@dataclass
class AlarmEventActions(PropertyType):
    alarm_actions: list[DslValue[AlarmAction]] = field(default_factory=list)


@dataclass
class AlarmRule(PropertyType):
    simple_rule: DslValue[SimpleRule] | None = None


@dataclass
class AssetPropertyTimestamp(PropertyType):
    time_in_seconds: DslValue[str] | None = None
    offset_in_nanos: DslValue[str] | None = None


@dataclass
class AssetPropertyValue(PropertyType):
    value: DslValue[AssetPropertyVariant] | None = None
    quality: DslValue[str] | None = None
    timestamp: DslValue[AssetPropertyTimestamp] | None = None


@dataclass
class AssetPropertyVariant(PropertyType):
    boolean_value: DslValue[str] | None = None
    double_value: DslValue[str] | None = None
    integer_value: DslValue[str] | None = None
    string_value: DslValue[str] | None = None


@dataclass
class DynamoDB(PropertyType):
    hash_key_field: DslValue[str] | None = None
    hash_key_value: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    hash_key_type: DslValue[str] | None = None
    operation: DslValue[str] | None = None
    payload: DslValue[Payload] | None = None
    payload_field: DslValue[str] | None = None
    range_key_field: DslValue[str] | None = None
    range_key_type: DslValue[str] | None = None
    range_key_value: DslValue[str] | None = None


@dataclass
class DynamoDBv2(PropertyType):
    table_name: DslValue[str] | None = None
    payload: DslValue[Payload] | None = None


@dataclass
class Firehose(PropertyType):
    delivery_stream_name: DslValue[str] | None = None
    payload: DslValue[Payload] | None = None
    separator: DslValue[str] | None = None


@dataclass
class InitializationConfiguration(PropertyType):
    disabled_on_initialization: DslValue[bool] | None = None


@dataclass
class IotEvents(PropertyType):
    input_name: DslValue[str] | None = None
    payload: DslValue[Payload] | None = None


@dataclass
class IotSiteWise(PropertyType):
    asset_id: DslValue[str] | None = None
    entry_id: DslValue[str] | None = None
    property_alias: DslValue[str] | None = None
    property_id: DslValue[str] | None = None
    property_value: DslValue[AssetPropertyValue] | None = None


@dataclass
class IotTopicPublish(PropertyType):
    mqtt_topic: DslValue[str] | None = None
    payload: DslValue[Payload] | None = None


@dataclass
class Lambda(PropertyType):
    function_arn: DslValue[str] | None = None
    payload: DslValue[Payload] | None = None


@dataclass
class Payload(PropertyType):
    content_expression: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class SimpleRule(PropertyType):
    comparison_operator: DslValue[str] | None = None
    input_property: DslValue[str] | None = None
    threshold: DslValue[str] | None = None


@dataclass
class Sns(PropertyType):
    target_arn: DslValue[str] | None = None
    payload: DslValue[Payload] | None = None


@dataclass
class Sqs(PropertyType):
    queue_url: DslValue[str] | None = None
    payload: DslValue[Payload] | None = None
    use_base64: DslValue[bool] | None = None
