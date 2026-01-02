"""PropertyTypes for AWS::ElasticLoadBalancingV2::ListenerRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    type_: str | None = None
    authenticate_cognito_config: AuthenticateCognitoConfig | None = None
    authenticate_oidc_config: AuthenticateOidcConfig | None = None
    fixed_response_config: FixedResponseConfig | None = None
    forward_config: ForwardConfig | None = None
    jwt_validation_config: JwtValidationConfig | None = None
    order: int | None = None
    redirect_config: RedirectConfig | None = None
    target_group_arn: str | None = None


@dataclass
class AuthenticateCognitoConfig(PropertyType):
    user_pool_arn: str | None = None
    user_pool_client_id: str | None = None
    user_pool_domain: str | None = None
    authentication_request_extra_params: dict[str, String] = field(default_factory=dict)
    on_unauthenticated_request: str | None = None
    scope: str | None = None
    session_cookie_name: str | None = None
    session_timeout: int | None = None


@dataclass
class AuthenticateOidcConfig(PropertyType):
    authorization_endpoint: str | None = None
    client_id: str | None = None
    issuer: str | None = None
    token_endpoint: str | None = None
    user_info_endpoint: str | None = None
    authentication_request_extra_params: dict[str, String] = field(default_factory=dict)
    client_secret: str | None = None
    on_unauthenticated_request: str | None = None
    scope: str | None = None
    session_cookie_name: str | None = None
    session_timeout: int | None = None
    use_existing_client_secret: bool | None = None


@dataclass
class FixedResponseConfig(PropertyType):
    status_code: str | None = None
    content_type: str | None = None
    message_body: str | None = None


@dataclass
class ForwardConfig(PropertyType):
    target_group_stickiness_config: TargetGroupStickinessConfig | None = None
    target_groups: list[TargetGroupTuple] = field(default_factory=list)


@dataclass
class HostHeaderConfig(PropertyType):
    regex_values: list[String] = field(default_factory=list)
    values: list[String] = field(default_factory=list)


@dataclass
class HttpHeaderConfig(PropertyType):
    http_header_name: str | None = None
    regex_values: list[String] = field(default_factory=list)
    values: list[String] = field(default_factory=list)


@dataclass
class HttpRequestMethodConfig(PropertyType):
    values: list[String] = field(default_factory=list)


@dataclass
class JwtValidationActionAdditionalClaim(PropertyType):
    format: str | None = None
    name: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class JwtValidationConfig(PropertyType):
    issuer: str | None = None
    jwks_endpoint: str | None = None
    additional_claims: list[JwtValidationActionAdditionalClaim] = field(
        default_factory=list
    )


@dataclass
class PathPatternConfig(PropertyType):
    regex_values: list[String] = field(default_factory=list)
    values: list[String] = field(default_factory=list)


@dataclass
class QueryStringConfig(PropertyType):
    values: list[QueryStringKeyValue] = field(default_factory=list)


@dataclass
class QueryStringKeyValue(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class RedirectConfig(PropertyType):
    status_code: str | None = None
    host: str | None = None
    path: str | None = None
    port: str | None = None
    protocol: str | None = None
    query: str | None = None


@dataclass
class RewriteConfig(PropertyType):
    regex: str | None = None
    replace: str | None = None


@dataclass
class RewriteConfigObject(PropertyType):
    rewrites: list[RewriteConfig] = field(default_factory=list)


@dataclass
class RuleCondition(PropertyType):
    field_: str | None = None
    host_header_config: HostHeaderConfig | None = None
    http_header_config: HttpHeaderConfig | None = None
    http_request_method_config: HttpRequestMethodConfig | None = None
    path_pattern_config: PathPatternConfig | None = None
    query_string_config: QueryStringConfig | None = None
    regex_values: list[String] = field(default_factory=list)
    source_ip_config: SourceIpConfig | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class SourceIpConfig(PropertyType):
    values: list[String] = field(default_factory=list)


@dataclass
class TargetGroupStickinessConfig(PropertyType):
    duration_seconds: int | None = None
    enabled: bool | None = None


@dataclass
class TargetGroupTuple(PropertyType):
    target_group_arn: str | None = None
    weight: int | None = None


@dataclass
class Transform(PropertyType):
    type_: str | None = None
    host_header_rewrite_config: RewriteConfigObject | None = None
    url_rewrite_config: RewriteConfigObject | None = None
