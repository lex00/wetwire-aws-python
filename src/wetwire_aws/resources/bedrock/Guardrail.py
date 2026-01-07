"""PropertyTypes for AWS::Bedrock::Guardrail."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutomatedReasoningPolicyConfig(PropertyType):
    policies: list[DslValue[str]] = field(default_factory=list)
    confidence_threshold: DslValue[float] | None = None


@dataclass
class ContentFilterConfig(PropertyType):
    input_strength: DslValue[str] | None = None
    output_strength: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    input_action: DslValue[str] | None = None
    input_enabled: DslValue[bool] | None = None
    input_modalities: list[DslValue[str]] = field(default_factory=list)
    output_action: DslValue[str] | None = None
    output_enabled: DslValue[bool] | None = None
    output_modalities: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ContentFiltersTierConfig(PropertyType):
    tier_name: DslValue[str] | None = None


@dataclass
class ContentPolicyConfig(PropertyType):
    filters_config: list[DslValue[ContentFilterConfig]] = field(default_factory=list)
    content_filters_tier_config: DslValue[ContentFiltersTierConfig] | None = None


@dataclass
class ContextualGroundingFilterConfig(PropertyType):
    threshold: DslValue[float] | None = None
    type_: DslValue[str] | None = None
    action: DslValue[str] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class ContextualGroundingPolicyConfig(PropertyType):
    filters_config: list[DslValue[ContextualGroundingFilterConfig]] = field(
        default_factory=list
    )


@dataclass
class GuardrailCrossRegionConfig(PropertyType):
    guardrail_profile_arn: DslValue[str] | None = None


@dataclass
class ManagedWordsConfig(PropertyType):
    type_: DslValue[str] | None = None
    input_action: DslValue[str] | None = None
    input_enabled: DslValue[bool] | None = None
    output_action: DslValue[str] | None = None
    output_enabled: DslValue[bool] | None = None


@dataclass
class PiiEntityConfig(PropertyType):
    action: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    input_action: DslValue[str] | None = None
    input_enabled: DslValue[bool] | None = None
    output_action: DslValue[str] | None = None
    output_enabled: DslValue[bool] | None = None


@dataclass
class RegexConfig(PropertyType):
    action: DslValue[str] | None = None
    name: DslValue[str] | None = None
    pattern: DslValue[str] | None = None
    description: DslValue[str] | None = None
    input_action: DslValue[str] | None = None
    input_enabled: DslValue[bool] | None = None
    output_action: DslValue[str] | None = None
    output_enabled: DslValue[bool] | None = None


@dataclass
class SensitiveInformationPolicyConfig(PropertyType):
    pii_entities_config: list[DslValue[PiiEntityConfig]] = field(default_factory=list)
    regexes_config: list[DslValue[RegexConfig]] = field(default_factory=list)


@dataclass
class TopicConfig(PropertyType):
    definition: DslValue[str] | None = None
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    examples: list[DslValue[str]] = field(default_factory=list)
    input_action: DslValue[str] | None = None
    input_enabled: DslValue[bool] | None = None
    output_action: DslValue[str] | None = None
    output_enabled: DslValue[bool] | None = None


@dataclass
class TopicPolicyConfig(PropertyType):
    topics_config: list[DslValue[TopicConfig]] = field(default_factory=list)
    topics_tier_config: DslValue[TopicsTierConfig] | None = None


@dataclass
class TopicsTierConfig(PropertyType):
    tier_name: DslValue[str] | None = None


@dataclass
class WordConfig(PropertyType):
    text: DslValue[str] | None = None
    input_action: DslValue[str] | None = None
    input_enabled: DslValue[bool] | None = None
    output_action: DslValue[str] | None = None
    output_enabled: DslValue[bool] | None = None


@dataclass
class WordPolicyConfig(PropertyType):
    managed_word_lists_config: list[DslValue[ManagedWordsConfig]] = field(
        default_factory=list
    )
    words_config: list[DslValue[WordConfig]] = field(default_factory=list)
