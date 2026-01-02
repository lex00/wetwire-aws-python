"""PropertyTypes for AWS::Bedrock::Guardrail."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutomatedReasoningPolicyConfig(PropertyType):
    policies: list[String] = field(default_factory=list)
    confidence_threshold: float | None = None


@dataclass
class ContentFilterConfig(PropertyType):
    input_strength: str | None = None
    output_strength: str | None = None
    type_: str | None = None
    input_action: str | None = None
    input_enabled: bool | None = None
    input_modalities: list[String] = field(default_factory=list)
    output_action: str | None = None
    output_enabled: bool | None = None
    output_modalities: list[String] = field(default_factory=list)


@dataclass
class ContentFiltersTierConfig(PropertyType):
    tier_name: str | None = None


@dataclass
class ContentPolicyConfig(PropertyType):
    filters_config: list[ContentFilterConfig] = field(default_factory=list)
    content_filters_tier_config: ContentFiltersTierConfig | None = None


@dataclass
class ContextualGroundingFilterConfig(PropertyType):
    threshold: float | None = None
    type_: str | None = None
    action: str | None = None
    enabled: bool | None = None


@dataclass
class ContextualGroundingPolicyConfig(PropertyType):
    filters_config: list[ContextualGroundingFilterConfig] = field(default_factory=list)


@dataclass
class GuardrailCrossRegionConfig(PropertyType):
    guardrail_profile_arn: str | None = None


@dataclass
class ManagedWordsConfig(PropertyType):
    type_: str | None = None
    input_action: str | None = None
    input_enabled: bool | None = None
    output_action: str | None = None
    output_enabled: bool | None = None


@dataclass
class PiiEntityConfig(PropertyType):
    action: str | None = None
    type_: str | None = None
    input_action: str | None = None
    input_enabled: bool | None = None
    output_action: str | None = None
    output_enabled: bool | None = None


@dataclass
class RegexConfig(PropertyType):
    action: str | None = None
    name: str | None = None
    pattern: str | None = None
    description: str | None = None
    input_action: str | None = None
    input_enabled: bool | None = None
    output_action: str | None = None
    output_enabled: bool | None = None


@dataclass
class SensitiveInformationPolicyConfig(PropertyType):
    pii_entities_config: list[PiiEntityConfig] = field(default_factory=list)
    regexes_config: list[RegexConfig] = field(default_factory=list)


@dataclass
class TopicConfig(PropertyType):
    definition: str | None = None
    name: str | None = None
    type_: str | None = None
    examples: list[String] = field(default_factory=list)
    input_action: str | None = None
    input_enabled: bool | None = None
    output_action: str | None = None
    output_enabled: bool | None = None


@dataclass
class TopicPolicyConfig(PropertyType):
    topics_config: list[TopicConfig] = field(default_factory=list)
    topics_tier_config: TopicsTierConfig | None = None


@dataclass
class TopicsTierConfig(PropertyType):
    tier_name: str | None = None


@dataclass
class WordConfig(PropertyType):
    text: str | None = None
    input_action: str | None = None
    input_enabled: bool | None = None
    output_action: str | None = None
    output_enabled: bool | None = None


@dataclass
class WordPolicyConfig(PropertyType):
    managed_word_lists_config: list[ManagedWordsConfig] = field(default_factory=list)
    words_config: list[WordConfig] = field(default_factory=list)
