"""PropertyTypes for AWS::Serverless::HttpApi."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CorsConfiguration(PropertyType):
    allow_credentials: DslValue[bool] | None = None
    allow_headers: list[DslValue[str]] = field(default_factory=list)
    allow_methods: list[DslValue[str]] = field(default_factory=list)
    allow_origins: list[DslValue[str]] = field(default_factory=list)
    expose_headers: list[DslValue[str]] = field(default_factory=list)
    max_age: DslValue[int] | None = None


@dataclass
class HttpApiAuth(PropertyType):
    authorizers: dict[str, DslValue[HttpApiAuthorizer]] = field(default_factory=dict)
    default_authorizer: DslValue[str] | None = None


@dataclass
class HttpApiAuthorizer(PropertyType):
    authorization_scopes: list[DslValue[str]] = field(default_factory=list)
    authorizer_payload_format_version: DslValue[str] | None = None
    enable_simple_responses: DslValue[bool] | None = None
    function_arn: DslValue[str] | None = None
    function_invoke_role: DslValue[str] | None = None
    identity_source: DslValue[str] | None = None
    jwt_configuration: DslValue[dict[str, Any]] | None = None


@dataclass
class RouteSettings(PropertyType):
    throttling_burst_limit: DslValue[int] | None = None
    throttling_rate_limit: DslValue[float] | None = None
