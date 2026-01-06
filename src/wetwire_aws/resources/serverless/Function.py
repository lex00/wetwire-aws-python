"""PropertyTypes for AWS::Serverless::Function."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApiEvent(PropertyType):
    method: str | None = None
    path: str | None = None
    auth: ApiEventAuth | None = None
    rest_api_id: str | None = None


@dataclass
class ApiEventAuth(PropertyType):
    api_key_required: bool | None = None
    authorization_scopes: list[str] = field(default_factory=list)
    authorizer: str | None = None
    resource_policy: dict[str, Any] | None = None


@dataclass
class CloudWatchEvent(PropertyType):
    pattern: dict[str, Any] | None = None
    event_bus_name: str | None = None
    input: str | None = None


@dataclass
class CognitoEvent(PropertyType):
    trigger: str | None = None
    user_pool: str | None = None


@dataclass
class DeadLetterConfig(PropertyType):
    arn: str | None = None
    queue_logical_id: str | None = None
    type_: str | None = None


@dataclass
class DeadLetterQueue(PropertyType):
    target_arn: str | None = None
    type_: str | None = None


@dataclass
class DynamoDBEvent(PropertyType):
    starting_position: str | None = None
    stream: str | None = None
    batch_size: int | None = None
    enabled: bool | None = None


@dataclass
class Environment(PropertyType):
    variables: dict[str, str] = field(default_factory=dict)


@dataclass
class EphemeralStorage(PropertyType):
    size: int | None = None


@dataclass
class EventBridgeRuleEvent(PropertyType):
    pattern: dict[str, Any] | None = None
    dead_letter_config: DeadLetterConfig | None = None
    event_bus_name: str | None = None
    input: str | None = None
    input_path: str | None = None
    retry_policy: RetryPolicy | None = None


@dataclass
class FunctionUrlConfig(PropertyType):
    auth_type: str | None = None
    cors: FunctionUrlCors | None = None
    invoke_mode: str | None = None


@dataclass
class FunctionUrlCors(PropertyType):
    allow_credentials: bool | None = None
    allow_headers: list[str] = field(default_factory=list)
    allow_methods: list[str] = field(default_factory=list)
    allow_origins: list[str] = field(default_factory=list)
    expose_headers: list[str] = field(default_factory=list)
    max_age: int | None = None


@dataclass
class HttpApiEvent(PropertyType):
    api_id: str | None = None
    auth: HttpApiEventAuth | None = None
    method: str | None = None
    path: str | None = None
    payload_format_version: str | None = None


@dataclass
class HttpApiEventAuth(PropertyType):
    authorization_scopes: list[str] = field(default_factory=list)
    authorizer: str | None = None


@dataclass
class KinesisEvent(PropertyType):
    starting_position: str | None = None
    stream: str | None = None
    batch_size: int | None = None
    enabled: bool | None = None


@dataclass
class LoggingConfig(PropertyType):
    application_log_level: str | None = None
    log_format: str | None = None
    log_group: str | None = None
    system_log_level: str | None = None


@dataclass
class ProvisionedConcurrencyConfig(PropertyType):
    provisioned_concurrent_executions: int | None = None


@dataclass
class RetryPolicy(PropertyType):
    maximum_event_age_in_seconds: int | None = None
    maximum_retry_attempts: int | None = None


@dataclass
class S3Event(PropertyType):
    bucket: str | None = None
    events: list[str] = field(default_factory=list)
    filter: S3NotificationFilter | None = None


@dataclass
class S3NotificationFilter(PropertyType):
    s3_key: dict[str, Any] | None = None


@dataclass
class SNSEvent(PropertyType):
    topic: str | None = None
    filter_policy: dict[str, Any] | None = None
    region: str | None = None


@dataclass
class SQSEvent(PropertyType):
    queue: str | None = None
    batch_size: int | None = None
    enabled: bool | None = None
    maximum_batching_window_in_seconds: int | None = None


@dataclass
class ScheduleEvent(PropertyType):
    schedule: str | None = None
    description: str | None = None
    enabled: bool | None = None
    input: str | None = None
    name: str | None = None


@dataclass
class SnapStart(PropertyType):
    apply_on: str | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[str] = field(default_factory=list)
    subnet_ids: list[str] = field(default_factory=list)
