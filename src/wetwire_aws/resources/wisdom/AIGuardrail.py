"""PropertyTypes for AWS::Wisdom::AIGuardrail."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AIGuardrailContentPolicyConfig(PropertyType):
    filters_config: list[DslValue[GuardrailContentFilterConfig]] = field(
        default_factory=list
    )


@dataclass
class AIGuardrailContextualGroundingPolicyConfig(PropertyType):
    filters_config: list[DslValue[GuardrailContextualGroundingFilterConfig]] = field(
        default_factory=list
    )


@dataclass
class AIGuardrailSensitiveInformationPolicyConfig(PropertyType):
    pii_entities_config: list[DslValue[GuardrailPiiEntityConfig]] = field(
        default_factory=list
    )
    regexes_config: list[DslValue[GuardrailRegexConfig]] = field(default_factory=list)


@dataclass
class AIGuardrailTopicPolicyConfig(PropertyType):
    topics_config: list[DslValue[GuardrailTopicConfig]] = field(default_factory=list)


@dataclass
class AIGuardrailWordPolicyConfig(PropertyType):
    managed_word_lists_config: list[DslValue[GuardrailManagedWordsConfig]] = field(
        default_factory=list
    )
    words_config: list[DslValue[GuardrailWordConfig]] = field(default_factory=list)


@dataclass
class GuardrailContentFilterConfig(PropertyType):
    input_strength: DslValue[str] | None = None
    output_strength: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class GuardrailContextualGroundingFilterConfig(PropertyType):
    threshold: DslValue[float] | None = None
    type_: DslValue[str] | None = None


@dataclass
class GuardrailManagedWordsConfig(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class GuardrailPiiEntityConfig(PropertyType):
    action: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class GuardrailRegexConfig(PropertyType):
    action: DslValue[str] | None = None
    name: DslValue[str] | None = None
    pattern: DslValue[str] | None = None
    description: DslValue[str] | None = None


@dataclass
class GuardrailTopicConfig(PropertyType):
    definition: DslValue[str] | None = None
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    examples: list[DslValue[str]] = field(default_factory=list)


@dataclass
class GuardrailWordConfig(PropertyType):
    text: DslValue[str] | None = None
