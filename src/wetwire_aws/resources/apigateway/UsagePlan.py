"""PropertyTypes for AWS::ApiGateway::UsagePlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApiStage(PropertyType):
    api_id: DslValue[str] | None = None
    stage: DslValue[str] | None = None
    throttle: dict[str, DslValue[ThrottleSettings]] = field(default_factory=dict)


@dataclass
class QuotaSettings(PropertyType):
    limit: DslValue[int] | None = None
    offset: DslValue[int] | None = None
    period: DslValue[str] | None = None


@dataclass
class ThrottleSettings(PropertyType):
    burst_limit: DslValue[int] | None = None
    rate_limit: DslValue[float] | None = None
