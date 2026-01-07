"""PropertyTypes for AWS::Wisdom::AIAgent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "answer_recommendation_ai_agent_configuration": "AnswerRecommendationAIAgentConfiguration",
        "email_generative_answer_ai_agent_configuration": "EmailGenerativeAnswerAIAgentConfiguration",
        "email_overview_ai_agent_configuration": "EmailOverviewAIAgentConfiguration",
        "email_response_ai_agent_configuration": "EmailResponseAIAgentConfiguration",
        "manual_search_ai_agent_configuration": "ManualSearchAIAgentConfiguration",
        "self_service_ai_agent_configuration": "SelfServiceAIAgentConfiguration",
    }

    answer_recommendation_ai_agent_configuration: (
        DslValue[AnswerRecommendationAIAgentConfiguration] | None
    ) = None
    email_generative_answer_ai_agent_configuration: (
        DslValue[EmailGenerativeAnswerAIAgentConfiguration] | None
    ) = None
    email_overview_ai_agent_configuration: (
        DslValue[EmailOverviewAIAgentConfiguration] | None
    ) = None
    email_response_ai_agent_configuration: (
        DslValue[EmailResponseAIAgentConfiguration] | None
    ) = None
    manual_search_ai_agent_configuration: (
        DslValue[ManualSearchAIAgentConfiguration] | None
    ) = None
    self_service_ai_agent_configuration: (
        DslValue[SelfServiceAIAgentConfiguration] | None
    ) = None


@dataclass
class AnswerRecommendationAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "answer_generation_ai_guardrail_id": "AnswerGenerationAIGuardrailId",
        "answer_generation_ai_prompt_id": "AnswerGenerationAIPromptId",
        "intent_labeling_generation_ai_prompt_id": "IntentLabelingGenerationAIPromptId",
        "query_reformulation_ai_prompt_id": "QueryReformulationAIPromptId",
    }

    answer_generation_ai_guardrail_id: DslValue[str] | None = None
    answer_generation_ai_prompt_id: DslValue[str] | None = None
    association_configurations: list[DslValue[AssociationConfiguration]] = field(
        default_factory=list
    )
    intent_labeling_generation_ai_prompt_id: DslValue[str] | None = None
    locale: DslValue[str] | None = None
    query_reformulation_ai_prompt_id: DslValue[str] | None = None


@dataclass
class AssociationConfiguration(PropertyType):
    association_configuration_data: DslValue[AssociationConfigurationData] | None = None
    association_id: DslValue[str] | None = None
    association_type: DslValue[str] | None = None


@dataclass
class AssociationConfigurationData(PropertyType):
    knowledge_base_association_configuration_data: (
        DslValue[KnowledgeBaseAssociationConfigurationData] | None
    ) = None


@dataclass
class EmailGenerativeAnswerAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "email_generative_answer_ai_prompt_id": "EmailGenerativeAnswerAIPromptId",
        "email_query_reformulation_ai_prompt_id": "EmailQueryReformulationAIPromptId",
    }

    association_configurations: list[DslValue[AssociationConfiguration]] = field(
        default_factory=list
    )
    email_generative_answer_ai_prompt_id: DslValue[str] | None = None
    email_query_reformulation_ai_prompt_id: DslValue[str] | None = None
    locale: DslValue[str] | None = None


@dataclass
class EmailOverviewAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "email_overview_ai_prompt_id": "EmailOverviewAIPromptId",
    }

    email_overview_ai_prompt_id: DslValue[str] | None = None
    locale: DslValue[str] | None = None


@dataclass
class EmailResponseAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "email_query_reformulation_ai_prompt_id": "EmailQueryReformulationAIPromptId",
        "email_response_ai_prompt_id": "EmailResponseAIPromptId",
    }

    association_configurations: list[DslValue[AssociationConfiguration]] = field(
        default_factory=list
    )
    email_query_reformulation_ai_prompt_id: DslValue[str] | None = None
    email_response_ai_prompt_id: DslValue[str] | None = None
    locale: DslValue[str] | None = None


@dataclass
class KnowledgeBaseAssociationConfigurationData(PropertyType):
    content_tag_filter: DslValue[TagFilter] | None = None
    max_results: DslValue[float] | None = None
    override_knowledge_base_search_type: DslValue[str] | None = None


@dataclass
class ManualSearchAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "answer_generation_ai_guardrail_id": "AnswerGenerationAIGuardrailId",
        "answer_generation_ai_prompt_id": "AnswerGenerationAIPromptId",
    }

    answer_generation_ai_guardrail_id: DslValue[str] | None = None
    answer_generation_ai_prompt_id: DslValue[str] | None = None
    association_configurations: list[DslValue[AssociationConfiguration]] = field(
        default_factory=list
    )
    locale: DslValue[str] | None = None


@dataclass
class OrCondition(PropertyType):
    and_conditions: list[DslValue[TagCondition]] = field(default_factory=list)
    tag_condition: DslValue[TagCondition] | None = None


@dataclass
class SelfServiceAIAgentConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "self_service_ai_guardrail_id": "SelfServiceAIGuardrailId",
        "self_service_answer_generation_ai_prompt_id": "SelfServiceAnswerGenerationAIPromptId",
        "self_service_pre_processing_ai_prompt_id": "SelfServicePreProcessingAIPromptId",
    }

    association_configurations: list[DslValue[AssociationConfiguration]] = field(
        default_factory=list
    )
    self_service_ai_guardrail_id: DslValue[str] | None = None
    self_service_answer_generation_ai_prompt_id: DslValue[str] | None = None
    self_service_pre_processing_ai_prompt_id: DslValue[str] | None = None


@dataclass
class TagCondition(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TagFilter(PropertyType):
    and_conditions: list[DslValue[TagCondition]] = field(default_factory=list)
    or_conditions: list[DslValue[OrCondition]] = field(default_factory=list)
    tag_condition: DslValue[TagCondition] | None = None
