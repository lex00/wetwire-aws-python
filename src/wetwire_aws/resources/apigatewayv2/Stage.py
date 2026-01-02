"""PropertyTypes for AWS::ApiGatewayV2::Stage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessLogSettings(PropertyType):
    destination_arn: str | None = None
    format: str | None = None


@dataclass
class RouteSettings(PropertyType):
    data_trace_enabled: bool | None = None
    detailed_metrics_enabled: bool | None = None
    logging_level: str | None = None
    throttling_burst_limit: int | None = None
    throttling_rate_limit: float | None = None
