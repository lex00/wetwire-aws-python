"""PropertyTypes for AWS::ApiGateway::Deployment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessLogSetting(PropertyType):
    destination_arn: DslValue[str] | None = None
    format: DslValue[str] | None = None


@dataclass
class CanarySetting(PropertyType):
    percent_traffic: DslValue[float] | None = None
    stage_variable_overrides: dict[str, DslValue[str]] = field(default_factory=dict)
    use_stage_cache: DslValue[bool] | None = None


@dataclass
class DeploymentCanarySettings(PropertyType):
    percent_traffic: DslValue[float] | None = None
    stage_variable_overrides: dict[str, DslValue[str]] = field(default_factory=dict)
    use_stage_cache: DslValue[bool] | None = None


@dataclass
class MethodSetting(PropertyType):
    cache_data_encrypted: DslValue[bool] | None = None
    cache_ttl_in_seconds: DslValue[int] | None = None
    caching_enabled: DslValue[bool] | None = None
    data_trace_enabled: DslValue[bool] | None = None
    http_method: DslValue[str] | None = None
    logging_level: DslValue[str] | None = None
    metrics_enabled: DslValue[bool] | None = None
    resource_path: DslValue[str] | None = None
    throttling_burst_limit: DslValue[int] | None = None
    throttling_rate_limit: DslValue[float] | None = None


@dataclass
class StageDescription(PropertyType):
    access_log_setting: DslValue[AccessLogSetting] | None = None
    cache_cluster_enabled: DslValue[bool] | None = None
    cache_cluster_size: DslValue[str] | None = None
    cache_data_encrypted: DslValue[bool] | None = None
    cache_ttl_in_seconds: DslValue[int] | None = None
    caching_enabled: DslValue[bool] | None = None
    canary_setting: DslValue[CanarySetting] | None = None
    client_certificate_id: DslValue[str] | None = None
    data_trace_enabled: DslValue[bool] | None = None
    description: DslValue[str] | None = None
    documentation_version: DslValue[str] | None = None
    logging_level: DslValue[str] | None = None
    method_settings: list[DslValue[MethodSetting]] = field(default_factory=list)
    metrics_enabled: DslValue[bool] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
    throttling_burst_limit: DslValue[int] | None = None
    throttling_rate_limit: DslValue[float] | None = None
    tracing_enabled: DslValue[bool] | None = None
    variables: dict[str, DslValue[str]] = field(default_factory=dict)
