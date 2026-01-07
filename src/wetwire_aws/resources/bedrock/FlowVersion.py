"""PropertyTypes for AWS::Bedrock::FlowVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AgentFlowNodeConfiguration(PropertyType):
    agent_alias_arn: DslValue[str] | None = None


@dataclass
class ConditionFlowNodeConfiguration(PropertyType):
    conditions: list[DslValue[FlowCondition]] = field(default_factory=list)


@dataclass
class FieldForReranking(PropertyType):
    field_name: DslValue[str] | None = None


@dataclass
class FlowCondition(PropertyType):
    name: DslValue[str] | None = None
    expression: DslValue[str] | None = None


@dataclass
class FlowConditionalConnectionConfiguration(PropertyType):
    condition: DslValue[str] | None = None


@dataclass
class FlowConnection(PropertyType):
    name: DslValue[str] | None = None
    source: DslValue[str] | None = None
    target: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    configuration: DslValue[FlowConnectionConfiguration] | None = None


@dataclass
class FlowConnectionConfiguration(PropertyType):
    conditional: DslValue[FlowConditionalConnectionConfiguration] | None = None
    data: DslValue[FlowDataConnectionConfiguration] | None = None


@dataclass
class FlowDataConnectionConfiguration(PropertyType):
    source_output: DslValue[str] | None = None
    target_input: DslValue[str] | None = None


@dataclass
class FlowDefinition(PropertyType):
    connections: list[DslValue[FlowConnection]] = field(default_factory=list)
    nodes: list[DslValue[FlowNode]] = field(default_factory=list)


@dataclass
class FlowNode(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    configuration: DslValue[FlowNodeConfiguration] | None = None
    inputs: list[DslValue[FlowNodeInput]] = field(default_factory=list)
    outputs: list[DslValue[FlowNodeOutput]] = field(default_factory=list)


@dataclass
class FlowNodeConfiguration(PropertyType):
    agent: DslValue[AgentFlowNodeConfiguration] | None = None
    collector: DslValue[dict[str, Any]] | None = None
    condition: DslValue[ConditionFlowNodeConfiguration] | None = None
    inline_code: DslValue[InlineCodeFlowNodeConfiguration] | None = None
    input: DslValue[dict[str, Any]] | None = None
    iterator: DslValue[dict[str, Any]] | None = None
    knowledge_base: DslValue[KnowledgeBaseFlowNodeConfiguration] | None = None
    lambda_function: DslValue[LambdaFunctionFlowNodeConfiguration] | None = None
    lex: DslValue[LexFlowNodeConfiguration] | None = None
    loop: DslValue[LoopFlowNodeConfiguration] | None = None
    loop_controller: DslValue[LoopControllerFlowNodeConfiguration] | None = None
    loop_input: DslValue[dict[str, Any]] | None = None
    output: DslValue[dict[str, Any]] | None = None
    prompt: DslValue[PromptFlowNodeConfiguration] | None = None
    retrieval: DslValue[RetrievalFlowNodeConfiguration] | None = None
    storage: DslValue[StorageFlowNodeConfiguration] | None = None


@dataclass
class FlowNodeInput(PropertyType):
    expression: DslValue[str] | None = None
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FlowNodeOutput(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class GuardrailConfiguration(PropertyType):
    guardrail_identifier: DslValue[str] | None = None
    guardrail_version: DslValue[str] | None = None


@dataclass
class InlineCodeFlowNodeConfiguration(PropertyType):
    code: DslValue[str] | None = None
    language: DslValue[str] | None = None


@dataclass
class KnowledgeBaseFlowNodeConfiguration(PropertyType):
    knowledge_base_id: DslValue[str] | None = None
    guardrail_configuration: DslValue[GuardrailConfiguration] | None = None
    inference_configuration: DslValue[PromptInferenceConfiguration] | None = None
    model_id: DslValue[str] | None = None
    number_of_results: DslValue[float] | None = None
    orchestration_configuration: (
        DslValue[KnowledgeBaseOrchestrationConfiguration] | None
    ) = None
    prompt_template: DslValue[KnowledgeBasePromptTemplate] | None = None
    reranking_configuration: DslValue[VectorSearchRerankingConfiguration] | None = None


@dataclass
class KnowledgeBaseOrchestrationConfiguration(PropertyType):
    additional_model_request_fields: DslValue[dict[str, Any]] | None = None
    inference_config: DslValue[PromptInferenceConfiguration] | None = None
    performance_config: DslValue[PerformanceConfiguration] | None = None
    prompt_template: DslValue[KnowledgeBasePromptTemplate] | None = None


@dataclass
class KnowledgeBasePromptTemplate(PropertyType):
    text_prompt_template: DslValue[str] | None = None


@dataclass
class LambdaFunctionFlowNodeConfiguration(PropertyType):
    lambda_arn: DslValue[str] | None = None


@dataclass
class LexFlowNodeConfiguration(PropertyType):
    bot_alias_arn: DslValue[str] | None = None
    locale_id: DslValue[str] | None = None


@dataclass
class LoopControllerFlowNodeConfiguration(PropertyType):
    continue_condition: DslValue[FlowCondition] | None = None
    max_iterations: DslValue[float] | None = None


@dataclass
class LoopFlowNodeConfiguration(PropertyType):
    definition: DslValue[FlowDefinition] | None = None


@dataclass
class MetadataConfigurationForReranking(PropertyType):
    selection_mode: DslValue[str] | None = None
    selective_mode_configuration: (
        DslValue[RerankingMetadataSelectiveModeConfiguration] | None
    ) = None


@dataclass
class PerformanceConfiguration(PropertyType):
    latency: DslValue[str] | None = None


@dataclass
class PromptFlowNodeConfiguration(PropertyType):
    source_configuration: DslValue[PromptFlowNodeSourceConfiguration] | None = None
    guardrail_configuration: DslValue[GuardrailConfiguration] | None = None


@dataclass
class PromptFlowNodeInlineConfiguration(PropertyType):
    model_id: DslValue[str] | None = None
    template_configuration: DslValue[PromptTemplateConfiguration] | None = None
    template_type: DslValue[str] | None = None
    inference_configuration: DslValue[PromptInferenceConfiguration] | None = None


@dataclass
class PromptFlowNodeResourceConfiguration(PropertyType):
    prompt_arn: DslValue[str] | None = None


@dataclass
class PromptFlowNodeSourceConfiguration(PropertyType):
    inline: DslValue[PromptFlowNodeInlineConfiguration] | None = None
    resource: DslValue[PromptFlowNodeResourceConfiguration] | None = None


@dataclass
class PromptInferenceConfiguration(PropertyType):
    text: DslValue[PromptModelInferenceConfiguration] | None = None


@dataclass
class PromptInputVariable(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class PromptModelInferenceConfiguration(PropertyType):
    max_tokens: DslValue[float] | None = None
    stop_sequences: list[DslValue[str]] = field(default_factory=list)
    temperature: DslValue[float] | None = None
    top_p: DslValue[float] | None = None


@dataclass
class PromptTemplateConfiguration(PropertyType):
    text: DslValue[TextPromptTemplateConfiguration] | None = None


@dataclass
class RerankingMetadataSelectiveModeConfiguration(PropertyType):
    fields_to_exclude: list[DslValue[FieldForReranking]] = field(default_factory=list)
    fields_to_include: list[DslValue[FieldForReranking]] = field(default_factory=list)


@dataclass
class RetrievalFlowNodeConfiguration(PropertyType):
    service_configuration: DslValue[RetrievalFlowNodeServiceConfiguration] | None = None


@dataclass
class RetrievalFlowNodeS3Configuration(PropertyType):
    bucket_name: DslValue[str] | None = None


@dataclass
class RetrievalFlowNodeServiceConfiguration(PropertyType):
    s3: DslValue[RetrievalFlowNodeS3Configuration] | None = None


@dataclass
class StorageFlowNodeConfiguration(PropertyType):
    service_configuration: DslValue[StorageFlowNodeServiceConfiguration] | None = None


@dataclass
class StorageFlowNodeS3Configuration(PropertyType):
    bucket_name: DslValue[str] | None = None


@dataclass
class StorageFlowNodeServiceConfiguration(PropertyType):
    s3: DslValue[StorageFlowNodeS3Configuration] | None = None


@dataclass
class TextPromptTemplateConfiguration(PropertyType):
    text: DslValue[str] | None = None
    input_variables: list[DslValue[PromptInputVariable]] = field(default_factory=list)


@dataclass
class VectorSearchBedrockRerankingConfiguration(PropertyType):
    model_configuration: (
        DslValue[VectorSearchBedrockRerankingModelConfiguration] | None
    ) = None
    metadata_configuration: DslValue[MetadataConfigurationForReranking] | None = None
    number_of_reranked_results: DslValue[float] | None = None


@dataclass
class VectorSearchBedrockRerankingModelConfiguration(PropertyType):
    model_arn: DslValue[str] | None = None
    additional_model_request_fields: DslValue[dict[str, Any]] | None = None


@dataclass
class VectorSearchRerankingConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    bedrock_reranking_configuration: (
        DslValue[VectorSearchBedrockRerankingConfiguration] | None
    ) = None
