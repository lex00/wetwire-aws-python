"""PropertyTypes for AWS::Glue::Job."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConnectionsList(PropertyType):
    connections: list[String] = field(default_factory=list)


@dataclass
class ExecutionProperty(PropertyType):
    max_concurrent_runs: float | None = None


@dataclass
class JobCommand(PropertyType):
    name: str | None = None
    python_version: str | None = None
    runtime: str | None = None
    script_location: str | None = None


@dataclass
class NotificationProperty(PropertyType):
    notify_delay_after: int | None = None
