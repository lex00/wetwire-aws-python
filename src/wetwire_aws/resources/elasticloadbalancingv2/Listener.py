"""PropertyTypes for AWS::ElasticLoadBalancingV2::Listener."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    type_: DslValue[str] | None = None
    authenticate_cognito_config: DslValue[AuthenticateCognitoConfig] | None = None
    authenticate_oidc_config: DslValue[AuthenticateOidcConfig] | None = None
    fixed_response_config: DslValue[FixedResponseConfig] | None = None
    forward_config: DslValue[ForwardConfig] | None = None
    jwt_validation_config: DslValue[JwtValidationConfig] | None = None
    order: DslValue[int] | None = None
    redirect_config: DslValue[RedirectConfig] | None = None
    target_group_arn: DslValue[str] | None = None


@dataclass
class AuthenticateCognitoConfig(PropertyType):
    user_pool_arn: DslValue[str] | None = None
    user_pool_client_id: DslValue[str] | None = None
    user_pool_domain: DslValue[str] | None = None
    authentication_request_extra_params: dict[str, DslValue[str]] = field(
        default_factory=dict
    )
    on_unauthenticated_request: DslValue[str] | None = None
    scope: DslValue[str] | None = None
    session_cookie_name: DslValue[str] | None = None
    session_timeout: DslValue[str] | None = None


@dataclass
class AuthenticateOidcConfig(PropertyType):
    authorization_endpoint: DslValue[str] | None = None
    client_id: DslValue[str] | None = None
    issuer: DslValue[str] | None = None
    token_endpoint: DslValue[str] | None = None
    user_info_endpoint: DslValue[str] | None = None
    authentication_request_extra_params: dict[str, DslValue[str]] = field(
        default_factory=dict
    )
    client_secret: DslValue[str] | None = None
    on_unauthenticated_request: DslValue[str] | None = None
    scope: DslValue[str] | None = None
    session_cookie_name: DslValue[str] | None = None
    session_timeout: DslValue[str] | None = None
    use_existing_client_secret: DslValue[bool] | None = None


@dataclass
class Certificate(PropertyType):
    certificate_arn: DslValue[str] | None = None


@dataclass
class FixedResponseConfig(PropertyType):
    status_code: DslValue[str] | None = None
    content_type: DslValue[str] | None = None
    message_body: DslValue[str] | None = None


@dataclass
class ForwardConfig(PropertyType):
    target_group_stickiness_config: DslValue[TargetGroupStickinessConfig] | None = None
    target_groups: list[DslValue[TargetGroupTuple]] = field(default_factory=list)


@dataclass
class JwtValidationActionAdditionalClaim(PropertyType):
    format: DslValue[str] | None = None
    name: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class JwtValidationConfig(PropertyType):
    issuer: DslValue[str] | None = None
    jwks_endpoint: DslValue[str] | None = None
    additional_claims: list[DslValue[JwtValidationActionAdditionalClaim]] = field(
        default_factory=list
    )


@dataclass
class ListenerAttribute(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class MutualAuthentication(PropertyType):
    advertise_trust_store_ca_names: DslValue[str] | None = None
    ignore_client_certificate_expiry: DslValue[bool] | None = None
    mode: DslValue[str] | None = None
    trust_store_arn: DslValue[str] | None = None


@dataclass
class RedirectConfig(PropertyType):
    status_code: DslValue[str] | None = None
    host: DslValue[str] | None = None
    path: DslValue[str] | None = None
    port: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
    query: DslValue[str] | None = None


@dataclass
class TargetGroupStickinessConfig(PropertyType):
    duration_seconds: DslValue[int] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class TargetGroupTuple(PropertyType):
    target_group_arn: DslValue[str] | None = None
    weight: DslValue[int] | None = None
