"""PropertyTypes for AWS::CloudFront::CachePolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CachePolicyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_ttl": "DefaultTTL",
        "max_ttl": "MaxTTL",
        "min_ttl": "MinTTL",
    }

    default_ttl: float | None = None
    max_ttl: float | None = None
    min_ttl: float | None = None
    name: str | None = None
    parameters_in_cache_key_and_forwarded_to_origin: (
        ParametersInCacheKeyAndForwardedToOrigin | None
    ) = None
    comment: str | None = None


@dataclass
class CookiesConfig(PropertyType):
    cookie_behavior: str | None = None
    cookies: list[String] = field(default_factory=list)


@dataclass
class HeadersConfig(PropertyType):
    header_behavior: str | None = None
    headers: list[String] = field(default_factory=list)


@dataclass
class ParametersInCacheKeyAndForwardedToOrigin(PropertyType):
    cookies_config: CookiesConfig | None = None
    enable_accept_encoding_gzip: bool | None = None
    headers_config: HeadersConfig | None = None
    query_strings_config: QueryStringsConfig | None = None
    enable_accept_encoding_brotli: bool | None = None


@dataclass
class QueryStringsConfig(PropertyType):
    query_string_behavior: str | None = None
    query_strings: list[String] = field(default_factory=list)
