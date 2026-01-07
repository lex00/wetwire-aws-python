"""PropertyTypes for AWS::CloudFront::OriginRequestPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CookiesConfig(PropertyType):
    cookie_behavior: DslValue[str] | None = None
    cookies: list[DslValue[str]] = field(default_factory=list)


@dataclass
class HeadersConfig(PropertyType):
    header_behavior: DslValue[str] | None = None
    headers: list[DslValue[str]] = field(default_factory=list)


@dataclass
class OriginRequestPolicyConfig(PropertyType):
    cookies_config: DslValue[CookiesConfig] | None = None
    headers_config: DslValue[HeadersConfig] | None = None
    name: DslValue[str] | None = None
    query_strings_config: DslValue[QueryStringsConfig] | None = None
    comment: DslValue[str] | None = None


@dataclass
class QueryStringsConfig(PropertyType):
    query_string_behavior: DslValue[str] | None = None
    query_strings: list[DslValue[str]] = field(default_factory=list)
