"""PropertyTypes for AWS::MWAA::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LoggingConfiguration(PropertyType):
    dag_processing_logs: DslValue[ModuleLoggingConfiguration] | None = None
    scheduler_logs: DslValue[ModuleLoggingConfiguration] | None = None
    task_logs: DslValue[ModuleLoggingConfiguration] | None = None
    webserver_logs: DslValue[ModuleLoggingConfiguration] | None = None
    worker_logs: DslValue[ModuleLoggingConfiguration] | None = None


@dataclass
class ModuleLoggingConfiguration(PropertyType):
    cloud_watch_log_group_arn: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None
    log_level: DslValue[str] | None = None


@dataclass
class NetworkConfiguration(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnet_ids: list[DslValue[str]] = field(default_factory=list)
