"""PropertyTypes for AWS::AppSync::Api."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthMode(PropertyType):
    auth_type: str | None = None


@dataclass
class AuthProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_config": "OpenIDConnectConfig",
    }

    auth_type: str | None = None
    cognito_config: CognitoConfig | None = None
    lambda_authorizer_config: LambdaAuthorizerConfig | None = None
    open_id_connect_config: OpenIDConnectConfig | None = None


@dataclass
class CognitoConfig(PropertyType):
    aws_region: str | None = None
    user_pool_id: str | None = None
    app_id_client_regex: str | None = None


@dataclass
class DnsMap(PropertyType):
    http: str | None = None
    realtime: str | None = None


@dataclass
class EventConfig(PropertyType):
    auth_providers: list[AuthProvider] = field(default_factory=list)
    connection_auth_modes: list[AuthMode] = field(default_factory=list)
    default_publish_auth_modes: list[AuthMode] = field(default_factory=list)
    default_subscribe_auth_modes: list[AuthMode] = field(default_factory=list)
    log_config: EventLogConfig | None = None


@dataclass
class EventLogConfig(PropertyType):
    cloud_watch_logs_role_arn: str | None = None
    log_level: str | None = None


@dataclass
class LambdaAuthorizerConfig(PropertyType):
    authorizer_uri: str | None = None
    authorizer_result_ttl_in_seconds: int | None = None
    identity_validation_expression: str | None = None


@dataclass
class OpenIDConnectConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_ttl": "AuthTTL",
        "iat_ttl": "IatTTL",
    }

    issuer: str | None = None
    auth_ttl: float | None = None
    client_id: str | None = None
    iat_ttl: float | None = None
