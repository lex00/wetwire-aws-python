"""PropertyTypes for AWS::Bedrock::Agent."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class APISchema(PropertyType):
    payload: DslValue[str] | None = None
    s3: DslValue[S3Identifier] | None = None


@dataclass
class ActionGroupExecutor(PropertyType):
    custom_control: DslValue[str] | None = None
    lambda_: DslValue[str] | None = None


@dataclass
class AgentActionGroup(PropertyType):
    action_group_name: DslValue[str] | None = None
    action_group_executor: DslValue[ActionGroupExecutor] | None = None
    action_group_state: DslValue[str] | None = None
    api_schema: DslValue[APISchema] | None = None
    description: DslValue[str] | None = None
    function_schema: DslValue[FunctionSchema] | None = None
    parent_action_group_signature: DslValue[str] | None = None
    skip_resource_in_use_check_on_delete: DslValue[bool] | None = None


@dataclass
class AgentCollaborator(PropertyType):
    agent_descriptor: DslValue[AgentDescriptor] | None = None
    collaboration_instruction: DslValue[str] | None = None
    collaborator_name: DslValue[str] | None = None
    relay_conversation_history: DslValue[str] | None = None


@dataclass
class AgentDescriptor(PropertyType):
    alias_arn: DslValue[str] | None = None


@dataclass
class AgentKnowledgeBase(PropertyType):
    description: DslValue[str] | None = None
    knowledge_base_id: DslValue[str] | None = None
    knowledge_base_state: DslValue[str] | None = None


@dataclass
class CustomOrchestration(PropertyType):
    executor: DslValue[OrchestrationExecutor] | None = None


@dataclass
class Function(PropertyType):
    name: DslValue[str] | None = None
    description: DslValue[str] | None = None
    parameters: dict[str, DslValue[ParameterDetail]] = field(default_factory=dict)
    require_confirmation: DslValue[str] | None = None


@dataclass
class FunctionSchema(PropertyType):
    functions: list[DslValue[Function]] = field(default_factory=list)


@dataclass
class GuardrailConfiguration(PropertyType):
    guardrail_identifier: DslValue[str] | None = None
    guardrail_version: DslValue[str] | None = None


@dataclass
class InferenceConfiguration(PropertyType):
    maximum_length: DslValue[float] | None = None
    stop_sequences: list[DslValue[str]] = field(default_factory=list)
    temperature: DslValue[float] | None = None
    top_k: DslValue[float] | None = None
    top_p: DslValue[float] | None = None


@dataclass
class MemoryConfiguration(PropertyType):
    enabled_memory_types: list[DslValue[str]] = field(default_factory=list)
    session_summary_configuration: DslValue[SessionSummaryConfiguration] | None = None
    storage_days: DslValue[float] | None = None


@dataclass
class OrchestrationExecutor(PropertyType):
    lambda_: DslValue[str] | None = None


@dataclass
class ParameterDetail(PropertyType):
    type_: DslValue[str] | None = None
    description: DslValue[str] | None = None
    required: DslValue[bool] | None = None


@dataclass
class PromptConfiguration(PropertyType):
    additional_model_request_fields: DslValue[dict[str, Any]] | None = None
    base_prompt_template: DslValue[str] | None = None
    foundation_model: DslValue[str] | None = None
    inference_configuration: DslValue[InferenceConfiguration] | None = None
    parser_mode: DslValue[str] | None = None
    prompt_creation_mode: DslValue[str] | None = None
    prompt_state: DslValue[str] | None = None
    prompt_type: DslValue[str] | None = None


@dataclass
class PromptOverrideConfiguration(PropertyType):
    prompt_configurations: list[DslValue[PromptConfiguration]] = field(
        default_factory=list
    )
    override_lambda: DslValue[str] | None = None


@dataclass
class S3Identifier(PropertyType):
    s3_bucket_name: DslValue[str] | None = None
    s3_object_key: DslValue[str] | None = None


@dataclass
class SessionSummaryConfiguration(PropertyType):
    max_recent_sessions: DslValue[float] | None = None
