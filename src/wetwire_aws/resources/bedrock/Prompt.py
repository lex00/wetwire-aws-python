"""PropertyTypes for AWS::Bedrock::Prompt."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CachePointBlock(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class ChatPromptTemplateConfiguration(PropertyType):
    messages: list[DslValue[Message]] = field(default_factory=list)
    input_variables: list[DslValue[PromptInputVariable]] = field(default_factory=list)
    system: list[DslValue[SystemContentBlock]] = field(default_factory=list)
    tool_configuration: DslValue[ToolConfiguration] | None = None


@dataclass
class ContentBlock(PropertyType):
    cache_point: DslValue[CachePointBlock] | None = None
    text: DslValue[str] | None = None


@dataclass
class Message(PropertyType):
    content: list[DslValue[ContentBlock]] = field(default_factory=list)
    role: DslValue[str] | None = None


@dataclass
class PromptAgentResource(PropertyType):
    agent_identifier: DslValue[str] | None = None


@dataclass
class PromptGenAiResource(PropertyType):
    agent: DslValue[PromptAgentResource] | None = None


@dataclass
class PromptInferenceConfiguration(PropertyType):
    text: DslValue[PromptModelInferenceConfiguration] | None = None


@dataclass
class PromptInputVariable(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class PromptMetadataEntry(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class PromptModelInferenceConfiguration(PropertyType):
    max_tokens: DslValue[float] | None = None
    stop_sequences: list[DslValue[str]] = field(default_factory=list)
    temperature: DslValue[float] | None = None
    top_p: DslValue[float] | None = None


@dataclass
class PromptTemplateConfiguration(PropertyType):
    chat: DslValue[ChatPromptTemplateConfiguration] | None = None
    text: DslValue[TextPromptTemplateConfiguration] | None = None


@dataclass
class PromptVariant(PropertyType):
    name: DslValue[str] | None = None
    template_configuration: DslValue[PromptTemplateConfiguration] | None = None
    template_type: DslValue[str] | None = None
    additional_model_request_fields: DslValue[dict[str, Any]] | None = None
    gen_ai_resource: DslValue[PromptGenAiResource] | None = None
    inference_configuration: DslValue[PromptInferenceConfiguration] | None = None
    metadata: list[DslValue[PromptMetadataEntry]] = field(default_factory=list)
    model_id: DslValue[str] | None = None


@dataclass
class SpecificToolChoice(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class SystemContentBlock(PropertyType):
    cache_point: DslValue[CachePointBlock] | None = None
    text: DslValue[str] | None = None


@dataclass
class TextPromptTemplateConfiguration(PropertyType):
    cache_point: DslValue[CachePointBlock] | None = None
    input_variables: list[DslValue[PromptInputVariable]] = field(default_factory=list)
    text: DslValue[str] | None = None
    text_s3_location: DslValue[TextS3Location] | None = None


@dataclass
class TextS3Location(PropertyType):
    bucket: DslValue[str] | None = None
    key: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class Tool(PropertyType):
    cache_point: DslValue[CachePointBlock] | None = None
    tool_spec: DslValue[ToolSpecification] | None = None


@dataclass
class ToolChoice(PropertyType):
    any: DslValue[dict[str, Any]] | None = None
    auto: DslValue[dict[str, Any]] | None = None
    tool: DslValue[SpecificToolChoice] | None = None


@dataclass
class ToolConfiguration(PropertyType):
    tools: list[DslValue[Tool]] = field(default_factory=list)
    tool_choice: DslValue[ToolChoice] | None = None


@dataclass
class ToolInputSchema(PropertyType):
    json: DslValue[dict[str, Any]] | None = None


@dataclass
class ToolSpecification(PropertyType):
    input_schema: DslValue[ToolInputSchema] | None = None
    name: DslValue[str] | None = None
    description: DslValue[str] | None = None
