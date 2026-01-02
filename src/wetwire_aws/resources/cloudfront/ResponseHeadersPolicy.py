"""PropertyTypes for AWS::CloudFront::ResponseHeadersPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessControlAllowHeaders(PropertyType):
    items: list[String] = field(default_factory=list)


@dataclass
class AccessControlAllowMethods(PropertyType):
    items: list[String] = field(default_factory=list)


@dataclass
class AccessControlAllowOrigins(PropertyType):
    items: list[String] = field(default_factory=list)


@dataclass
class AccessControlExposeHeaders(PropertyType):
    items: list[String] = field(default_factory=list)


@dataclass
class ContentSecurityPolicy(PropertyType):
    content_security_policy: str | None = None
    override: bool | None = None


@dataclass
class ContentTypeOptions(PropertyType):
    override: bool | None = None


@dataclass
class CorsConfig(PropertyType):
    access_control_allow_credentials: bool | None = None
    access_control_allow_headers: AccessControlAllowHeaders | None = None
    access_control_allow_methods: AccessControlAllowMethods | None = None
    access_control_allow_origins: AccessControlAllowOrigins | None = None
    origin_override: bool | None = None
    access_control_expose_headers: AccessControlExposeHeaders | None = None
    access_control_max_age_sec: int | None = None


@dataclass
class CustomHeader(PropertyType):
    header: str | None = None
    override: bool | None = None
    value: str | None = None


@dataclass
class CustomHeadersConfig(PropertyType):
    items: list[CustomHeader] = field(default_factory=list)


@dataclass
class FrameOptions(PropertyType):
    frame_option: str | None = None
    override: bool | None = None


@dataclass
class ReferrerPolicy(PropertyType):
    override: bool | None = None
    referrer_policy: str | None = None


@dataclass
class RemoveHeader(PropertyType):
    header: str | None = None


@dataclass
class RemoveHeadersConfig(PropertyType):
    items: list[RemoveHeader] = field(default_factory=list)


@dataclass
class ResponseHeadersPolicyConfig(PropertyType):
    name: str | None = None
    comment: str | None = None
    cors_config: CorsConfig | None = None
    custom_headers_config: CustomHeadersConfig | None = None
    remove_headers_config: RemoveHeadersConfig | None = None
    security_headers_config: SecurityHeadersConfig | None = None
    server_timing_headers_config: ServerTimingHeadersConfig | None = None


@dataclass
class SecurityHeadersConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "xss_protection": "XSSProtection",
    }

    content_security_policy: ContentSecurityPolicy | None = None
    content_type_options: ContentTypeOptions | None = None
    frame_options: FrameOptions | None = None
    referrer_policy: ReferrerPolicy | None = None
    strict_transport_security: StrictTransportSecurity | None = None
    xss_protection: XSSProtection | None = None


@dataclass
class ServerTimingHeadersConfig(PropertyType):
    enabled: bool | None = None
    sampling_rate: float | None = None


@dataclass
class StrictTransportSecurity(PropertyType):
    access_control_max_age_sec: int | None = None
    override: bool | None = None
    include_subdomains: bool | None = None
    preload: bool | None = None


@dataclass
class XSSProtection(PropertyType):
    override: bool | None = None
    protection: bool | None = None
    mode_block: bool | None = None
    report_uri: str | None = None
