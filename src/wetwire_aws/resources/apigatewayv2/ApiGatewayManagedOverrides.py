"""PropertyTypes for AWS::ApiGatewayV2::ApiGatewayManagedOverrides."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessLogSettings(PropertyType):
    destination_arn: str | None = None
    format: str | None = None


@dataclass
class IntegrationOverrides(PropertyType):
    description: str | None = None
    integration_method: str | None = None
    payload_format_version: str | None = None
    timeout_in_millis: int | None = None


@dataclass
class RouteOverrides(PropertyType):
    authorization_scopes: list[String] = field(default_factory=list)
    authorization_type: str | None = None
    authorizer_id: str | None = None
    operation_name: str | None = None
    target: str | None = None


@dataclass
class RouteSettings(PropertyType):
    data_trace_enabled: bool | None = None
    detailed_metrics_enabled: bool | None = None
    logging_level: str | None = None
    throttling_burst_limit: int | None = None
    throttling_rate_limit: float | None = None


@dataclass
class StageOverrides(PropertyType):
    access_log_settings: AccessLogSettings | None = None
    auto_deploy: bool | None = None
    default_route_settings: RouteSettings | None = None
    description: str | None = None
    route_settings: dict[str, Any] | None = None
    stage_variables: dict[str, Any] | None = None
