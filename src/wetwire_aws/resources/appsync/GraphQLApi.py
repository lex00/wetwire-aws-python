"""PropertyTypes for AWS::AppSync::GraphQLApi."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdditionalAuthenticationProvider(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "open_id_connect_config": "OpenIDConnectConfig",
    }

    authentication_type: DslValue[str] | None = None
    lambda_authorizer_config: DslValue[LambdaAuthorizerConfig] | None = None
    open_id_connect_config: DslValue[OpenIDConnectConfig] | None = None
    user_pool_config: DslValue[CognitoUserPoolConfig] | None = None


@dataclass
class CognitoUserPoolConfig(PropertyType):
    app_id_client_regex: DslValue[str] | None = None
    aws_region: DslValue[str] | None = None
    user_pool_id: DslValue[str] | None = None


@dataclass
class EnhancedMetricsConfig(PropertyType):
    data_source_level_metrics_behavior: DslValue[str] | None = None
    operation_level_metrics_config: DslValue[str] | None = None
    resolver_level_metrics_behavior: DslValue[str] | None = None


@dataclass
class LambdaAuthorizerConfig(PropertyType):
    authorizer_result_ttl_in_seconds: DslValue[float] | None = None
    authorizer_uri: DslValue[str] | None = None
    identity_validation_expression: DslValue[str] | None = None


@dataclass
class LogConfig(PropertyType):
    cloud_watch_logs_role_arn: DslValue[str] | None = None
    field_log_level: DslValue[str] | None = None
    exclude_verbose_content: DslValue[bool] | None = None


@dataclass
class OpenIDConnectConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_ttl": "AuthTTL",
        "iat_ttl": "IatTTL",
    }

    auth_ttl: DslValue[float] | None = None
    client_id: DslValue[str] | None = None
    iat_ttl: DslValue[float] | None = None
    issuer: DslValue[str] | None = None


@dataclass
class UserPoolConfig(PropertyType):
    app_id_client_regex: DslValue[str] | None = None
    aws_region: DslValue[str] | None = None
    default_action: DslValue[str] | None = None
    user_pool_id: DslValue[str] | None = None
