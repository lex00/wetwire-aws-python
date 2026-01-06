"""PropertyTypes for AWS::Serverless::HttpApi."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CorsConfiguration(PropertyType):
    allow_credentials: bool | None = None
    allow_headers: list[str] = field(default_factory=list)
    allow_methods: list[str] = field(default_factory=list)
    allow_origins: list[str] = field(default_factory=list)
    expose_headers: list[str] = field(default_factory=list)
    max_age: int | None = None


@dataclass
class HttpApiAuth(PropertyType):
    authorizers: dict[str, HttpApiAuthorizer] = field(default_factory=dict)
    default_authorizer: str | None = None


@dataclass
class HttpApiAuthorizer(PropertyType):
    authorization_scopes: list[str] = field(default_factory=list)
    authorizer_payload_format_version: str | None = None
    enable_simple_responses: bool | None = None
    function_arn: str | None = None
    function_invoke_role: str | None = None
    identity_source: str | None = None
    jwt_configuration: dict[str, Any] | None = None


@dataclass
class RouteSettings(PropertyType):
    throttling_burst_limit: int | None = None
    throttling_rate_limit: float | None = None
