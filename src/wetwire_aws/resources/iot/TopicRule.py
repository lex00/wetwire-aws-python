"""PropertyTypes for AWS::IoT::TopicRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamo_db": "DynamoDB",
    }

    cloudwatch_alarm: CloudwatchAlarmAction | None = None
    cloudwatch_logs: CloudwatchLogsAction | None = None
    cloudwatch_metric: CloudwatchMetricAction | None = None
    dynamo_d_bv2: DynamoDBv2Action | None = None
    dynamo_db: DynamoDBAction | None = None
    elasticsearch: ElasticsearchAction | None = None
    firehose: FirehoseAction | None = None
    http: HttpAction | None = None
    iot_analytics: IotAnalyticsAction | None = None
    iot_events: IotEventsAction | None = None
    iot_site_wise: IotSiteWiseAction | None = None
    kafka: KafkaAction | None = None
    kinesis: KinesisAction | None = None
    lambda_: LambdaAction | None = None
    location: LocationAction | None = None
    open_search: OpenSearchAction | None = None
    republish: RepublishAction | None = None
    s3: S3Action | None = None
    sns: SnsAction | None = None
    sqs: SqsAction | None = None
    step_functions: StepFunctionsAction | None = None
    timestream: TimestreamAction | None = None


@dataclass
class AssetPropertyTimestamp(PropertyType):
    time_in_seconds: str | None = None
    offset_in_nanos: str | None = None


@dataclass
class AssetPropertyValue(PropertyType):
    timestamp: AssetPropertyTimestamp | None = None
    value: AssetPropertyVariant | None = None
    quality: str | None = None


@dataclass
class AssetPropertyVariant(PropertyType):
    boolean_value: str | None = None
    double_value: str | None = None
    integer_value: str | None = None
    string_value: str | None = None


@dataclass
class BatchConfig(PropertyType):
    max_batch_open_ms: int | None = None
    max_batch_size: int | None = None
    max_batch_size_bytes: int | None = None


@dataclass
class CloudwatchAlarmAction(PropertyType):
    alarm_name: str | None = None
    role_arn: str | None = None
    state_reason: str | None = None
    state_value: str | None = None


@dataclass
class CloudwatchLogsAction(PropertyType):
    log_group_name: str | None = None
    role_arn: str | None = None
    batch_mode: bool | None = None


@dataclass
class CloudwatchMetricAction(PropertyType):
    metric_name: str | None = None
    metric_namespace: str | None = None
    metric_unit: str | None = None
    metric_value: str | None = None
    role_arn: str | None = None
    metric_timestamp: str | None = None


@dataclass
class DynamoDBAction(PropertyType):
    hash_key_field: str | None = None
    hash_key_value: str | None = None
    role_arn: str | None = None
    table_name: str | None = None
    hash_key_type: str | None = None
    payload_field: str | None = None
    range_key_field: str | None = None
    range_key_type: str | None = None
    range_key_value: str | None = None


@dataclass
class DynamoDBv2Action(PropertyType):
    put_item: PutItemInput | None = None
    role_arn: str | None = None


@dataclass
class ElasticsearchAction(PropertyType):
    endpoint: str | None = None
    id: str | None = None
    index: str | None = None
    role_arn: str | None = None
    type_: str | None = None


@dataclass
class FirehoseAction(PropertyType):
    delivery_stream_name: str | None = None
    role_arn: str | None = None
    batch_mode: bool | None = None
    separator: str | None = None


@dataclass
class HttpAction(PropertyType):
    url: str | None = None
    auth: HttpAuthorization | None = None
    batch_config: BatchConfig | None = None
    confirmation_url: str | None = None
    enable_batching: bool | None = None
    headers: list[HttpActionHeader] = field(default_factory=list)


@dataclass
class HttpActionHeader(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class HttpAuthorization(PropertyType):
    sigv4: SigV4Authorization | None = None


@dataclass
class IotAnalyticsAction(PropertyType):
    channel_name: str | None = None
    role_arn: str | None = None
    batch_mode: bool | None = None


@dataclass
class IotEventsAction(PropertyType):
    input_name: str | None = None
    role_arn: str | None = None
    batch_mode: bool | None = None
    message_id: str | None = None


@dataclass
class IotSiteWiseAction(PropertyType):
    put_asset_property_value_entries: list[PutAssetPropertyValueEntry] = field(
        default_factory=list
    )
    role_arn: str | None = None


@dataclass
class KafkaAction(PropertyType):
    client_properties: dict[str, String] = field(default_factory=dict)
    destination_arn: str | None = None
    topic: str | None = None
    headers: list[KafkaActionHeader] = field(default_factory=list)
    key: str | None = None
    partition: str | None = None


@dataclass
class KafkaActionHeader(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class KinesisAction(PropertyType):
    role_arn: str | None = None
    stream_name: str | None = None
    partition_key: str | None = None


@dataclass
class LambdaAction(PropertyType):
    function_arn: str | None = None


@dataclass
class LocationAction(PropertyType):
    device_id: str | None = None
    latitude: str | None = None
    longitude: str | None = None
    role_arn: str | None = None
    tracker_name: str | None = None
    timestamp: Timestamp | None = None


@dataclass
class OpenSearchAction(PropertyType):
    endpoint: str | None = None
    id: str | None = None
    index: str | None = None
    role_arn: str | None = None
    type_: str | None = None


@dataclass
class PutAssetPropertyValueEntry(PropertyType):
    property_values: list[AssetPropertyValue] = field(default_factory=list)
    asset_id: str | None = None
    entry_id: str | None = None
    property_alias: str | None = None
    property_id: str | None = None


@dataclass
class PutItemInput(PropertyType):
    table_name: str | None = None


@dataclass
class RepublishAction(PropertyType):
    role_arn: str | None = None
    topic: str | None = None
    headers: RepublishActionHeaders | None = None
    qos: int | None = None


@dataclass
class RepublishActionHeaders(PropertyType):
    content_type: str | None = None
    correlation_data: str | None = None
    message_expiry: str | None = None
    payload_format_indicator: str | None = None
    response_topic: str | None = None
    user_properties: list[UserProperty] = field(default_factory=list)


@dataclass
class S3Action(PropertyType):
    bucket_name: str | None = None
    key: str | None = None
    role_arn: str | None = None
    canned_acl: str | None = None


@dataclass
class SigV4Authorization(PropertyType):
    role_arn: str | None = None
    service_name: str | None = None
    signing_region: str | None = None


@dataclass
class SnsAction(PropertyType):
    role_arn: str | None = None
    target_arn: str | None = None
    message_format: str | None = None


@dataclass
class SqsAction(PropertyType):
    queue_url: str | None = None
    role_arn: str | None = None
    use_base64: bool | None = None


@dataclass
class StepFunctionsAction(PropertyType):
    role_arn: str | None = None
    state_machine_name: str | None = None
    execution_name_prefix: str | None = None


@dataclass
class Timestamp(PropertyType):
    value: str | None = None
    unit: str | None = None


@dataclass
class TimestreamAction(PropertyType):
    database_name: str | None = None
    dimensions: list[TimestreamDimension] = field(default_factory=list)
    role_arn: str | None = None
    table_name: str | None = None
    timestamp: TimestreamTimestamp | None = None


@dataclass
class TimestreamDimension(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class TimestreamTimestamp(PropertyType):
    unit: str | None = None
    value: str | None = None


@dataclass
class TopicRulePayload(PropertyType):
    actions: list[Action] = field(default_factory=list)
    sql: str | None = None
    aws_iot_sql_version: str | None = None
    description: str | None = None
    error_action: Action | None = None
    rule_disabled: bool | None = None


@dataclass
class UserProperty(PropertyType):
    key: str | None = None
    value: str | None = None
