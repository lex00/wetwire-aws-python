"""PropertyTypes for AWS::Lightsail::Distribution."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CacheBehavior(PropertyType):
    behavior: str | None = None


@dataclass
class CacheBehaviorPerPath(PropertyType):
    behavior: str | None = None
    path: str | None = None


@dataclass
class CacheSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_http_methods": "AllowedHTTPMethods",
        "cached_http_methods": "CachedHTTPMethods",
        "default_ttl": "DefaultTTL",
        "maximum_ttl": "MaximumTTL",
        "minimum_ttl": "MinimumTTL",
    }

    allowed_http_methods: str | None = None
    cached_http_methods: str | None = None
    default_ttl: int | None = None
    forwarded_cookies: CookieObject | None = None
    forwarded_headers: HeaderObject | None = None
    forwarded_query_strings: QueryStringObject | None = None
    maximum_ttl: int | None = None
    minimum_ttl: int | None = None


@dataclass
class CookieObject(PropertyType):
    cookies_allow_list: list[String] = field(default_factory=list)
    option: str | None = None


@dataclass
class HeaderObject(PropertyType):
    headers_allow_list: list[String] = field(default_factory=list)
    option: str | None = None


@dataclass
class InputOrigin(PropertyType):
    name: str | None = None
    protocol_policy: str | None = None
    region_name: str | None = None


@dataclass
class QueryStringObject(PropertyType):
    option: bool | None = None
    query_strings_allow_list: list[String] = field(default_factory=list)
