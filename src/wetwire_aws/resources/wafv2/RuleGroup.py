"""PropertyTypes for AWS::WAFv2::RuleGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AllowAction(PropertyType):
    custom_request_handling: CustomRequestHandling | None = None


@dataclass
class AndStatement(PropertyType):
    statements: list[Statement] = field(default_factory=list)


@dataclass
class AsnMatchStatement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forwarded_ip_config": "ForwardedIPConfig",
    }

    asn_list: list[Integer] = field(default_factory=list)
    forwarded_ip_config: ForwardedIPConfiguration | None = None


@dataclass
class BlockAction(PropertyType):
    custom_response: CustomResponse | None = None


@dataclass
class Body(PropertyType):
    oversize_handling: str | None = None


@dataclass
class ByteMatchStatement(PropertyType):
    field_to_match: FieldToMatch | None = None
    positional_constraint: str | None = None
    text_transformations: list[TextTransformation] = field(default_factory=list)
    search_string: str | None = None
    search_string_base64: str | None = None


@dataclass
class CaptchaAction(PropertyType):
    custom_request_handling: CustomRequestHandling | None = None


@dataclass
class CaptchaConfig(PropertyType):
    immunity_time_property: ImmunityTimeProperty | None = None


@dataclass
class ChallengeAction(PropertyType):
    custom_request_handling: CustomRequestHandling | None = None


@dataclass
class ChallengeConfig(PropertyType):
    immunity_time_property: ImmunityTimeProperty | None = None


@dataclass
class CookieMatchPattern(PropertyType):
    all: dict[str, Any] | None = None
    excluded_cookies: list[String] = field(default_factory=list)
    included_cookies: list[String] = field(default_factory=list)


@dataclass
class Cookies(PropertyType):
    match_pattern: CookieMatchPattern | None = None
    match_scope: str | None = None
    oversize_handling: str | None = None


@dataclass
class CountAction(PropertyType):
    custom_request_handling: CustomRequestHandling | None = None


@dataclass
class CustomHTTPHeader(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class CustomRequestHandling(PropertyType):
    insert_headers: list[CustomHTTPHeader] = field(default_factory=list)


@dataclass
class CustomResponse(PropertyType):
    response_code: int | None = None
    custom_response_body_key: str | None = None
    response_headers: list[CustomHTTPHeader] = field(default_factory=list)


@dataclass
class CustomResponseBody(PropertyType):
    content: str | None = None
    content_type: str | None = None


@dataclass
class FieldToMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ja3_fingerprint": "JA3Fingerprint",
        "ja4_fingerprint": "JA4Fingerprint",
    }

    all_query_arguments: dict[str, Any] | None = None
    body: Body | None = None
    cookies: Cookies | None = None
    headers: Headers | None = None
    ja3_fingerprint: JA3Fingerprint | None = None
    ja4_fingerprint: JA4Fingerprint | None = None
    json_body: JsonBody | None = None
    method: dict[str, Any] | None = None
    query_string: dict[str, Any] | None = None
    single_header: SingleHeader | None = None
    single_query_argument: SingleQueryArgument | None = None
    uri_fragment: UriFragment | None = None
    uri_path: dict[str, Any] | None = None


@dataclass
class ForwardedIPConfiguration(PropertyType):
    fallback_behavior: str | None = None
    header_name: str | None = None


@dataclass
class GeoMatchStatement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forwarded_ip_config": "ForwardedIPConfig",
    }

    country_codes: list[String] = field(default_factory=list)
    forwarded_ip_config: ForwardedIPConfiguration | None = None


@dataclass
class HeaderMatchPattern(PropertyType):
    all: dict[str, Any] | None = None
    excluded_headers: list[String] = field(default_factory=list)
    included_headers: list[String] = field(default_factory=list)


@dataclass
class Headers(PropertyType):
    match_pattern: HeaderMatchPattern | None = None
    match_scope: str | None = None
    oversize_handling: str | None = None


@dataclass
class IPSetForwardedIPConfiguration(PropertyType):
    fallback_behavior: str | None = None
    header_name: str | None = None
    position: str | None = None


@dataclass
class IPSetReferenceStatement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_set_forwarded_ip_config": "IPSetForwardedIPConfig",
    }

    arn: str | None = None
    ip_set_forwarded_ip_config: IPSetForwardedIPConfiguration | None = None


@dataclass
class ImmunityTimeProperty(PropertyType):
    immunity_time: int | None = None


@dataclass
class JA3Fingerprint(PropertyType):
    fallback_behavior: str | None = None


@dataclass
class JA4Fingerprint(PropertyType):
    fallback_behavior: str | None = None


@dataclass
class JsonBody(PropertyType):
    match_pattern: JsonMatchPattern | None = None
    match_scope: str | None = None
    invalid_fallback_behavior: str | None = None
    oversize_handling: str | None = None


@dataclass
class JsonMatchPattern(PropertyType):
    all: dict[str, Any] | None = None
    included_paths: list[String] = field(default_factory=list)


@dataclass
class Label(PropertyType):
    name: str | None = None


@dataclass
class LabelMatchStatement(PropertyType):
    key: str | None = None
    scope: str | None = None


@dataclass
class LabelSummary(PropertyType):
    name: str | None = None


@dataclass
class NotStatement(PropertyType):
    statement: Statement | None = None


@dataclass
class OrStatement(PropertyType):
    statements: list[Statement] = field(default_factory=list)


@dataclass
class RateBasedStatement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forwarded_ip_config": "ForwardedIPConfig",
    }

    aggregate_key_type: str | None = None
    limit: int | None = None
    custom_keys: list[RateBasedStatementCustomKey] = field(default_factory=list)
    evaluation_window_sec: int | None = None
    forwarded_ip_config: ForwardedIPConfiguration | None = None
    scope_down_statement: Statement | None = None


@dataclass
class RateBasedStatementCustomKey(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "asn": "ASN",
        "forwarded_ip": "ForwardedIP",
        "http_method": "HTTPMethod",
        "ip": "IP",
        "ja3_fingerprint": "JA3Fingerprint",
        "ja4_fingerprint": "JA4Fingerprint",
    }

    asn: dict[str, Any] | None = None
    cookie: RateLimitCookie | None = None
    forwarded_ip: dict[str, Any] | None = None
    header: RateLimitHeader | None = None
    http_method: dict[str, Any] | None = None
    ip: dict[str, Any] | None = None
    ja3_fingerprint: RateLimitJA3Fingerprint | None = None
    ja4_fingerprint: RateLimitJA4Fingerprint | None = None
    label_namespace: RateLimitLabelNamespace | None = None
    query_argument: RateLimitQueryArgument | None = None
    query_string: RateLimitQueryString | None = None
    uri_path: RateLimitUriPath | None = None


@dataclass
class RateLimitCookie(PropertyType):
    name: str | None = None
    text_transformations: list[TextTransformation] = field(default_factory=list)


@dataclass
class RateLimitHeader(PropertyType):
    name: str | None = None
    text_transformations: list[TextTransformation] = field(default_factory=list)


@dataclass
class RateLimitJA3Fingerprint(PropertyType):
    fallback_behavior: str | None = None


@dataclass
class RateLimitJA4Fingerprint(PropertyType):
    fallback_behavior: str | None = None


@dataclass
class RateLimitLabelNamespace(PropertyType):
    namespace: str | None = None


@dataclass
class RateLimitQueryArgument(PropertyType):
    name: str | None = None
    text_transformations: list[TextTransformation] = field(default_factory=list)


@dataclass
class RateLimitQueryString(PropertyType):
    text_transformations: list[TextTransformation] = field(default_factory=list)


@dataclass
class RateLimitUriPath(PropertyType):
    text_transformations: list[TextTransformation] = field(default_factory=list)


@dataclass
class RegexMatchStatement(PropertyType):
    field_to_match: FieldToMatch | None = None
    regex_string: str | None = None
    text_transformations: list[TextTransformation] = field(default_factory=list)


@dataclass
class RegexPatternSetReferenceStatement(PropertyType):
    arn: str | None = None
    field_to_match: FieldToMatch | None = None
    text_transformations: list[TextTransformation] = field(default_factory=list)


@dataclass
class Rule(PropertyType):
    name: str | None = None
    priority: int | None = None
    statement: Statement | None = None
    visibility_config: VisibilityConfig | None = None
    action: RuleAction | None = None
    captcha_config: CaptchaConfig | None = None
    challenge_config: ChallengeConfig | None = None
    rule_labels: list[Label] = field(default_factory=list)


@dataclass
class RuleAction(PropertyType):
    allow: AllowAction | None = None
    block: BlockAction | None = None
    captcha: CaptchaAction | None = None
    challenge: ChallengeAction | None = None
    count: CountAction | None = None


@dataclass
class SingleHeader(PropertyType):
    name: str | None = None


@dataclass
class SingleQueryArgument(PropertyType):
    name: str | None = None


@dataclass
class SizeConstraintStatement(PropertyType):
    comparison_operator: str | None = None
    field_to_match: FieldToMatch | None = None
    size: float | None = None
    text_transformations: list[TextTransformation] = field(default_factory=list)


@dataclass
class SqliMatchStatement(PropertyType):
    field_to_match: FieldToMatch | None = None
    text_transformations: list[TextTransformation] = field(default_factory=list)
    sensitivity_level: str | None = None


@dataclass
class Statement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_set_reference_statement": "IPSetReferenceStatement",
    }

    and_statement: AndStatement | None = None
    asn_match_statement: AsnMatchStatement | None = None
    byte_match_statement: ByteMatchStatement | None = None
    geo_match_statement: GeoMatchStatement | None = None
    ip_set_reference_statement: IPSetReferenceStatement | None = None
    label_match_statement: LabelMatchStatement | None = None
    not_statement: NotStatement | None = None
    or_statement: OrStatement | None = None
    rate_based_statement: RateBasedStatement | None = None
    regex_match_statement: RegexMatchStatement | None = None
    regex_pattern_set_reference_statement: RegexPatternSetReferenceStatement | None = (
        None
    )
    size_constraint_statement: SizeConstraintStatement | None = None
    sqli_match_statement: SqliMatchStatement | None = None
    xss_match_statement: XssMatchStatement | None = None


@dataclass
class TextTransformation(PropertyType):
    priority: int | None = None
    type_: str | None = None


@dataclass
class UriFragment(PropertyType):
    fallback_behavior: str | None = None


@dataclass
class VisibilityConfig(PropertyType):
    cloud_watch_metrics_enabled: bool | None = None
    metric_name: str | None = None
    sampled_requests_enabled: bool | None = None


@dataclass
class XssMatchStatement(PropertyType):
    field_to_match: FieldToMatch | None = None
    text_transformations: list[TextTransformation] = field(default_factory=list)
