"""PropertyTypes for AWS::Serverless::GraphQLApi."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdditionalAuth(PropertyType):
    type_: DslValue[str] | None = None
    lambda_authorizer: DslValue[LambdaAuthorizerConfig] | None = None
    open_id_connect: DslValue[OpenIdConnectConfig] | None = None
    user_pool: DslValue[CognitoUserPoolConfig] | None = None


@dataclass
class CognitoUserPoolConfig(PropertyType):
    user_pool_id: DslValue[str] | None = None
    app_id_client_regex: DslValue[str] | None = None
    aws_region: DslValue[str] | None = None
    default_action: DslValue[str] | None = None


@dataclass
class GraphQLAuth(PropertyType):
    type_: DslValue[str] | None = None
    additional: list[DslValue[AdditionalAuth]] = field(default_factory=list)
    lambda_authorizer: DslValue[LambdaAuthorizerConfig] | None = None
    open_id_connect: DslValue[OpenIdConnectConfig] | None = None
    user_pool: DslValue[CognitoUserPoolConfig] | None = None


@dataclass
class LambdaAuthorizerConfig(PropertyType):
    authorizer_uri: DslValue[str] | None = None
    authorizer_result_ttl_in_seconds: DslValue[int] | None = None
    identity_validation_expression: DslValue[str] | None = None


@dataclass
class OpenIdConnectConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_ttl": "AuthTTL",
        "iat_ttl": "IatTTL",
    }

    issuer: DslValue[str] | None = None
    auth_ttl: DslValue[int] | None = None
    client_id: DslValue[str] | None = None
    iat_ttl: DslValue[int] | None = None
