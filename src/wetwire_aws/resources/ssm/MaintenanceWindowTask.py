"""PropertyTypes for AWS::SSM::MaintenanceWindowTask."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudWatchOutputConfig(PropertyType):
    cloud_watch_log_group_name: DslValue[str] | None = None
    cloud_watch_output_enabled: DslValue[bool] | None = None


@dataclass
class LoggingInfo(PropertyType):
    region: DslValue[str] | None = None
    s3_bucket: DslValue[str] | None = None
    s3_prefix: DslValue[str] | None = None


@dataclass
class MaintenanceWindowAutomationParameters(PropertyType):
    document_version: DslValue[str] | None = None
    parameters: DslValue[dict[str, Any]] | None = None


@dataclass
class MaintenanceWindowLambdaParameters(PropertyType):
    client_context: DslValue[str] | None = None
    payload: DslValue[str] | None = None
    qualifier: DslValue[str] | None = None


@dataclass
class MaintenanceWindowRunCommandParameters(PropertyType):
    cloud_watch_output_config: DslValue[CloudWatchOutputConfig] | None = None
    comment: DslValue[str] | None = None
    document_hash: DslValue[str] | None = None
    document_hash_type: DslValue[str] | None = None
    document_version: DslValue[str] | None = None
    notification_config: DslValue[NotificationConfig] | None = None
    output_s3_bucket_name: DslValue[str] | None = None
    output_s3_key_prefix: DslValue[str] | None = None
    parameters: DslValue[dict[str, Any]] | None = None
    service_role_arn: DslValue[str] | None = None
    timeout_seconds: DslValue[int] | None = None


@dataclass
class MaintenanceWindowStepFunctionsParameters(PropertyType):
    input: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class NotificationConfig(PropertyType):
    notification_arn: DslValue[str] | None = None
    notification_events: list[DslValue[str]] = field(default_factory=list)
    notification_type: DslValue[str] | None = None


@dataclass
class Target(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class TaskInvocationParameters(PropertyType):
    maintenance_window_automation_parameters: (
        DslValue[MaintenanceWindowAutomationParameters] | None
    ) = None
    maintenance_window_lambda_parameters: (
        DslValue[MaintenanceWindowLambdaParameters] | None
    ) = None
    maintenance_window_run_command_parameters: (
        DslValue[MaintenanceWindowRunCommandParameters] | None
    ) = None
    maintenance_window_step_functions_parameters: (
        DslValue[MaintenanceWindowStepFunctionsParameters] | None
    ) = None
