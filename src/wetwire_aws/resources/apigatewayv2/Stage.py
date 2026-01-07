"""PropertyTypes for AWS::ApiGatewayV2::Stage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessLogSettings(PropertyType):
    destination_arn: DslValue[str] | None = None
    format: DslValue[str] | None = None


@dataclass
class RouteSettings(PropertyType):
    data_trace_enabled: DslValue[bool] | None = None
    detailed_metrics_enabled: DslValue[bool] | None = None
    logging_level: DslValue[str] | None = None
    throttling_burst_limit: DslValue[int] | None = None
    throttling_rate_limit: DslValue[float] | None = None
