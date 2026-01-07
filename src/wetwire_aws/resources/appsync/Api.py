"""PropertyTypes for AWS::AppSync::Api."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuthMode(PropertyType):
    auth_type: DslValue[str] | None = None


@dataclass
class AuthProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_config": "OpenIDConnectConfig",
    }

    auth_type: DslValue[str] | None = None
    cognito_config: DslValue[CognitoConfig] | None = None
    lambda_authorizer_config: DslValue[LambdaAuthorizerConfig] | None = None
    open_id_connect_config: DslValue[OpenIDConnectConfig] | None = None


@dataclass
class CognitoConfig(PropertyType):
    aws_region: DslValue[str] | None = None
    user_pool_id: DslValue[str] | None = None
    app_id_client_regex: DslValue[str] | None = None


@dataclass
class DnsMap(PropertyType):
    http: DslValue[str] | None = None
    realtime: DslValue[str] | None = None


@dataclass
class EventConfig(PropertyType):
    auth_providers: list[DslValue[AuthProvider]] = field(default_factory=list)
    connection_auth_modes: list[DslValue[AuthMode]] = field(default_factory=list)
    default_publish_auth_modes: list[DslValue[AuthMode]] = field(default_factory=list)
    default_subscribe_auth_modes: list[DslValue[AuthMode]] = field(default_factory=list)
    log_config: DslValue[EventLogConfig] | None = None


@dataclass
class EventLogConfig(PropertyType):
    cloud_watch_logs_role_arn: DslValue[str] | None = None
    log_level: DslValue[str] | None = None


@dataclass
class LambdaAuthorizerConfig(PropertyType):
    authorizer_uri: DslValue[str] | None = None
    authorizer_result_ttl_in_seconds: DslValue[int] | None = None
    identity_validation_expression: DslValue[str] | None = None


@dataclass
class OpenIDConnectConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_ttl": "AuthTTL",
        "iat_ttl": "IatTTL",
    }

    issuer: DslValue[str] | None = None
    auth_ttl: DslValue[float] | None = None
    client_id: DslValue[str] | None = None
    iat_ttl: DslValue[float] | None = None
