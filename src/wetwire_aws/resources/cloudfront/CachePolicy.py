"""PropertyTypes for AWS::CloudFront::CachePolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CachePolicyConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "default_ttl": "DefaultTTL",
        "max_ttl": "MaxTTL",
        "min_ttl": "MinTTL",
    }

    default_ttl: DslValue[float] | None = None
    max_ttl: DslValue[float] | None = None
    min_ttl: DslValue[float] | None = None
    name: DslValue[str] | None = None
    parameters_in_cache_key_and_forwarded_to_origin: (
        DslValue[ParametersInCacheKeyAndForwardedToOrigin] | None
    ) = None
    comment: DslValue[str] | None = None


@dataclass
class CookiesConfig(PropertyType):
    cookie_behavior: DslValue[str] | None = None
    cookies: list[DslValue[str]] = field(default_factory=list)


@dataclass
class HeadersConfig(PropertyType):
    header_behavior: DslValue[str] | None = None
    headers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ParametersInCacheKeyAndForwardedToOrigin(PropertyType):
    cookies_config: DslValue[CookiesConfig] | None = None
    enable_accept_encoding_gzip: DslValue[bool] | None = None
    headers_config: DslValue[HeadersConfig] | None = None
    query_strings_config: DslValue[QueryStringsConfig] | None = None
    enable_accept_encoding_brotli: DslValue[bool] | None = None


@dataclass
class QueryStringsConfig(PropertyType):
    query_string_behavior: DslValue[str] | None = None
    query_strings: list[DslValue[str]] = field(default_factory=list)
