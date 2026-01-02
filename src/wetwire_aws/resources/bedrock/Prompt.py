"""PropertyTypes for AWS::Bedrock::Prompt."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CachePointBlock(PropertyType):
    type_: str | None = None


@dataclass
class ChatPromptTemplateConfiguration(PropertyType):
    messages: list[Message] = field(default_factory=list)
    input_variables: list[PromptInputVariable] = field(default_factory=list)
    system: list[SystemContentBlock] = field(default_factory=list)
    tool_configuration: ToolConfiguration | None = None


@dataclass
class ContentBlock(PropertyType):
    cache_point: CachePointBlock | None = None
    text: str | None = None


@dataclass
class Message(PropertyType):
    content: list[ContentBlock] = field(default_factory=list)
    role: str | None = None


@dataclass
class PromptAgentResource(PropertyType):
    agent_identifier: str | None = None


@dataclass
class PromptGenAiResource(PropertyType):
    agent: PromptAgentResource | None = None


@dataclass
class PromptInferenceConfiguration(PropertyType):
    text: PromptModelInferenceConfiguration | None = None


@dataclass
class PromptInputVariable(PropertyType):
    name: str | None = None


@dataclass
class PromptMetadataEntry(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class PromptModelInferenceConfiguration(PropertyType):
    max_tokens: float | None = None
    stop_sequences: list[String] = field(default_factory=list)
    temperature: float | None = None
    top_p: float | None = None


@dataclass
class PromptTemplateConfiguration(PropertyType):
    chat: ChatPromptTemplateConfiguration | None = None
    text: TextPromptTemplateConfiguration | None = None


@dataclass
class PromptVariant(PropertyType):
    name: str | None = None
    template_configuration: PromptTemplateConfiguration | None = None
    template_type: str | None = None
    additional_model_request_fields: dict[str, Any] | None = None
    gen_ai_resource: PromptGenAiResource | None = None
    inference_configuration: PromptInferenceConfiguration | None = None
    metadata: list[PromptMetadataEntry] = field(default_factory=list)
    model_id: str | None = None


@dataclass
class SpecificToolChoice(PropertyType):
    name: str | None = None


@dataclass
class SystemContentBlock(PropertyType):
    cache_point: CachePointBlock | None = None
    text: str | None = None


@dataclass
class TextPromptTemplateConfiguration(PropertyType):
    cache_point: CachePointBlock | None = None
    input_variables: list[PromptInputVariable] = field(default_factory=list)
    text: str | None = None
    text_s3_location: TextS3Location | None = None


@dataclass
class TextS3Location(PropertyType):
    bucket: str | None = None
    key: str | None = None
    version: str | None = None


@dataclass
class Tool(PropertyType):
    cache_point: CachePointBlock | None = None
    tool_spec: ToolSpecification | None = None


@dataclass
class ToolChoice(PropertyType):
    any: dict[str, Any] | None = None
    auto: dict[str, Any] | None = None
    tool: SpecificToolChoice | None = None


@dataclass
class ToolConfiguration(PropertyType):
    tools: list[Tool] = field(default_factory=list)
    tool_choice: ToolChoice | None = None


@dataclass
class ToolInputSchema(PropertyType):
    json: dict[str, Any] | None = None


@dataclass
class ToolSpecification(PropertyType):
    input_schema: ToolInputSchema | None = None
    name: str | None = None
    description: str | None = None
