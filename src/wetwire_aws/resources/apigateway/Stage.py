"""PropertyTypes for AWS::ApiGateway::Stage."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessLogSetting(PropertyType):
    destination_arn: str | None = None
    format: str | None = None


@dataclass
class CanarySetting(PropertyType):
    deployment_id: str | None = None
    percent_traffic: float | None = None
    stage_variable_overrides: dict[str, String] = field(default_factory=dict)
    use_stage_cache: bool | None = None


@dataclass
class MethodSetting(PropertyType):
    cache_data_encrypted: bool | None = None
    cache_ttl_in_seconds: int | None = None
    caching_enabled: bool | None = None
    data_trace_enabled: bool | None = None
    http_method: str | None = None
    logging_level: str | None = None
    metrics_enabled: bool | None = None
    resource_path: str | None = None
    throttling_burst_limit: int | None = None
    throttling_rate_limit: float | None = None
