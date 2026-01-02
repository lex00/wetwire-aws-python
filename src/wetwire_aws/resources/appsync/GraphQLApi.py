"""PropertyTypes for AWS::AppSync::GraphQLApi."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdditionalAuthenticationProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_config": "OpenIDConnectConfig",
    }

    authentication_type: str | None = None
    lambda_authorizer_config: LambdaAuthorizerConfig | None = None
    open_id_connect_config: OpenIDConnectConfig | None = None
    user_pool_config: CognitoUserPoolConfig | None = None


@dataclass
class CognitoUserPoolConfig(PropertyType):
    app_id_client_regex: str | None = None
    aws_region: str | None = None
    user_pool_id: str | None = None


@dataclass
class EnhancedMetricsConfig(PropertyType):
    data_source_level_metrics_behavior: str | None = None
    operation_level_metrics_config: str | None = None
    resolver_level_metrics_behavior: str | None = None


@dataclass
class LambdaAuthorizerConfig(PropertyType):
    authorizer_result_ttl_in_seconds: float | None = None
    authorizer_uri: str | None = None
    identity_validation_expression: str | None = None


@dataclass
class LogConfig(PropertyType):
    cloud_watch_logs_role_arn: str | None = None
    field_log_level: str | None = None
    exclude_verbose_content: bool | None = None


@dataclass
class OpenIDConnectConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_ttl": "AuthTTL",
        "iat_ttl": "IatTTL",
    }

    auth_ttl: float | None = None
    client_id: str | None = None
    iat_ttl: float | None = None
    issuer: str | None = None


@dataclass
class UserPoolConfig(PropertyType):
    app_id_client_regex: str | None = None
    aws_region: str | None = None
    default_action: str | None = None
    user_pool_id: str | None = None
