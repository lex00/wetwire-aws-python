"""PropertyTypes for AWS::Bedrock::Agent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class APISchema(PropertyType):
    payload: str | None = None
    s3: S3Identifier | None = None


@dataclass
class ActionGroupExecutor(PropertyType):
    custom_control: str | None = None
    lambda_: str | None = None


@dataclass
class AgentActionGroup(PropertyType):
    action_group_name: str | None = None
    action_group_executor: ActionGroupExecutor | None = None
    action_group_state: str | None = None
    api_schema: APISchema | None = None
    description: str | None = None
    function_schema: FunctionSchema | None = None
    parent_action_group_signature: str | None = None
    skip_resource_in_use_check_on_delete: bool | None = None


@dataclass
class AgentCollaborator(PropertyType):
    agent_descriptor: AgentDescriptor | None = None
    collaboration_instruction: str | None = None
    collaborator_name: str | None = None
    relay_conversation_history: str | None = None


@dataclass
class AgentDescriptor(PropertyType):
    alias_arn: str | None = None


@dataclass
class AgentKnowledgeBase(PropertyType):
    description: str | None = None
    knowledge_base_id: str | None = None
    knowledge_base_state: str | None = None


@dataclass
class CustomOrchestration(PropertyType):
    executor: OrchestrationExecutor | None = None


@dataclass
class Function(PropertyType):
    name: str | None = None
    description: str | None = None
    parameters: dict[str, ParameterDetail] = field(default_factory=dict)
    require_confirmation: str | None = None


@dataclass
class FunctionSchema(PropertyType):
    functions: list[Function] = field(default_factory=list)


@dataclass
class GuardrailConfiguration(PropertyType):
    guardrail_identifier: str | None = None
    guardrail_version: str | None = None


@dataclass
class InferenceConfiguration(PropertyType):
    maximum_length: float | None = None
    stop_sequences: list[String] = field(default_factory=list)
    temperature: float | None = None
    top_k: float | None = None
    top_p: float | None = None


@dataclass
class MemoryConfiguration(PropertyType):
    enabled_memory_types: list[String] = field(default_factory=list)
    session_summary_configuration: SessionSummaryConfiguration | None = None
    storage_days: float | None = None


@dataclass
class OrchestrationExecutor(PropertyType):
    lambda_: str | None = None


@dataclass
class ParameterDetail(PropertyType):
    type_: str | None = None
    description: str | None = None
    required: bool | None = None


@dataclass
class PromptConfiguration(PropertyType):
    additional_model_request_fields: dict[str, Any] | None = None
    base_prompt_template: str | None = None
    foundation_model: str | None = None
    inference_configuration: InferenceConfiguration | None = None
    parser_mode: str | None = None
    prompt_creation_mode: str | None = None
    prompt_state: str | None = None
    prompt_type: str | None = None


@dataclass
class PromptOverrideConfiguration(PropertyType):
    prompt_configurations: list[PromptConfiguration] = field(default_factory=list)
    override_lambda: str | None = None


@dataclass
class S3Identifier(PropertyType):
    s3_bucket_name: str | None = None
    s3_object_key: str | None = None


@dataclass
class SessionSummaryConfiguration(PropertyType):
    max_recent_sessions: float | None = None
