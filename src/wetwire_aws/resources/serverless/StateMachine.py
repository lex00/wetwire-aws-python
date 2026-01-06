"""PropertyTypes for AWS::Serverless::StateMachine."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LogDestination(PropertyType):
    cloud_watch_logs_log_group: dict[str, Any] | None = None


@dataclass
class LoggingConfiguration(PropertyType):
    destinations: list[LogDestination] = field(default_factory=list)
    include_execution_data: bool | None = None
    level: str | None = None


@dataclass
class TracingConfiguration(PropertyType):
    enabled: bool | None = None
