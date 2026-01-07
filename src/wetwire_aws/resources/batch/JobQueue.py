"""PropertyTypes for AWS::Batch::JobQueue."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComputeEnvironmentOrder(PropertyType):
    compute_environment: DslValue[str] | None = None
    order: DslValue[int] | None = None


@dataclass
class JobStateTimeLimitAction(PropertyType):
    action: DslValue[str] | None = None
    max_time_seconds: DslValue[int] | None = None
    reason: DslValue[str] | None = None
    state: DslValue[str] | None = None


@dataclass
class ServiceEnvironmentOrder(PropertyType):
    order: DslValue[int] | None = None
    service_environment: DslValue[str] | None = None
