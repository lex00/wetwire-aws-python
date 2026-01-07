"""PropertyTypes for AWS::WAFv2::RuleGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AllowAction(PropertyType):
    custom_request_handling: DslValue[CustomRequestHandling] | None = None


@dataclass
class AndStatement(PropertyType):
    statements: list[DslValue[Statement]] = field(default_factory=list)


@dataclass
class AsnMatchStatement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forwarded_ip_config": "ForwardedIPConfig",
    }

    asn_list: list[DslValue[int]] = field(default_factory=list)
    forwarded_ip_config: DslValue[ForwardedIPConfiguration] | None = None


@dataclass
class BlockAction(PropertyType):
    custom_response: DslValue[CustomResponse] | None = None


@dataclass
class Body(PropertyType):
    oversize_handling: DslValue[str] | None = None


@dataclass
class ByteMatchStatement(PropertyType):
    field_to_match: DslValue[FieldToMatch] | None = None
    positional_constraint: DslValue[str] | None = None
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )
    search_string: DslValue[str] | None = None
    search_string_base64: DslValue[str] | None = None


@dataclass
class CaptchaAction(PropertyType):
    custom_request_handling: DslValue[CustomRequestHandling] | None = None


@dataclass
class CaptchaConfig(PropertyType):
    immunity_time_property: DslValue[ImmunityTimeProperty] | None = None


@dataclass
class ChallengeAction(PropertyType):
    custom_request_handling: DslValue[CustomRequestHandling] | None = None


@dataclass
class ChallengeConfig(PropertyType):
    immunity_time_property: DslValue[ImmunityTimeProperty] | None = None


@dataclass
class CookieMatchPattern(PropertyType):
    all: DslValue[dict[str, Any]] | None = None
    excluded_cookies: list[DslValue[str]] = field(default_factory=list)
    included_cookies: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Cookies(PropertyType):
    match_pattern: DslValue[CookieMatchPattern] | None = None
    match_scope: DslValue[str] | None = None
    oversize_handling: DslValue[str] | None = None


@dataclass
class CountAction(PropertyType):
    custom_request_handling: DslValue[CustomRequestHandling] | None = None


@dataclass
class CustomHTTPHeader(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class CustomRequestHandling(PropertyType):
    insert_headers: list[DslValue[CustomHTTPHeader]] = field(default_factory=list)


@dataclass
class CustomResponse(PropertyType):
    response_code: DslValue[int] | None = None
    custom_response_body_key: DslValue[str] | None = None
    response_headers: list[DslValue[CustomHTTPHeader]] = field(default_factory=list)


@dataclass
class CustomResponseBody(PropertyType):
    content: DslValue[str] | None = None
    content_type: DslValue[str] | None = None


@dataclass
class FieldToMatch(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ja3_fingerprint": "JA3Fingerprint",
        "ja4_fingerprint": "JA4Fingerprint",
    }

    all_query_arguments: DslValue[dict[str, Any]] | None = None
    body: DslValue[Body] | None = None
    cookies: DslValue[Cookies] | None = None
    headers: DslValue[Headers] | None = None
    ja3_fingerprint: DslValue[JA3Fingerprint] | None = None
    ja4_fingerprint: DslValue[JA4Fingerprint] | None = None
    json_body: DslValue[JsonBody] | None = None
    method: DslValue[dict[str, Any]] | None = None
    query_string: DslValue[dict[str, Any]] | None = None
    single_header: DslValue[SingleHeader] | None = None
    single_query_argument: DslValue[SingleQueryArgument] | None = None
    uri_fragment: DslValue[UriFragment] | None = None
    uri_path: DslValue[dict[str, Any]] | None = None


@dataclass
class ForwardedIPConfiguration(PropertyType):
    fallback_behavior: DslValue[str] | None = None
    header_name: DslValue[str] | None = None


@dataclass
class GeoMatchStatement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forwarded_ip_config": "ForwardedIPConfig",
    }

    country_codes: list[DslValue[str]] = field(default_factory=list)
    forwarded_ip_config: DslValue[ForwardedIPConfiguration] | None = None


@dataclass
class HeaderMatchPattern(PropertyType):
    all: DslValue[dict[str, Any]] | None = None
    excluded_headers: list[DslValue[str]] = field(default_factory=list)
    included_headers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Headers(PropertyType):
    match_pattern: DslValue[HeaderMatchPattern] | None = None
    match_scope: DslValue[str] | None = None
    oversize_handling: DslValue[str] | None = None


@dataclass
class IPSetForwardedIPConfiguration(PropertyType):
    fallback_behavior: DslValue[str] | None = None
    header_name: DslValue[str] | None = None
    position: DslValue[str] | None = None


@dataclass
class IPSetReferenceStatement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_set_forwarded_ip_config": "IPSetForwardedIPConfig",
    }

    arn: DslValue[str] | None = None
    ip_set_forwarded_ip_config: DslValue[IPSetForwardedIPConfiguration] | None = None


@dataclass
class ImmunityTimeProperty(PropertyType):
    immunity_time: DslValue[int] | None = None


@dataclass
class JA3Fingerprint(PropertyType):
    fallback_behavior: DslValue[str] | None = None


@dataclass
class JA4Fingerprint(PropertyType):
    fallback_behavior: DslValue[str] | None = None


@dataclass
class JsonBody(PropertyType):
    match_pattern: DslValue[JsonMatchPattern] | None = None
    match_scope: DslValue[str] | None = None
    invalid_fallback_behavior: DslValue[str] | None = None
    oversize_handling: DslValue[str] | None = None


@dataclass
class JsonMatchPattern(PropertyType):
    all: DslValue[dict[str, Any]] | None = None
    included_paths: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Label(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class LabelMatchStatement(PropertyType):
    key: DslValue[str] | None = None
    scope: DslValue[str] | None = None


@dataclass
class LabelSummary(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class NotStatement(PropertyType):
    statement: DslValue[Statement] | None = None


@dataclass
class OrStatement(PropertyType):
    statements: list[DslValue[Statement]] = field(default_factory=list)


@dataclass
class RateBasedStatement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "forwarded_ip_config": "ForwardedIPConfig",
    }

    aggregate_key_type: DslValue[str] | None = None
    limit: DslValue[int] | None = None
    custom_keys: list[DslValue[RateBasedStatementCustomKey]] = field(
        default_factory=list
    )
    evaluation_window_sec: DslValue[int] | None = None
    forwarded_ip_config: DslValue[ForwardedIPConfiguration] | None = None
    scope_down_statement: DslValue[Statement] | None = None


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

    asn: DslValue[dict[str, Any]] | None = None
    cookie: DslValue[RateLimitCookie] | None = None
    forwarded_ip: DslValue[dict[str, Any]] | None = None
    header: DslValue[RateLimitHeader] | None = None
    http_method: DslValue[dict[str, Any]] | None = None
    ip: DslValue[dict[str, Any]] | None = None
    ja3_fingerprint: DslValue[RateLimitJA3Fingerprint] | None = None
    ja4_fingerprint: DslValue[RateLimitJA4Fingerprint] | None = None
    label_namespace: DslValue[RateLimitLabelNamespace] | None = None
    query_argument: DslValue[RateLimitQueryArgument] | None = None
    query_string: DslValue[RateLimitQueryString] | None = None
    uri_path: DslValue[RateLimitUriPath] | None = None


@dataclass
class RateLimitCookie(PropertyType):
    name: DslValue[str] | None = None
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )


@dataclass
class RateLimitHeader(PropertyType):
    name: DslValue[str] | None = None
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )


@dataclass
class RateLimitJA3Fingerprint(PropertyType):
    fallback_behavior: DslValue[str] | None = None


@dataclass
class RateLimitJA4Fingerprint(PropertyType):
    fallback_behavior: DslValue[str] | None = None


@dataclass
class RateLimitLabelNamespace(PropertyType):
    namespace: DslValue[str] | None = None


@dataclass
class RateLimitQueryArgument(PropertyType):
    name: DslValue[str] | None = None
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )


@dataclass
class RateLimitQueryString(PropertyType):
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )


@dataclass
class RateLimitUriPath(PropertyType):
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )


@dataclass
class RegexMatchStatement(PropertyType):
    field_to_match: DslValue[FieldToMatch] | None = None
    regex_string: DslValue[str] | None = None
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )


@dataclass
class RegexPatternSetReferenceStatement(PropertyType):
    arn: DslValue[str] | None = None
    field_to_match: DslValue[FieldToMatch] | None = None
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )


@dataclass
class Rule(PropertyType):
    name: DslValue[str] | None = None
    priority: DslValue[int] | None = None
    statement: DslValue[Statement] | None = None
    visibility_config: DslValue[VisibilityConfig] | None = None
    action: DslValue[RuleAction] | None = None
    captcha_config: DslValue[CaptchaConfig] | None = None
    challenge_config: DslValue[ChallengeConfig] | None = None
    rule_labels: list[DslValue[Label]] = field(default_factory=list)


@dataclass
class RuleAction(PropertyType):
    allow: DslValue[AllowAction] | None = None
    block: DslValue[BlockAction] | None = None
    captcha: DslValue[CaptchaAction] | None = None
    challenge: DslValue[ChallengeAction] | None = None
    count: DslValue[CountAction] | None = None


@dataclass
class SingleHeader(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class SingleQueryArgument(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class SizeConstraintStatement(PropertyType):
    comparison_operator: DslValue[str] | None = None
    field_to_match: DslValue[FieldToMatch] | None = None
    size: DslValue[float] | None = None
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )


@dataclass
class SqliMatchStatement(PropertyType):
    field_to_match: DslValue[FieldToMatch] | None = None
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )
    sensitivity_level: DslValue[str] | None = None


@dataclass
class Statement(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ip_set_reference_statement": "IPSetReferenceStatement",
    }

    and_statement: DslValue[AndStatement] | None = None
    asn_match_statement: DslValue[AsnMatchStatement] | None = None
    byte_match_statement: DslValue[ByteMatchStatement] | None = None
    geo_match_statement: DslValue[GeoMatchStatement] | None = None
    ip_set_reference_statement: DslValue[IPSetReferenceStatement] | None = None
    label_match_statement: DslValue[LabelMatchStatement] | None = None
    not_statement: DslValue[NotStatement] | None = None
    or_statement: DslValue[OrStatement] | None = None
    rate_based_statement: DslValue[RateBasedStatement] | None = None
    regex_match_statement: DslValue[RegexMatchStatement] | None = None
    regex_pattern_set_reference_statement: (
        DslValue[RegexPatternSetReferenceStatement] | None
    ) = None
    size_constraint_statement: DslValue[SizeConstraintStatement] | None = None
    sqli_match_statement: DslValue[SqliMatchStatement] | None = None
    xss_match_statement: DslValue[XssMatchStatement] | None = None


@dataclass
class TextTransformation(PropertyType):
    priority: DslValue[int] | None = None
    type_: DslValue[str] | None = None


@dataclass
class UriFragment(PropertyType):
    fallback_behavior: DslValue[str] | None = None


@dataclass
class VisibilityConfig(PropertyType):
    cloud_watch_metrics_enabled: DslValue[bool] | None = None
    metric_name: DslValue[str] | None = None
    sampled_requests_enabled: DslValue[bool] | None = None


@dataclass
class XssMatchStatement(PropertyType):
    field_to_match: DslValue[FieldToMatch] | None = None
    text_transformations: list[DslValue[TextTransformation]] = field(
        default_factory=list
    )
