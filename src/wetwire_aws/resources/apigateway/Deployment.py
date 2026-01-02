"""PropertyTypes for AWS::ApiGateway::Deployment."""

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
    percent_traffic: float | None = None
    stage_variable_overrides: dict[str, String] = field(default_factory=dict)
    use_stage_cache: bool | None = None


@dataclass
class DeploymentCanarySettings(PropertyType):
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


@dataclass
class StageDescription(PropertyType):
    access_log_setting: AccessLogSetting | None = None
    cache_cluster_enabled: bool | None = None
    cache_cluster_size: str | None = None
    cache_data_encrypted: bool | None = None
    cache_ttl_in_seconds: int | None = None
    caching_enabled: bool | None = None
    canary_setting: CanarySetting | None = None
    client_certificate_id: str | None = None
    data_trace_enabled: bool | None = None
    description: str | None = None
    documentation_version: str | None = None
    logging_level: str | None = None
    method_settings: list[MethodSetting] = field(default_factory=list)
    metrics_enabled: bool | None = None
    tags: list[Tag] = field(default_factory=list)
    throttling_burst_limit: int | None = None
    throttling_rate_limit: float | None = None
    tracing_enabled: bool | None = None
    variables: dict[str, String] = field(default_factory=dict)
