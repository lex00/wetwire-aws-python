"""PropertyTypes for AWS::ApiGateway::UsagePlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApiStage(PropertyType):
    api_id: str | None = None
    stage: str | None = None
    throttle: dict[str, ThrottleSettings] = field(default_factory=dict)


@dataclass
class QuotaSettings(PropertyType):
    limit: int | None = None
    offset: int | None = None
    period: str | None = None


@dataclass
class ThrottleSettings(PropertyType):
    burst_limit: int | None = None
    rate_limit: float | None = None
