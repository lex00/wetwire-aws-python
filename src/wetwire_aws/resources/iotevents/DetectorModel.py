"""PropertyTypes for AWS::IoTEvents::DetectorModel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamo_db": "DynamoDB",
    }

    clear_timer: ClearTimer | None = None
    dynamo_d_bv2: DynamoDBv2 | None = None
    dynamo_db: DynamoDB | None = None
    firehose: Firehose | None = None
    iot_events: IotEvents | None = None
    iot_site_wise: IotSiteWise | None = None
    iot_topic_publish: IotTopicPublish | None = None
    lambda_: Lambda | None = None
    reset_timer: ResetTimer | None = None
    set_timer: SetTimer | None = None
    set_variable: SetVariable | None = None
    sns: Sns | None = None
    sqs: Sqs | None = None


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
class ClearTimer(PropertyType):
    timer_name: str | None = None


@dataclass
class DetectorModelDefinition(PropertyType):
    initial_state_name: str | None = None
    states: list[State] = field(default_factory=list)


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
class Event(PropertyType):
    event_name: str | None = None
    actions: list[Action] = field(default_factory=list)
    condition: str | None = None


@dataclass
class Firehose(PropertyType):
    delivery_stream_name: str | None = None
    payload: Payload | None = None
    separator: str | None = None


@dataclass
class IotEvents(PropertyType):
    input_name: str | None = None
    payload: Payload | None = None


@dataclass
class IotSiteWise(PropertyType):
    property_value: AssetPropertyValue | None = None
    asset_id: str | None = None
    entry_id: str | None = None
    property_alias: str | None = None
    property_id: str | None = None


@dataclass
class IotTopicPublish(PropertyType):
    mqtt_topic: str | None = None
    payload: Payload | None = None


@dataclass
class Lambda(PropertyType):
    function_arn: str | None = None
    payload: Payload | None = None


@dataclass
class OnEnter(PropertyType):
    events: list[Event] = field(default_factory=list)


@dataclass
class OnExit(PropertyType):
    events: list[Event] = field(default_factory=list)


@dataclass
class OnInput(PropertyType):
    events: list[Event] = field(default_factory=list)
    transition_events: list[TransitionEvent] = field(default_factory=list)


@dataclass
class Payload(PropertyType):
    content_expression: str | None = None
    type_: str | None = None


@dataclass
class ResetTimer(PropertyType):
    timer_name: str | None = None


@dataclass
class SetTimer(PropertyType):
    timer_name: str | None = None
    duration_expression: str | None = None
    seconds: int | None = None


@dataclass
class SetVariable(PropertyType):
    value: str | None = None
    variable_name: str | None = None


@dataclass
class Sns(PropertyType):
    target_arn: str | None = None
    payload: Payload | None = None


@dataclass
class Sqs(PropertyType):
    queue_url: str | None = None
    payload: Payload | None = None
    use_base64: bool | None = None


@dataclass
class State(PropertyType):
    state_name: str | None = None
    on_enter: OnEnter | None = None
    on_exit: OnExit | None = None
    on_input: OnInput | None = None


@dataclass
class TransitionEvent(PropertyType):
    condition: str | None = None
    event_name: str | None = None
    next_state: str | None = None
    actions: list[Action] = field(default_factory=list)
