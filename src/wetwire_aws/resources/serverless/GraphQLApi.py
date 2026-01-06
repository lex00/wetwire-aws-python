"""PropertyTypes for AWS::Serverless::GraphQLApi."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdditionalAuth(PropertyType):
    type_: str | None = None
    lambda_authorizer: LambdaAuthorizerConfig | None = None
    open_id_connect: OpenIdConnectConfig | None = None
    user_pool: CognitoUserPoolConfig | None = None


@dataclass
class CognitoUserPoolConfig(PropertyType):
    user_pool_id: str | None = None
    app_id_client_regex: str | None = None
    aws_region: str | None = None
    default_action: str | None = None


@dataclass
class GraphQLAuth(PropertyType):
    type_: str | None = None
    additional: list[AdditionalAuth] = field(default_factory=list)
    lambda_authorizer: LambdaAuthorizerConfig | None = None
    open_id_connect: OpenIdConnectConfig | None = None
    user_pool: CognitoUserPoolConfig | None = None


@dataclass
class LambdaAuthorizerConfig(PropertyType):
    authorizer_uri: str | None = None
    authorizer_result_ttl_in_seconds: int | None = None
    identity_validation_expression: str | None = None


@dataclass
class OpenIdConnectConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auth_ttl": "AuthTTL",
        "iat_ttl": "IatTTL",
    }

    issuer: str | None = None
    auth_ttl: int | None = None
    client_id: str | None = None
    iat_ttl: int | None = None
