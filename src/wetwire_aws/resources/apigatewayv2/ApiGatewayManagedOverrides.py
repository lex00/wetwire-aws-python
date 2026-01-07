"""PropertyTypes for AWS::ApiGatewayV2::ApiGatewayManagedOverrides."""

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
class IntegrationOverrides(PropertyType):
    description: DslValue[str] | None = None
    integration_method: DslValue[str] | None = None
    payload_format_version: DslValue[str] | None = None
    timeout_in_millis: DslValue[int] | None = None


@dataclass
class RouteOverrides(PropertyType):
    authorization_scopes: list[DslValue[str]] = field(default_factory=list)
    authorization_type: DslValue[str] | None = None
    authorizer_id: DslValue[str] | None = None
    operation_name: DslValue[str] | None = None
    target: DslValue[str] | None = None


@dataclass
class RouteSettings(PropertyType):
    data_trace_enabled: DslValue[bool] | None = None
    detailed_metrics_enabled: DslValue[bool] | None = None
    logging_level: DslValue[str] | None = None
    throttling_burst_limit: DslValue[int] | None = None
    throttling_rate_limit: DslValue[float] | None = None


@dataclass
class StageOverrides(PropertyType):
    access_log_settings: DslValue[AccessLogSettings] | None = None
    auto_deploy: DslValue[bool] | None = None
    default_route_settings: DslValue[RouteSettings] | None = None
    description: DslValue[str] | None = None
    route_settings: DslValue[dict[str, Any]] | None = None
    stage_variables: DslValue[dict[str, Any]] | None = None
