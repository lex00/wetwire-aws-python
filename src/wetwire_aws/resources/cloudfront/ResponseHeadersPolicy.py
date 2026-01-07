"""PropertyTypes for AWS::CloudFront::ResponseHeadersPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessControlAllowHeaders(PropertyType):
    items: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AccessControlAllowMethods(PropertyType):
    items: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AccessControlAllowOrigins(PropertyType):
    items: list[DslValue[str]] = field(default_factory=list)


@dataclass
class AccessControlExposeHeaders(PropertyType):
    items: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ContentSecurityPolicy(PropertyType):
    content_security_policy: DslValue[str] | None = None
    override: DslValue[bool] | None = None


@dataclass
class ContentTypeOptions(PropertyType):
    override: DslValue[bool] | None = None


@dataclass
class CorsConfig(PropertyType):
    access_control_allow_credentials: DslValue[bool] | None = None
    access_control_allow_headers: DslValue[AccessControlAllowHeaders] | None = None
    access_control_allow_methods: DslValue[AccessControlAllowMethods] | None = None
    access_control_allow_origins: DslValue[AccessControlAllowOrigins] | None = None
    origin_override: DslValue[bool] | None = None
    access_control_expose_headers: DslValue[AccessControlExposeHeaders] | None = None
    access_control_max_age_sec: DslValue[int] | None = None


@dataclass
class CustomHeader(PropertyType):
    header: DslValue[str] | None = None
    override: DslValue[bool] | None = None
    value: DslValue[str] | None = None


@dataclass
class CustomHeadersConfig(PropertyType):
    items: list[DslValue[CustomHeader]] = field(default_factory=list)


@dataclass
class FrameOptions(PropertyType):
    frame_option: DslValue[str] | None = None
    override: DslValue[bool] | None = None


@dataclass
class ReferrerPolicy(PropertyType):
    override: DslValue[bool] | None = None
    referrer_policy: DslValue[str] | None = None


@dataclass
class RemoveHeader(PropertyType):
    header: DslValue[str] | None = None


@dataclass
class RemoveHeadersConfig(PropertyType):
    items: list[DslValue[RemoveHeader]] = field(default_factory=list)


@dataclass
class ResponseHeadersPolicyConfig(PropertyType):
    name: DslValue[str] | None = None
    comment: DslValue[str] | None = None
    cors_config: DslValue[CorsConfig] | None = None
    custom_headers_config: DslValue[CustomHeadersConfig] | None = None
    remove_headers_config: DslValue[RemoveHeadersConfig] | None = None
    security_headers_config: DslValue[SecurityHeadersConfig] | None = None
    server_timing_headers_config: DslValue[ServerTimingHeadersConfig] | None = None


@dataclass
class SecurityHeadersConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "xss_protection": "XSSProtection",
    }

    content_security_policy: DslValue[ContentSecurityPolicy] | None = None
    content_type_options: DslValue[ContentTypeOptions] | None = None
    frame_options: DslValue[FrameOptions] | None = None
    referrer_policy: DslValue[ReferrerPolicy] | None = None
    strict_transport_security: DslValue[StrictTransportSecurity] | None = None
    xss_protection: DslValue[XSSProtection] | None = None


@dataclass
class ServerTimingHeadersConfig(PropertyType):
    enabled: DslValue[bool] | None = None
    sampling_rate: DslValue[float] | None = None


@dataclass
class StrictTransportSecurity(PropertyType):
    access_control_max_age_sec: DslValue[int] | None = None
    override: DslValue[bool] | None = None
    include_subdomains: DslValue[bool] | None = None
    preload: DslValue[bool] | None = None


@dataclass
class XSSProtection(PropertyType):
    override: DslValue[bool] | None = None
    protection: DslValue[bool] | None = None
    mode_block: DslValue[bool] | None = None
    report_uri: DslValue[str] | None = None
