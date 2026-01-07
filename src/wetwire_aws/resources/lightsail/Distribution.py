"""PropertyTypes for AWS::Lightsail::Distribution."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CacheBehavior(PropertyType):
    behavior: DslValue[str] | None = None


@dataclass
class CacheBehaviorPerPath(PropertyType):
    behavior: DslValue[str] | None = None
    path: DslValue[str] | None = None


@dataclass
class CacheSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allowed_http_methods": "AllowedHTTPMethods",
        "cached_http_methods": "CachedHTTPMethods",
        "default_ttl": "DefaultTTL",
        "maximum_ttl": "MaximumTTL",
        "minimum_ttl": "MinimumTTL",
    }

    allowed_http_methods: DslValue[str] | None = None
    cached_http_methods: DslValue[str] | None = None
    default_ttl: DslValue[int] | None = None
    forwarded_cookies: DslValue[CookieObject] | None = None
    forwarded_headers: DslValue[HeaderObject] | None = None
    forwarded_query_strings: DslValue[QueryStringObject] | None = None
    maximum_ttl: DslValue[int] | None = None
    minimum_ttl: DslValue[int] | None = None


@dataclass
class CookieObject(PropertyType):
    cookies_allow_list: list[DslValue[str]] = field(default_factory=list)
    option: DslValue[str] | None = None


@dataclass
class HeaderObject(PropertyType):
    headers_allow_list: list[DslValue[str]] = field(default_factory=list)
    option: DslValue[str] | None = None


@dataclass
class InputOrigin(PropertyType):
    name: DslValue[str] | None = None
    protocol_policy: DslValue[str] | None = None
    region_name: DslValue[str] | None = None


@dataclass
class QueryStringObject(PropertyType):
    option: DslValue[bool] | None = None
    query_strings_allow_list: list[DslValue[str]] = field(default_factory=list)
