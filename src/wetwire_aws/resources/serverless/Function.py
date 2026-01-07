"""PropertyTypes for AWS::Serverless::Function."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApiEvent(PropertyType):
    method: DslValue[str] | None = None
    path: DslValue[str] | None = None
    auth: DslValue[ApiEventAuth] | None = None
    rest_api_id: DslValue[str] | None = None


@dataclass
class ApiEventAuth(PropertyType):
    api_key_required: DslValue[bool] | None = None
    authorization_scopes: list[DslValue[str]] = field(default_factory=list)
    authorizer: DslValue[str] | None = None
    resource_policy: DslValue[dict[str, Any]] | None = None


@dataclass
class CloudWatchEvent(PropertyType):
    pattern: DslValue[dict[str, Any]] | None = None
    event_bus_name: DslValue[str] | None = None
    input: DslValue[str] | None = None


@dataclass
class CognitoEvent(PropertyType):
    trigger: DslValue[str] | None = None
    user_pool: DslValue[str] | None = None


@dataclass
class DeadLetterConfig(PropertyType):
    arn: DslValue[str] | None = None
    queue_logical_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DeadLetterQueue(PropertyType):
    target_arn: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class DynamoDBEvent(PropertyType):
    starting_position: DslValue[str] | None = None
    stream: DslValue[str] | None = None
    batch_size: DslValue[int] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class Environment(PropertyType):
    variables: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class EphemeralStorage(PropertyType):
    size: DslValue[int] | None = None


@dataclass
class EventBridgeRuleEvent(PropertyType):
    pattern: DslValue[dict[str, Any]] | None = None
    dead_letter_config: DslValue[DeadLetterConfig] | None = None
    event_bus_name: DslValue[str] | None = None
    input: DslValue[str] | None = None
    input_path: DslValue[str] | None = None
    retry_policy: DslValue[RetryPolicy] | None = None


@dataclass
class FunctionUrlConfig(PropertyType):
    auth_type: DslValue[str] | None = None
    cors: DslValue[FunctionUrlCors] | None = None
    invoke_mode: DslValue[str] | None = None


@dataclass
class FunctionUrlCors(PropertyType):
    allow_credentials: DslValue[bool] | None = None
    allow_headers: list[DslValue[str]] = field(default_factory=list)
    allow_methods: list[DslValue[str]] = field(default_factory=list)
    allow_origins: list[DslValue[str]] = field(default_factory=list)
    expose_headers: list[DslValue[str]] = field(default_factory=list)
    max_age: DslValue[int] | None = None


@dataclass
class HttpApiEvent(PropertyType):
    api_id: DslValue[str] | None = None
    auth: DslValue[HttpApiEventAuth] | None = None
    method: DslValue[str] | None = None
    path: DslValue[str] | None = None
    payload_format_version: DslValue[str] | None = None


@dataclass
class HttpApiEventAuth(PropertyType):
    authorization_scopes: list[DslValue[str]] = field(default_factory=list)
    authorizer: DslValue[str] | None = None


@dataclass
class KinesisEvent(PropertyType):
    starting_position: DslValue[str] | None = None
    stream: DslValue[str] | None = None
    batch_size: DslValue[int] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class LoggingConfig(PropertyType):
    application_log_level: DslValue[str] | None = None
    log_format: DslValue[str] | None = None
    log_group: DslValue[str] | None = None
    system_log_level: DslValue[str] | None = None


@dataclass
class ProvisionedConcurrencyConfig(PropertyType):
    provisioned_concurrent_executions: DslValue[int] | None = None


@dataclass
class RetryPolicy(PropertyType):
    maximum_event_age_in_seconds: DslValue[int] | None = None
    maximum_retry_attempts: DslValue[int] | None = None


@dataclass
class S3Event(PropertyType):
    bucket: DslValue[str] | None = None
    events: list[DslValue[str]] = field(default_factory=list)
    filter: DslValue[S3NotificationFilter] | None = None


@dataclass
class S3NotificationFilter(PropertyType):
    s3_key: DslValue[dict[str, Any]] | None = None


@dataclass
class SNSEvent(PropertyType):
    topic: DslValue[str] | None = None
    filter_policy: DslValue[dict[str, Any]] | None = None
    region: DslValue[str] | None = None


@dataclass
class SQSEvent(PropertyType):
    queue: DslValue[str] | None = None
    batch_size: DslValue[int] | None = None
    enabled: DslValue[bool] | None = None
    maximum_batching_window_in_seconds: DslValue[int] | None = None


@dataclass
class ScheduleEvent(PropertyType):
    schedule: DslValue[str] | None = None
    description: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None
    input: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class SnapStart(PropertyType):
    apply_on: DslValue[str] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
