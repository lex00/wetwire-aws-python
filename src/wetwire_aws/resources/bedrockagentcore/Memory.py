"""PropertyTypes for AWS::BedrockAgentCore::Memory."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomConfigurationInput(PropertyType):
    episodic_override: DslValue[EpisodicOverride] | None = None
    self_managed_configuration: DslValue[SelfManagedConfiguration] | None = None
    semantic_override: DslValue[SemanticOverride] | None = None
    summary_override: DslValue[SummaryOverride] | None = None
    user_preference_override: DslValue[UserPreferenceOverride] | None = None


@dataclass
class CustomMemoryStrategy(PropertyType):
    name: DslValue[str] | None = None
    configuration: DslValue[CustomConfigurationInput] | None = None
    created_at: DslValue[str] | None = None
    description: DslValue[str] | None = None
    namespaces: list[DslValue[str]] = field(default_factory=list)
    status: DslValue[str] | None = None
    strategy_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    updated_at: DslValue[str] | None = None


@dataclass
class EpisodicMemoryStrategy(PropertyType):
    name: DslValue[str] | None = None
    created_at: DslValue[str] | None = None
    description: DslValue[str] | None = None
    namespaces: list[DslValue[str]] = field(default_factory=list)
    reflection_configuration: DslValue[EpisodicReflectionConfigurationInput] | None = (
        None
    )
    status: DslValue[str] | None = None
    strategy_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    updated_at: DslValue[str] | None = None


@dataclass
class EpisodicOverride(PropertyType):
    consolidation: DslValue[EpisodicOverrideConsolidationConfigurationInput] | None = (
        None
    )
    extraction: DslValue[EpisodicOverrideExtractionConfigurationInput] | None = None
    reflection: DslValue[EpisodicOverrideReflectionConfigurationInput] | None = None


@dataclass
class EpisodicOverrideConsolidationConfigurationInput(PropertyType):
    append_to_prompt: DslValue[str] | None = None
    model_id: DslValue[str] | None = None


@dataclass
class EpisodicOverrideExtractionConfigurationInput(PropertyType):
    append_to_prompt: DslValue[str] | None = None
    model_id: DslValue[str] | None = None


@dataclass
class EpisodicOverrideReflectionConfigurationInput(PropertyType):
    append_to_prompt: DslValue[str] | None = None
    model_id: DslValue[str] | None = None
    namespaces: list[DslValue[str]] = field(default_factory=list)


@dataclass
class EpisodicReflectionConfigurationInput(PropertyType):
    namespaces: list[DslValue[str]] = field(default_factory=list)


@dataclass
class InvocationConfigurationInput(PropertyType):
    payload_delivery_bucket_name: DslValue[str] | None = None
    topic_arn: DslValue[str] | None = None


@dataclass
class MemoryStrategy(PropertyType):
    custom_memory_strategy: DslValue[CustomMemoryStrategy] | None = None
    episodic_memory_strategy: DslValue[EpisodicMemoryStrategy] | None = None
    semantic_memory_strategy: DslValue[SemanticMemoryStrategy] | None = None
    summary_memory_strategy: DslValue[SummaryMemoryStrategy] | None = None
    user_preference_memory_strategy: DslValue[UserPreferenceMemoryStrategy] | None = (
        None
    )


@dataclass
class MessageBasedTriggerInput(PropertyType):
    message_count: DslValue[int] | None = None


@dataclass
class SelfManagedConfiguration(PropertyType):
    historical_context_window_size: DslValue[int] | None = None
    invocation_configuration: DslValue[InvocationConfigurationInput] | None = None
    trigger_conditions: list[DslValue[TriggerConditionInput]] = field(
        default_factory=list
    )


@dataclass
class SemanticMemoryStrategy(PropertyType):
    name: DslValue[str] | None = None
    created_at: DslValue[str] | None = None
    description: DslValue[str] | None = None
    namespaces: list[DslValue[str]] = field(default_factory=list)
    status: DslValue[str] | None = None
    strategy_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    updated_at: DslValue[str] | None = None


@dataclass
class SemanticOverride(PropertyType):
    consolidation: DslValue[SemanticOverrideConsolidationConfigurationInput] | None = (
        None
    )
    extraction: DslValue[SemanticOverrideExtractionConfigurationInput] | None = None


@dataclass
class SemanticOverrideConsolidationConfigurationInput(PropertyType):
    append_to_prompt: DslValue[str] | None = None
    model_id: DslValue[str] | None = None


@dataclass
class SemanticOverrideExtractionConfigurationInput(PropertyType):
    append_to_prompt: DslValue[str] | None = None
    model_id: DslValue[str] | None = None


@dataclass
class SummaryMemoryStrategy(PropertyType):
    name: DslValue[str] | None = None
    created_at: DslValue[str] | None = None
    description: DslValue[str] | None = None
    namespaces: list[DslValue[str]] = field(default_factory=list)
    status: DslValue[str] | None = None
    strategy_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    updated_at: DslValue[str] | None = None


@dataclass
class SummaryOverride(PropertyType):
    consolidation: DslValue[SummaryOverrideConsolidationConfigurationInput] | None = (
        None
    )


@dataclass
class SummaryOverrideConsolidationConfigurationInput(PropertyType):
    append_to_prompt: DslValue[str] | None = None
    model_id: DslValue[str] | None = None


@dataclass
class TimeBasedTriggerInput(PropertyType):
    idle_session_timeout: DslValue[int] | None = None


@dataclass
class TokenBasedTriggerInput(PropertyType):
    token_count: DslValue[int] | None = None


@dataclass
class TriggerConditionInput(PropertyType):
    message_based_trigger: DslValue[MessageBasedTriggerInput] | None = None
    time_based_trigger: DslValue[TimeBasedTriggerInput] | None = None
    token_based_trigger: DslValue[TokenBasedTriggerInput] | None = None


@dataclass
class UserPreferenceMemoryStrategy(PropertyType):
    name: DslValue[str] | None = None
    created_at: DslValue[str] | None = None
    description: DslValue[str] | None = None
    namespaces: list[DslValue[str]] = field(default_factory=list)
    status: DslValue[str] | None = None
    strategy_id: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    updated_at: DslValue[str] | None = None


@dataclass
class UserPreferenceOverride(PropertyType):
    consolidation: (
        DslValue[UserPreferenceOverrideConsolidationConfigurationInput] | None
    ) = None
    extraction: DslValue[UserPreferenceOverrideExtractionConfigurationInput] | None = (
        None
    )


@dataclass
class UserPreferenceOverrideConsolidationConfigurationInput(PropertyType):
    append_to_prompt: DslValue[str] | None = None
    model_id: DslValue[str] | None = None


@dataclass
class UserPreferenceOverrideExtractionConfigurationInput(PropertyType):
    append_to_prompt: DslValue[str] | None = None
    model_id: DslValue[str] | None = None
