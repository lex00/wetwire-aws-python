"""PropertyTypes for AWS::Bedrock::FlowVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AgentFlowNodeConfiguration(PropertyType):
    agent_alias_arn: str | None = None


@dataclass
class ConditionFlowNodeConfiguration(PropertyType):
    conditions: list[FlowCondition] = field(default_factory=list)


@dataclass
class FieldForReranking(PropertyType):
    field_name: str | None = None


@dataclass
class FlowCondition(PropertyType):
    name: str | None = None
    expression: str | None = None


@dataclass
class FlowConditionalConnectionConfiguration(PropertyType):
    condition: str | None = None


@dataclass
class FlowConnection(PropertyType):
    name: str | None = None
    source: str | None = None
    target: str | None = None
    type_: str | None = None
    configuration: FlowConnectionConfiguration | None = None


@dataclass
class FlowConnectionConfiguration(PropertyType):
    conditional: FlowConditionalConnectionConfiguration | None = None
    data: FlowDataConnectionConfiguration | None = None


@dataclass
class FlowDataConnectionConfiguration(PropertyType):
    source_output: str | None = None
    target_input: str | None = None


@dataclass
class FlowDefinition(PropertyType):
    connections: list[FlowConnection] = field(default_factory=list)
    nodes: list[FlowNode] = field(default_factory=list)


@dataclass
class FlowNode(PropertyType):
    name: str | None = None
    type_: str | None = None
    configuration: FlowNodeConfiguration | None = None
    inputs: list[FlowNodeInput] = field(default_factory=list)
    outputs: list[FlowNodeOutput] = field(default_factory=list)


@dataclass
class FlowNodeConfiguration(PropertyType):
    agent: AgentFlowNodeConfiguration | None = None
    collector: dict[str, Any] | None = None
    condition: ConditionFlowNodeConfiguration | None = None
    inline_code: InlineCodeFlowNodeConfiguration | None = None
    input: dict[str, Any] | None = None
    iterator: dict[str, Any] | None = None
    knowledge_base: KnowledgeBaseFlowNodeConfiguration | None = None
    lambda_function: LambdaFunctionFlowNodeConfiguration | None = None
    lex: LexFlowNodeConfiguration | None = None
    loop: LoopFlowNodeConfiguration | None = None
    loop_controller: LoopControllerFlowNodeConfiguration | None = None
    loop_input: dict[str, Any] | None = None
    output: dict[str, Any] | None = None
    prompt: PromptFlowNodeConfiguration | None = None
    retrieval: RetrievalFlowNodeConfiguration | None = None
    storage: StorageFlowNodeConfiguration | None = None


@dataclass
class FlowNodeInput(PropertyType):
    expression: str | None = None
    name: str | None = None
    type_: str | None = None


@dataclass
class FlowNodeOutput(PropertyType):
    name: str | None = None
    type_: str | None = None


@dataclass
class GuardrailConfiguration(PropertyType):
    guardrail_identifier: str | None = None
    guardrail_version: str | None = None


@dataclass
class InlineCodeFlowNodeConfiguration(PropertyType):
    code: str | None = None
    language: str | None = None


@dataclass
class KnowledgeBaseFlowNodeConfiguration(PropertyType):
    knowledge_base_id: str | None = None
    guardrail_configuration: GuardrailConfiguration | None = None
    inference_configuration: PromptInferenceConfiguration | None = None
    model_id: str | None = None
    number_of_results: float | None = None
    orchestration_configuration: KnowledgeBaseOrchestrationConfiguration | None = None
    prompt_template: KnowledgeBasePromptTemplate | None = None
    reranking_configuration: VectorSearchRerankingConfiguration | None = None


@dataclass
class KnowledgeBaseOrchestrationConfiguration(PropertyType):
    additional_model_request_fields: dict[str, Any] | None = None
    inference_config: PromptInferenceConfiguration | None = None
    performance_config: PerformanceConfiguration | None = None
    prompt_template: KnowledgeBasePromptTemplate | None = None


@dataclass
class KnowledgeBasePromptTemplate(PropertyType):
    text_prompt_template: str | None = None


@dataclass
class LambdaFunctionFlowNodeConfiguration(PropertyType):
    lambda_arn: str | None = None


@dataclass
class LexFlowNodeConfiguration(PropertyType):
    bot_alias_arn: str | None = None
    locale_id: str | None = None


@dataclass
class LoopControllerFlowNodeConfiguration(PropertyType):
    continue_condition: FlowCondition | None = None
    max_iterations: float | None = None


@dataclass
class LoopFlowNodeConfiguration(PropertyType):
    definition: FlowDefinition | None = None


@dataclass
class MetadataConfigurationForReranking(PropertyType):
    selection_mode: str | None = None
    selective_mode_configuration: RerankingMetadataSelectiveModeConfiguration | None = (
        None
    )


@dataclass
class PerformanceConfiguration(PropertyType):
    latency: str | None = None


@dataclass
class PromptFlowNodeConfiguration(PropertyType):
    source_configuration: PromptFlowNodeSourceConfiguration | None = None
    guardrail_configuration: GuardrailConfiguration | None = None


@dataclass
class PromptFlowNodeInlineConfiguration(PropertyType):
    model_id: str | None = None
    template_configuration: PromptTemplateConfiguration | None = None
    template_type: str | None = None
    inference_configuration: PromptInferenceConfiguration | None = None


@dataclass
class PromptFlowNodeResourceConfiguration(PropertyType):
    prompt_arn: str | None = None


@dataclass
class PromptFlowNodeSourceConfiguration(PropertyType):
    inline: PromptFlowNodeInlineConfiguration | None = None
    resource: PromptFlowNodeResourceConfiguration | None = None


@dataclass
class PromptInferenceConfiguration(PropertyType):
    text: PromptModelInferenceConfiguration | None = None


@dataclass
class PromptInputVariable(PropertyType):
    name: str | None = None


@dataclass
class PromptModelInferenceConfiguration(PropertyType):
    max_tokens: float | None = None
    stop_sequences: list[String] = field(default_factory=list)
    temperature: float | None = None
    top_p: float | None = None


@dataclass
class PromptTemplateConfiguration(PropertyType):
    text: TextPromptTemplateConfiguration | None = None


@dataclass
class RerankingMetadataSelectiveModeConfiguration(PropertyType):
    fields_to_exclude: list[FieldForReranking] = field(default_factory=list)
    fields_to_include: list[FieldForReranking] = field(default_factory=list)


@dataclass
class RetrievalFlowNodeConfiguration(PropertyType):
    service_configuration: RetrievalFlowNodeServiceConfiguration | None = None


@dataclass
class RetrievalFlowNodeS3Configuration(PropertyType):
    bucket_name: str | None = None


@dataclass
class RetrievalFlowNodeServiceConfiguration(PropertyType):
    s3: RetrievalFlowNodeS3Configuration | None = None


@dataclass
class StorageFlowNodeConfiguration(PropertyType):
    service_configuration: StorageFlowNodeServiceConfiguration | None = None


@dataclass
class StorageFlowNodeS3Configuration(PropertyType):
    bucket_name: str | None = None


@dataclass
class StorageFlowNodeServiceConfiguration(PropertyType):
    s3: StorageFlowNodeS3Configuration | None = None


@dataclass
class TextPromptTemplateConfiguration(PropertyType):
    text: str | None = None
    input_variables: list[PromptInputVariable] = field(default_factory=list)


@dataclass
class VectorSearchBedrockRerankingConfiguration(PropertyType):
    model_configuration: VectorSearchBedrockRerankingModelConfiguration | None = None
    metadata_configuration: MetadataConfigurationForReranking | None = None
    number_of_reranked_results: float | None = None


@dataclass
class VectorSearchBedrockRerankingModelConfiguration(PropertyType):
    model_arn: str | None = None
    additional_model_request_fields: dict[str, Any] | None = None


@dataclass
class VectorSearchRerankingConfiguration(PropertyType):
    type_: str | None = None
    bedrock_reranking_configuration: (
        VectorSearchBedrockRerankingConfiguration | None
    ) = None
