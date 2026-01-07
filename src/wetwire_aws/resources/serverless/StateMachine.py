"""PropertyTypes for AWS::Serverless::StateMachine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LogDestination(PropertyType):
    cloud_watch_logs_log_group: DslValue[dict[str, Any]] | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    destinations: list[DslValue[LogDestination]] = field(default_factory=list)
    include_execution_data: DslValue[bool] | None = None
    level: DslValue[str] | None = None


@dataclass
class TracingConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
