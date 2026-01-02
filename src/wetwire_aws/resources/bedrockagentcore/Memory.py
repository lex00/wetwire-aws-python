"""PropertyTypes for AWS::BedrockAgentCore::Memory."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomConfigurationInput(PropertyType):
    self_managed_configuration: SelfManagedConfiguration | None = None
    semantic_override: SemanticOverride | None = None
    summary_override: SummaryOverride | None = None
    user_preference_override: UserPreferenceOverride | None = None


@dataclass
class CustomMemoryStrategy(PropertyType):
    name: str | None = None
    configuration: CustomConfigurationInput | None = None
    created_at: str | None = None
    description: str | None = None
    namespaces: list[String] = field(default_factory=list)
    status: str | None = None
    strategy_id: str | None = None
    type_: str | None = None
    updated_at: str | None = None


@dataclass
class InvocationConfigurationInput(PropertyType):
    payload_delivery_bucket_name: str | None = None
    topic_arn: str | None = None


@dataclass
class MemoryStrategy(PropertyType):
    custom_memory_strategy: CustomMemoryStrategy | None = None
    semantic_memory_strategy: SemanticMemoryStrategy | None = None
    summary_memory_strategy: SummaryMemoryStrategy | None = None
    user_preference_memory_strategy: UserPreferenceMemoryStrategy | None = None


@dataclass
class MessageBasedTriggerInput(PropertyType):
    message_count: int | None = None


@dataclass
class SelfManagedConfiguration(PropertyType):
    historical_context_window_size: int | None = None
    invocation_configuration: InvocationConfigurationInput | None = None
    trigger_conditions: list[TriggerConditionInput] = field(default_factory=list)


@dataclass
class SemanticMemoryStrategy(PropertyType):
    name: str | None = None
    created_at: str | None = None
    description: str | None = None
    namespaces: list[String] = field(default_factory=list)
    status: str | None = None
    strategy_id: str | None = None
    type_: str | None = None
    updated_at: str | None = None


@dataclass
class SemanticOverride(PropertyType):
    consolidation: SemanticOverrideConsolidationConfigurationInput | None = None
    extraction: SemanticOverrideExtractionConfigurationInput | None = None


@dataclass
class SemanticOverrideConsolidationConfigurationInput(PropertyType):
    append_to_prompt: str | None = None
    model_id: str | None = None


@dataclass
class SemanticOverrideExtractionConfigurationInput(PropertyType):
    append_to_prompt: str | None = None
    model_id: str | None = None


@dataclass
class SummaryMemoryStrategy(PropertyType):
    name: str | None = None
    created_at: str | None = None
    description: str | None = None
    namespaces: list[String] = field(default_factory=list)
    status: str | None = None
    strategy_id: str | None = None
    type_: str | None = None
    updated_at: str | None = None


@dataclass
class SummaryOverride(PropertyType):
    consolidation: SummaryOverrideConsolidationConfigurationInput | None = None


@dataclass
class SummaryOverrideConsolidationConfigurationInput(PropertyType):
    append_to_prompt: str | None = None
    model_id: str | None = None


@dataclass
class TimeBasedTriggerInput(PropertyType):
    idle_session_timeout: int | None = None


@dataclass
class TokenBasedTriggerInput(PropertyType):
    token_count: int | None = None


@dataclass
class TriggerConditionInput(PropertyType):
    message_based_trigger: MessageBasedTriggerInput | None = None
    time_based_trigger: TimeBasedTriggerInput | None = None
    token_based_trigger: TokenBasedTriggerInput | None = None


@dataclass
class UserPreferenceMemoryStrategy(PropertyType):
    name: str | None = None
    created_at: str | None = None
    description: str | None = None
    namespaces: list[String] = field(default_factory=list)
    status: str | None = None
    strategy_id: str | None = None
    type_: str | None = None
    updated_at: str | None = None


@dataclass
class UserPreferenceOverride(PropertyType):
    consolidation: UserPreferenceOverrideConsolidationConfigurationInput | None = None
    extraction: UserPreferenceOverrideExtractionConfigurationInput | None = None


@dataclass
class UserPreferenceOverrideConsolidationConfigurationInput(PropertyType):
    append_to_prompt: str | None = None
    model_id: str | None = None


@dataclass
class UserPreferenceOverrideExtractionConfigurationInput(PropertyType):
    append_to_prompt: str | None = None
    model_id: str | None = None
