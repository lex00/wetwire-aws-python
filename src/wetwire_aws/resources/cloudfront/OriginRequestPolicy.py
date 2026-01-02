"""PropertyTypes for AWS::CloudFront::OriginRequestPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CookiesConfig(PropertyType):
    cookie_behavior: str | None = None
    cookies: list[String] = field(default_factory=list)


@dataclass
class HeadersConfig(PropertyType):
    header_behavior: str | None = None
    headers: list[String] = field(default_factory=list)


@dataclass
class OriginRequestPolicyConfig(PropertyType):
    cookies_config: CookiesConfig | None = None
    headers_config: HeadersConfig | None = None
    name: str | None = None
    query_strings_config: QueryStringsConfig | None = None
    comment: str | None = None


@dataclass
class QueryStringsConfig(PropertyType):
    query_string_behavior: str | None = None
    query_strings: list[String] = field(default_factory=list)
