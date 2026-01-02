"""PropertyTypes for AWS::Wisdom::AIGuardrail."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AIGuardrailContentPolicyConfig(PropertyType):
    filters_config: list[GuardrailContentFilterConfig] = field(default_factory=list)


@dataclass
class AIGuardrailContextualGroundingPolicyConfig(PropertyType):
    filters_config: list[GuardrailContextualGroundingFilterConfig] = field(
        default_factory=list
    )


@dataclass
class AIGuardrailSensitiveInformationPolicyConfig(PropertyType):
    pii_entities_config: list[GuardrailPiiEntityConfig] = field(default_factory=list)
    regexes_config: list[GuardrailRegexConfig] = field(default_factory=list)


@dataclass
class AIGuardrailTopicPolicyConfig(PropertyType):
    topics_config: list[GuardrailTopicConfig] = field(default_factory=list)


@dataclass
class AIGuardrailWordPolicyConfig(PropertyType):
    managed_word_lists_config: list[GuardrailManagedWordsConfig] = field(
        default_factory=list
    )
    words_config: list[GuardrailWordConfig] = field(default_factory=list)


@dataclass
class GuardrailContentFilterConfig(PropertyType):
    input_strength: str | None = None
    output_strength: str | None = None
    type_: str | None = None


@dataclass
class GuardrailContextualGroundingFilterConfig(PropertyType):
    threshold: float | None = None
    type_: str | None = None


@dataclass
class GuardrailManagedWordsConfig(PropertyType):
    type_: str | None = None


@dataclass
class GuardrailPiiEntityConfig(PropertyType):
    action: str | None = None
    type_: str | None = None


@dataclass
class GuardrailRegexConfig(PropertyType):
    action: str | None = None
    name: str | None = None
    pattern: str | None = None
    description: str | None = None


@dataclass
class GuardrailTopicConfig(PropertyType):
    definition: str | None = None
    name: str | None = None
    type_: str | None = None
    examples: list[String] = field(default_factory=list)


@dataclass
class GuardrailWordConfig(PropertyType):
    text: str | None = None
