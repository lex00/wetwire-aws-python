"""PropertyTypes for AWS::SSM::MaintenanceWindowTask."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudWatchOutputConfig(PropertyType):
    cloud_watch_log_group_name: str | None = None
    cloud_watch_output_enabled: bool | None = None


@dataclass
class LoggingInfo(PropertyType):
    region: str | None = None
    s3_bucket: str | None = None
    s3_prefix: str | None = None


@dataclass
class MaintenanceWindowAutomationParameters(PropertyType):
    document_version: str | None = None
    parameters: dict[str, Any] | None = None


@dataclass
class MaintenanceWindowLambdaParameters(PropertyType):
    client_context: str | None = None
    payload: str | None = None
    qualifier: str | None = None


@dataclass
class MaintenanceWindowRunCommandParameters(PropertyType):
    cloud_watch_output_config: CloudWatchOutputConfig | None = None
    comment: str | None = None
    document_hash: str | None = None
    document_hash_type: str | None = None
    document_version: str | None = None
    notification_config: NotificationConfig | None = None
    output_s3_bucket_name: str | None = None
    output_s3_key_prefix: str | None = None
    parameters: dict[str, Any] | None = None
    service_role_arn: str | None = None
    timeout_seconds: int | None = None


@dataclass
class MaintenanceWindowStepFunctionsParameters(PropertyType):
    input: str | None = None
    name: str | None = None


@dataclass
class NotificationConfig(PropertyType):
    notification_arn: str | None = None
    notification_events: list[String] = field(default_factory=list)
    notification_type: str | None = None


@dataclass
class Target(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class TaskInvocationParameters(PropertyType):
    maintenance_window_automation_parameters: (
        MaintenanceWindowAutomationParameters | None
    ) = None
    maintenance_window_lambda_parameters: MaintenanceWindowLambdaParameters | None = (
        None
    )
    maintenance_window_run_command_parameters: (
        MaintenanceWindowRunCommandParameters | None
    ) = None
    maintenance_window_step_functions_parameters: (
        MaintenanceWindowStepFunctionsParameters | None
    ) = None
