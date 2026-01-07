"""PropertyTypes for AWS::IoT::TopicRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dynamo_db": "DynamoDB",
    }

    cloudwatch_alarm: DslValue[CloudwatchAlarmAction] | None = None
    cloudwatch_logs: DslValue[CloudwatchLogsAction] | None = None
    cloudwatch_metric: DslValue[CloudwatchMetricAction] | None = None
    dynamo_d_bv2: DslValue[DynamoDBv2Action] | None = None
    dynamo_db: DslValue[DynamoDBAction] | None = None
    elasticsearch: DslValue[ElasticsearchAction] | None = None
    firehose: DslValue[FirehoseAction] | None = None
    http: DslValue[HttpAction] | None = None
    iot_analytics: DslValue[IotAnalyticsAction] | None = None
    iot_events: DslValue[IotEventsAction] | None = None
    iot_site_wise: DslValue[IotSiteWiseAction] | None = None
    kafka: DslValue[KafkaAction] | None = None
    kinesis: DslValue[KinesisAction] | None = None
    lambda_: DslValue[LambdaAction] | None = None
    location: DslValue[LocationAction] | None = None
    open_search: DslValue[OpenSearchAction] | None = None
    republish: DslValue[RepublishAction] | None = None
    s3: DslValue[S3Action] | None = None
    sns: DslValue[SnsAction] | None = None
    sqs: DslValue[SqsAction] | None = None
    step_functions: DslValue[StepFunctionsAction] | None = None
    timestream: DslValue[TimestreamAction] | None = None


@dataclass
class AssetPropertyTimestamp(PropertyType):
    time_in_seconds: DslValue[str] | None = None
    offset_in_nanos: DslValue[str] | None = None


@dataclass
class AssetPropertyValue(PropertyType):
    timestamp: DslValue[AssetPropertyTimestamp] | None = None
    value: DslValue[AssetPropertyVariant] | None = None
    quality: DslValue[str] | None = None


@dataclass
class AssetPropertyVariant(PropertyType):
    boolean_value: DslValue[str] | None = None
    double_value: DslValue[str] | None = None
    integer_value: DslValue[str] | None = None
    string_value: DslValue[str] | None = None


@dataclass
class BatchConfig(PropertyType):
    max_batch_open_ms: DslValue[int] | None = None
    max_batch_size: DslValue[int] | None = None
    max_batch_size_bytes: DslValue[int] | None = None


@dataclass
class CloudwatchAlarmAction(PropertyType):
    alarm_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    state_reason: DslValue[str] | None = None
    state_value: DslValue[str] | None = None


@dataclass
class CloudwatchLogsAction(PropertyType):
    log_group_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    batch_mode: DslValue[bool] | None = None


@dataclass
class CloudwatchMetricAction(PropertyType):
    metric_name: DslValue[str] | None = None
    metric_namespace: DslValue[str] | None = None
    metric_unit: DslValue[str] | None = None
    metric_value: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    metric_timestamp: DslValue[str] | None = None


@dataclass
class DynamoDBAction(PropertyType):
    hash_key_field: DslValue[str] | None = None
    hash_key_value: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    hash_key_type: DslValue[str] | None = None
    payload_field: DslValue[str] | None = None
    range_key_field: DslValue[str] | None = None
    range_key_type: DslValue[str] | None = None
    range_key_value: DslValue[str] | None = None


@dataclass
class DynamoDBv2Action(PropertyType):
    put_item: DslValue[PutItemInput] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class ElasticsearchAction(PropertyType):
    endpoint: DslValue[str] | None = None
    id: DslValue[str] | None = None
    index: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FirehoseAction(PropertyType):
    delivery_stream_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    batch_mode: DslValue[bool] | None = None
    separator: DslValue[str] | None = None


@dataclass
class HttpAction(PropertyType):
    url: DslValue[str] | None = None
    auth: DslValue[HttpAuthorization] | None = None
    batch_config: DslValue[BatchConfig] | None = None
    confirmation_url: DslValue[str] | None = None
    enable_batching: DslValue[bool] | None = None
    headers: list[DslValue[HttpActionHeader]] = field(default_factory=list)


@dataclass
class HttpActionHeader(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class HttpAuthorization(PropertyType):
    sigv4: DslValue[SigV4Authorization] | None = None


@dataclass
class IotAnalyticsAction(PropertyType):
    channel_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    batch_mode: DslValue[bool] | None = None


@dataclass
class IotEventsAction(PropertyType):
    input_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    batch_mode: DslValue[bool] | None = None
    message_id: DslValue[str] | None = None


@dataclass
class IotSiteWiseAction(PropertyType):
    put_asset_property_value_entries: list[DslValue[PutAssetPropertyValueEntry]] = (
        field(default_factory=list)
    )
    role_arn: DslValue[str] | None = None


@dataclass
class KafkaAction(PropertyType):
    client_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    destination_arn: DslValue[str] | None = None
    topic: DslValue[str] | None = None
    headers: list[DslValue[KafkaActionHeader]] = field(default_factory=list)
    key: DslValue[str] | None = None
    partition: DslValue[str] | None = None


@dataclass
class KafkaActionHeader(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class KinesisAction(PropertyType):
    role_arn: DslValue[str] | None = None
    stream_name: DslValue[str] | None = None
    partition_key: DslValue[str] | None = None


@dataclass
class LambdaAction(PropertyType):
    function_arn: DslValue[str] | None = None


@dataclass
class LocationAction(PropertyType):
    device_id: DslValue[str] | None = None
    latitude: DslValue[str] | None = None
    longitude: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    tracker_name: DslValue[str] | None = None
    timestamp: DslValue[Timestamp] | None = None


@dataclass
class OpenSearchAction(PropertyType):
    endpoint: DslValue[str] | None = None
    id: DslValue[str] | None = None
    index: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class PutAssetPropertyValueEntry(PropertyType):
    property_values: list[DslValue[AssetPropertyValue]] = field(default_factory=list)
    asset_id: DslValue[str] | None = None
    entry_id: DslValue[str] | None = None
    property_alias: DslValue[str] | None = None
    property_id: DslValue[str] | None = None


@dataclass
class PutItemInput(PropertyType):
    table_name: DslValue[str] | None = None


@dataclass
class RepublishAction(PropertyType):
    role_arn: DslValue[str] | None = None
    topic: DslValue[str] | None = None
    headers: DslValue[RepublishActionHeaders] | None = None
    qos: DslValue[int] | None = None


@dataclass
class RepublishActionHeaders(PropertyType):
    content_type: DslValue[str] | None = None
    correlation_data: DslValue[str] | None = None
    message_expiry: DslValue[str] | None = None
    payload_format_indicator: DslValue[str] | None = None
    response_topic: DslValue[str] | None = None
    user_properties: list[DslValue[UserProperty]] = field(default_factory=list)


@dataclass
class S3Action(PropertyType):
    bucket_name: DslValue[str] | None = None
    key: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    canned_acl: DslValue[str] | None = None


@dataclass
class SigV4Authorization(PropertyType):
    role_arn: DslValue[str] | None = None
    service_name: DslValue[str] | None = None
    signing_region: DslValue[str] | None = None


@dataclass
class SnsAction(PropertyType):
    role_arn: DslValue[str] | None = None
    target_arn: DslValue[str] | None = None
    message_format: DslValue[str] | None = None


@dataclass
class SqsAction(PropertyType):
    queue_url: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    use_base64: DslValue[bool] | None = None


@dataclass
class StepFunctionsAction(PropertyType):
    role_arn: DslValue[str] | None = None
    state_machine_name: DslValue[str] | None = None
    execution_name_prefix: DslValue[str] | None = None


@dataclass
class Timestamp(PropertyType):
    value: DslValue[str] | None = None
    unit: DslValue[str] | None = None


@dataclass
class TimestreamAction(PropertyType):
    database_name: DslValue[str] | None = None
    dimensions: list[DslValue[TimestreamDimension]] = field(default_factory=list)
    role_arn: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    timestamp: DslValue[TimestreamTimestamp] | None = None


@dataclass
class TimestreamDimension(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TimestreamTimestamp(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TopicRulePayload(PropertyType):
    actions: list[DslValue[Action]] = field(default_factory=list)
    sql: DslValue[str] | None = None
    aws_iot_sql_version: DslValue[str] | None = None
    description: DslValue[str] | None = None
    error_action: DslValue[Action] | None = None
    rule_disabled: DslValue[bool] | None = None


@dataclass
class UserProperty(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
