"""PropertyTypes for AWS::Glue::Job."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectionsList(PropertyType):
    connections: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ExecutionProperty(PropertyType):
    max_concurrent_runs: DslValue[float] | None = None


@dataclass
class JobCommand(PropertyType):
    name: DslValue[str] | None = None
    python_version: DslValue[str] | None = None
    runtime: DslValue[str] | None = None
    script_location: DslValue[str] | None = None


@dataclass
class NotificationProperty(PropertyType):
    notify_delay_after: DslValue[int] | None = None
