"""PropertyTypes for AWS::WorkSpacesWeb::DataProtectionSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomPattern(PropertyType):
    pattern_name: str | None = None
    pattern_regex: str | None = None
    keyword_regex: str | None = None
    pattern_description: str | None = None


@dataclass
class InlineRedactionConfiguration(PropertyType):
    inline_redaction_patterns: list[InlineRedactionPattern] = field(
        default_factory=list
    )
    global_confidence_level: float | None = None
    global_enforced_urls: list[String] = field(default_factory=list)
    global_exempt_urls: list[String] = field(default_factory=list)


@dataclass
class InlineRedactionPattern(PropertyType):
    redaction_place_holder: RedactionPlaceHolder | None = None
    built_in_pattern_id: str | None = None
    confidence_level: float | None = None
    custom_pattern: CustomPattern | None = None
    enforced_urls: list[String] = field(default_factory=list)
    exempt_urls: list[String] = field(default_factory=list)


@dataclass
class RedactionPlaceHolder(PropertyType):
    redaction_place_holder_type: str | None = None
    redaction_place_holder_text: str | None = None
