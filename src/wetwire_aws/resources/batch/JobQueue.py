"""PropertyTypes for AWS::Batch::JobQueue."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComputeEnvironmentOrder(PropertyType):
    compute_environment: str | None = None
    order: int | None = None


@dataclass
class JobStateTimeLimitAction(PropertyType):
    action: str | None = None
    max_time_seconds: int | None = None
    reason: str | None = None
    state: str | None = None


@dataclass
class ServiceEnvironmentOrder(PropertyType):
    order: int | None = None
    service_environment: str | None = None
