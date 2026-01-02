"""PropertyTypes for AWS::MWAA::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LoggingConfiguration(PropertyType):
    dag_processing_logs: ModuleLoggingConfiguration | None = None
    scheduler_logs: ModuleLoggingConfiguration | None = None
    task_logs: ModuleLoggingConfiguration | None = None
    webserver_logs: ModuleLoggingConfiguration | None = None
    worker_logs: ModuleLoggingConfiguration | None = None


@dataclass
class ModuleLoggingConfiguration(PropertyType):
    cloud_watch_log_group_arn: str | None = None
    enabled: bool | None = None
    log_level: str | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnet_ids: list[String] = field(default_factory=list)
