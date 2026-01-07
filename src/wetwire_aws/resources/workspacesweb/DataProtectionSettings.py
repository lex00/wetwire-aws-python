"""PropertyTypes for AWS::WorkSpacesWeb::DataProtectionSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomPattern(PropertyType):
    pattern_name: DslValue[str] | None = None
    pattern_regex: DslValue[str] | None = None
    keyword_regex: DslValue[str] | None = None
    pattern_description: DslValue[str] | None = None


@dataclass
class InlineRedactionConfiguration(PropertyType):
    inline_redaction_patterns: list[DslValue[InlineRedactionPattern]] = field(
        default_factory=list
    )
    global_confidence_level: DslValue[float] | None = None
    global_enforced_urls: list[DslValue[str]] = field(default_factory=list)
    global_exempt_urls: list[DslValue[str]] = field(default_factory=list)


@dataclass
class InlineRedactionPattern(PropertyType):
    redaction_place_holder: DslValue[RedactionPlaceHolder] | None = None
    built_in_pattern_id: DslValue[str] | None = None
    confidence_level: DslValue[float] | None = None
    custom_pattern: DslValue[CustomPattern] | None = None
    enforced_urls: list[DslValue[str]] = field(default_factory=list)
    exempt_urls: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RedactionPlaceHolder(PropertyType):
    redaction_place_holder_type: DslValue[str] | None = None
    redaction_place_holder_text: DslValue[str] | None = None
