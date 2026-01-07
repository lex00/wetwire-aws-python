"""PropertyTypes for AWS::Lex::Bot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdvancedRecognitionSetting(PropertyType):
    audio_recognition_strategy: DslValue[str] | None = None


@dataclass
class AllowedInputTypes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_dtmf_input": "AllowDTMFInput",
    }

    allow_audio_input: DslValue[bool] | None = None
    allow_dtmf_input: DslValue[bool] | None = None


@dataclass
class AudioAndDTMFInputSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dtmf_specification": "DTMFSpecification",
    }

    start_timeout_ms: DslValue[int] | None = None
    audio_specification: DslValue[AudioSpecification] | None = None
    dtmf_specification: DslValue[DTMFSpecification] | None = None


@dataclass
class AudioLogDestination(PropertyType):
    s3_bucket: DslValue[S3BucketLogDestination] | None = None


@dataclass
class AudioLogSetting(PropertyType):
    destination: DslValue[AudioLogDestination] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class AudioSpecification(PropertyType):
    end_timeout_ms: DslValue[int] | None = None
    max_length_ms: DslValue[int] | None = None


@dataclass
class BKBExactResponseFields(PropertyType):
    answer_field: DslValue[str] | None = None


@dataclass
class BedrockAgentConfiguration(PropertyType):
    bedrock_agent_alias_id: DslValue[str] | None = None
    bedrock_agent_id: DslValue[str] | None = None


@dataclass
class BedrockAgentIntentConfiguration(PropertyType):
    bedrock_agent_configuration: DslValue[BedrockAgentConfiguration] | None = None
    bedrock_agent_intent_knowledge_base_configuration: (
        DslValue[BedrockAgentIntentKnowledgeBaseConfiguration] | None
    ) = None


@dataclass
class BedrockAgentIntentKnowledgeBaseConfiguration(PropertyType):
    bedrock_knowledge_base_arn: DslValue[str] | None = None
    bedrock_model_configuration: DslValue[BedrockModelSpecification] | None = None


@dataclass
class BedrockGuardrailConfiguration(PropertyType):
    bedrock_guardrail_identifier: DslValue[str] | None = None
    bedrock_guardrail_version: DslValue[str] | None = None


@dataclass
class BedrockKnowledgeStoreConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bkb_exact_response_fields": "BKBExactResponseFields",
    }

    bedrock_knowledge_base_arn: DslValue[str] | None = None
    bkb_exact_response_fields: DslValue[BKBExactResponseFields] | None = None
    exact_response: DslValue[bool] | None = None


@dataclass
class BedrockModelSpecification(PropertyType):
    model_arn: DslValue[str] | None = None
    bedrock_guardrail_configuration: DslValue[BedrockGuardrailConfiguration] | None = (
        None
    )
    bedrock_model_custom_prompt: DslValue[str] | None = None
    bedrock_trace_status: DslValue[str] | None = None


@dataclass
class BotAliasLocaleSettings(PropertyType):
    enabled: DslValue[bool] | None = None
    code_hook_specification: DslValue[CodeHookSpecification] | None = None


@dataclass
class BotAliasLocaleSettingsItem(PropertyType):
    bot_alias_locale_setting: DslValue[BotAliasLocaleSettings] | None = None
    locale_id: DslValue[str] | None = None


@dataclass
class BotLocale(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "generative_ai_settings": "GenerativeAISettings",
    }

    locale_id: DslValue[str] | None = None
    nlu_confidence_threshold: DslValue[float] | None = None
    custom_vocabulary: DslValue[CustomVocabulary] | None = None
    description: DslValue[str] | None = None
    generative_ai_settings: DslValue[GenerativeAISettings] | None = None
    intents: list[DslValue[Intent]] = field(default_factory=list)
    slot_types: list[DslValue[SlotType]] = field(default_factory=list)
    speech_detection_sensitivity: DslValue[str] | None = None
    unified_speech_settings: DslValue[UnifiedSpeechSettings] | None = None
    voice_settings: DslValue[VoiceSettings] | None = None


@dataclass
class BuildtimeSettings(PropertyType):
    descriptive_bot_builder_specification: (
        DslValue[DescriptiveBotBuilderSpecification] | None
    ) = None
    sample_utterance_generation_specification: (
        DslValue[SampleUtteranceGenerationSpecification] | None
    ) = None


@dataclass
class Button(PropertyType):
    text: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class CloudWatchLogGroupLogDestination(PropertyType):
    cloud_watch_log_group_arn: DslValue[str] | None = None
    log_prefix: DslValue[str] | None = None


@dataclass
class CodeHookSpecification(PropertyType):
    lambda_code_hook: DslValue[LambdaCodeHook] | None = None


@dataclass
class CompositeSlotTypeSetting(PropertyType):
    sub_slots: list[DslValue[SubSlotTypeComposition]] = field(default_factory=list)


@dataclass
class Condition(PropertyType):
    expression_string: DslValue[str] | None = None


@dataclass
class ConditionalBranch(PropertyType):
    condition: DslValue[Condition] | None = None
    name: DslValue[str] | None = None
    next_step: DslValue[DialogState] | None = None
    response: DslValue[ResponseSpecification] | None = None


@dataclass
class ConditionalSpecification(PropertyType):
    conditional_branches: list[DslValue[ConditionalBranch]] = field(
        default_factory=list
    )
    default_branch: DslValue[DefaultConditionalBranch] | None = None
    is_active: DslValue[bool] | None = None


@dataclass
class ConversationLogSettings(PropertyType):
    audio_log_settings: list[DslValue[AudioLogSetting]] = field(default_factory=list)
    text_log_settings: list[DslValue[TextLogSetting]] = field(default_factory=list)


@dataclass
class CustomPayload(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class CustomVocabulary(PropertyType):
    custom_vocabulary_items: list[DslValue[CustomVocabularyItem]] = field(
        default_factory=list
    )


@dataclass
class CustomVocabularyItem(PropertyType):
    phrase: DslValue[str] | None = None
    display_as: DslValue[str] | None = None
    weight: DslValue[int] | None = None


@dataclass
class DTMFSpecification(PropertyType):
    deletion_character: DslValue[str] | None = None
    end_character: DslValue[str] | None = None
    end_timeout_ms: DslValue[int] | None = None
    max_length: DslValue[int] | None = None


@dataclass
class DataPrivacy(PropertyType):
    child_directed: DslValue[bool] | None = None


@dataclass
class DataSourceConfiguration(PropertyType):
    bedrock_knowledge_store_configuration: (
        DslValue[BedrockKnowledgeStoreConfiguration] | None
    ) = None
    kendra_configuration: DslValue[QnAKendraConfiguration] | None = None
    opensearch_configuration: DslValue[OpensearchConfiguration] | None = None


@dataclass
class DefaultConditionalBranch(PropertyType):
    next_step: DslValue[DialogState] | None = None
    response: DslValue[ResponseSpecification] | None = None


@dataclass
class DescriptiveBotBuilderSpecification(PropertyType):
    enabled: DslValue[bool] | None = None
    bedrock_model_specification: DslValue[BedrockModelSpecification] | None = None


@dataclass
class DialogAction(PropertyType):
    type_: DslValue[str] | None = None
    slot_to_elicit: DslValue[str] | None = None
    suppress_next_message: DslValue[bool] | None = None


@dataclass
class DialogCodeHookInvocationSetting(PropertyType):
    enable_code_hook_invocation: DslValue[bool] | None = None
    is_active: DslValue[bool] | None = None
    post_code_hook_specification: (
        DslValue[PostDialogCodeHookInvocationSpecification] | None
    ) = None
    invocation_label: DslValue[str] | None = None


@dataclass
class DialogCodeHookSetting(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class DialogState(PropertyType):
    dialog_action: DslValue[DialogAction] | None = None
    intent: DslValue[IntentOverride] | None = None
    session_attributes: list[DslValue[SessionAttribute]] = field(default_factory=list)


@dataclass
class ElicitationCodeHookInvocationSetting(PropertyType):
    enable_code_hook_invocation: DslValue[bool] | None = None
    invocation_label: DslValue[str] | None = None


@dataclass
class ErrorLogSettings(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class ExactResponseFields(PropertyType):
    answer_field: DslValue[str] | None = None
    question_field: DslValue[str] | None = None


@dataclass
class ExternalSourceSetting(PropertyType):
    grammar_slot_type_setting: DslValue[GrammarSlotTypeSetting] | None = None


@dataclass
class FulfillmentCodeHookSetting(PropertyType):
    enabled: DslValue[bool] | None = None
    fulfillment_updates_specification: (
        DslValue[FulfillmentUpdatesSpecification] | None
    ) = None
    is_active: DslValue[bool] | None = None
    post_fulfillment_status_specification: (
        DslValue[PostFulfillmentStatusSpecification] | None
    ) = None


@dataclass
class FulfillmentStartResponseSpecification(PropertyType):
    delay_in_seconds: DslValue[int] | None = None
    message_groups: list[DslValue[MessageGroup]] = field(default_factory=list)
    allow_interrupt: DslValue[bool] | None = None


@dataclass
class FulfillmentUpdateResponseSpecification(PropertyType):
    frequency_in_seconds: DslValue[int] | None = None
    message_groups: list[DslValue[MessageGroup]] = field(default_factory=list)
    allow_interrupt: DslValue[bool] | None = None


@dataclass
class FulfillmentUpdatesSpecification(PropertyType):
    active: DslValue[bool] | None = None
    start_response: DslValue[FulfillmentStartResponseSpecification] | None = None
    timeout_in_seconds: DslValue[int] | None = None
    update_response: DslValue[FulfillmentUpdateResponseSpecification] | None = None


@dataclass
class GenerativeAISettings(PropertyType):
    buildtime_settings: DslValue[BuildtimeSettings] | None = None
    runtime_settings: DslValue[RuntimeSettings] | None = None


@dataclass
class GrammarSlotTypeSetting(PropertyType):
    source: DslValue[GrammarSlotTypeSource] | None = None


@dataclass
class GrammarSlotTypeSource(PropertyType):
    s3_bucket_name: DslValue[str] | None = None
    s3_object_key: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class ImageResponseCard(PropertyType):
    title: DslValue[str] | None = None
    buttons: list[DslValue[Button]] = field(default_factory=list)
    image_url: DslValue[str] | None = None
    subtitle: DslValue[str] | None = None


@dataclass
class InitialResponseSetting(PropertyType):
    code_hook: DslValue[DialogCodeHookInvocationSetting] | None = None
    conditional: DslValue[ConditionalSpecification] | None = None
    initial_response: DslValue[ResponseSpecification] | None = None
    next_step: DslValue[DialogState] | None = None


@dataclass
class InputContext(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class Intent(PropertyType):
    name: DslValue[str] | None = None
    bedrock_agent_intent_configuration: (
        DslValue[BedrockAgentIntentConfiguration] | None
    ) = None
    description: DslValue[str] | None = None
    dialog_code_hook: DslValue[DialogCodeHookSetting] | None = None
    display_name: DslValue[str] | None = None
    fulfillment_code_hook: DslValue[FulfillmentCodeHookSetting] | None = None
    initial_response_setting: DslValue[InitialResponseSetting] | None = None
    input_contexts: list[DslValue[InputContext]] = field(default_factory=list)
    intent_closing_setting: DslValue[IntentClosingSetting] | None = None
    intent_confirmation_setting: DslValue[IntentConfirmationSetting] | None = None
    kendra_configuration: DslValue[KendraConfiguration] | None = None
    output_contexts: list[DslValue[OutputContext]] = field(default_factory=list)
    parent_intent_signature: DslValue[str] | None = None
    q_in_connect_intent_configuration: (
        DslValue[QInConnectIntentConfiguration] | None
    ) = None
    qn_a_intent_configuration: DslValue[QnAIntentConfiguration] | None = None
    sample_utterances: list[DslValue[SampleUtterance]] = field(default_factory=list)
    slot_priorities: list[DslValue[SlotPriority]] = field(default_factory=list)
    slots: list[DslValue[Slot]] = field(default_factory=list)


@dataclass
class IntentClosingSetting(PropertyType):
    closing_response: DslValue[ResponseSpecification] | None = None
    conditional: DslValue[ConditionalSpecification] | None = None
    is_active: DslValue[bool] | None = None
    next_step: DslValue[DialogState] | None = None


@dataclass
class IntentConfirmationSetting(PropertyType):
    prompt_specification: DslValue[PromptSpecification] | None = None
    code_hook: DslValue[DialogCodeHookInvocationSetting] | None = None
    confirmation_conditional: DslValue[ConditionalSpecification] | None = None
    confirmation_next_step: DslValue[DialogState] | None = None
    confirmation_response: DslValue[ResponseSpecification] | None = None
    declination_conditional: DslValue[ConditionalSpecification] | None = None
    declination_next_step: DslValue[DialogState] | None = None
    declination_response: DslValue[ResponseSpecification] | None = None
    elicitation_code_hook: DslValue[ElicitationCodeHookInvocationSetting] | None = None
    failure_conditional: DslValue[ConditionalSpecification] | None = None
    failure_next_step: DslValue[DialogState] | None = None
    failure_response: DslValue[ResponseSpecification] | None = None
    is_active: DslValue[bool] | None = None


@dataclass
class IntentDisambiguationSettings(PropertyType):
    enabled: DslValue[bool] | None = None
    custom_disambiguation_message: DslValue[str] | None = None
    max_disambiguation_intents: DslValue[int] | None = None


@dataclass
class IntentOverride(PropertyType):
    name: DslValue[str] | None = None
    slots: list[DslValue[SlotValueOverrideMap]] = field(default_factory=list)


@dataclass
class KendraConfiguration(PropertyType):
    kendra_index: DslValue[str] | None = None
    query_filter_string: DslValue[str] | None = None
    query_filter_string_enabled: DslValue[bool] | None = None


@dataclass
class LambdaCodeHook(PropertyType):
    code_hook_interface_version: DslValue[str] | None = None
    lambda_arn: DslValue[str] | None = None


@dataclass
class Message(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ssml_message": "SSMLMessage",
    }

    custom_payload: DslValue[CustomPayload] | None = None
    image_response_card: DslValue[ImageResponseCard] | None = None
    plain_text_message: DslValue[PlainTextMessage] | None = None
    ssml_message: DslValue[SSMLMessage] | None = None


@dataclass
class MessageGroup(PropertyType):
    message: DslValue[Message] | None = None
    variations: list[DslValue[Message]] = field(default_factory=list)


@dataclass
class MultipleValuesSetting(PropertyType):
    allow_multiple_values: DslValue[bool] | None = None


@dataclass
class NluImprovementSpecification(PropertyType):
    enabled: DslValue[bool] | None = None
    assisted_nlu_mode: DslValue[str] | None = None
    intent_disambiguation_settings: DslValue[IntentDisambiguationSettings] | None = None


@dataclass
class ObfuscationSetting(PropertyType):
    obfuscation_setting_type: DslValue[str] | None = None


@dataclass
class OpensearchConfiguration(PropertyType):
    domain_endpoint: DslValue[str] | None = None
    exact_response: DslValue[bool] | None = None
    exact_response_fields: DslValue[ExactResponseFields] | None = None
    include_fields: list[DslValue[str]] = field(default_factory=list)
    index_name: DslValue[str] | None = None


@dataclass
class OutputContext(PropertyType):
    name: DslValue[str] | None = None
    time_to_live_in_seconds: DslValue[int] | None = None
    turns_to_live: DslValue[int] | None = None


@dataclass
class PlainTextMessage(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class PostDialogCodeHookInvocationSpecification(PropertyType):
    failure_conditional: DslValue[ConditionalSpecification] | None = None
    failure_next_step: DslValue[DialogState] | None = None
    failure_response: DslValue[ResponseSpecification] | None = None
    success_conditional: DslValue[ConditionalSpecification] | None = None
    success_next_step: DslValue[DialogState] | None = None
    success_response: DslValue[ResponseSpecification] | None = None
    timeout_conditional: DslValue[ConditionalSpecification] | None = None
    timeout_next_step: DslValue[DialogState] | None = None
    timeout_response: DslValue[ResponseSpecification] | None = None


@dataclass
class PostFulfillmentStatusSpecification(PropertyType):
    failure_conditional: DslValue[ConditionalSpecification] | None = None
    failure_next_step: DslValue[DialogState] | None = None
    failure_response: DslValue[ResponseSpecification] | None = None
    success_conditional: DslValue[ConditionalSpecification] | None = None
    success_next_step: DslValue[DialogState] | None = None
    success_response: DslValue[ResponseSpecification] | None = None
    timeout_conditional: DslValue[ConditionalSpecification] | None = None
    timeout_next_step: DslValue[DialogState] | None = None
    timeout_response: DslValue[ResponseSpecification] | None = None


@dataclass
class PromptAttemptSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_and_dtmf_input_specification": "AudioAndDTMFInputSpecification",
    }

    allowed_input_types: DslValue[AllowedInputTypes] | None = None
    allow_interrupt: DslValue[bool] | None = None
    audio_and_dtmf_input_specification: (
        DslValue[AudioAndDTMFInputSpecification] | None
    ) = None
    text_input_specification: DslValue[TextInputSpecification] | None = None


@dataclass
class PromptSpecification(PropertyType):
    max_retries: DslValue[int] | None = None
    message_groups_list: list[DslValue[MessageGroup]] = field(default_factory=list)
    allow_interrupt: DslValue[bool] | None = None
    message_selection_strategy: DslValue[str] | None = None
    prompt_attempts_specification: dict[str, DslValue[PromptAttemptSpecification]] = (
        field(default_factory=dict)
    )


@dataclass
class QInConnectAssistantConfiguration(PropertyType):
    assistant_arn: DslValue[str] | None = None


@dataclass
class QInConnectIntentConfiguration(PropertyType):
    q_in_connect_assistant_configuration: (
        DslValue[QInConnectAssistantConfiguration] | None
    ) = None


@dataclass
class QnAIntentConfiguration(PropertyType):
    bedrock_model_configuration: DslValue[BedrockModelSpecification] | None = None
    data_source_configuration: DslValue[DataSourceConfiguration] | None = None


@dataclass
class QnAKendraConfiguration(PropertyType):
    exact_response: DslValue[bool] | None = None
    kendra_index: DslValue[str] | None = None
    query_filter_string_enabled: DslValue[bool] | None = None
    query_filter_string: DslValue[str] | None = None


@dataclass
class Replication(PropertyType):
    replica_regions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ResponseSpecification(PropertyType):
    message_groups_list: list[DslValue[MessageGroup]] = field(default_factory=list)
    allow_interrupt: DslValue[bool] | None = None


@dataclass
class RuntimeSettings(PropertyType):
    nlu_improvement_specification: DslValue[NluImprovementSpecification] | None = None
    slot_resolution_improvement_specification: (
        DslValue[SlotResolutionImprovementSpecification] | None
    ) = None


@dataclass
class S3BucketLogDestination(PropertyType):
    log_prefix: DslValue[str] | None = None
    s3_bucket_arn: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class S3Location(PropertyType):
    s3_bucket: DslValue[str] | None = None
    s3_object_key: DslValue[str] | None = None
    s3_object_version: DslValue[str] | None = None


@dataclass
class SSMLMessage(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class SampleUtterance(PropertyType):
    utterance: DslValue[str] | None = None


@dataclass
class SampleUtteranceGenerationSpecification(PropertyType):
    enabled: DslValue[bool] | None = None
    bedrock_model_specification: DslValue[BedrockModelSpecification] | None = None


@dataclass
class SampleValue(PropertyType):
    value: DslValue[str] | None = None


@dataclass
class SentimentAnalysisSettings(PropertyType):
    detect_sentiment: DslValue[bool] | None = None


@dataclass
class SessionAttribute(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class Slot(PropertyType):
    name: DslValue[str] | None = None
    slot_type_name: DslValue[str] | None = None
    value_elicitation_setting: DslValue[SlotValueElicitationSetting] | None = None
    description: DslValue[str] | None = None
    multiple_values_setting: DslValue[MultipleValuesSetting] | None = None
    obfuscation_setting: DslValue[ObfuscationSetting] | None = None
    sub_slot_setting: DslValue[SubSlotSetting] | None = None


@dataclass
class SlotCaptureSetting(PropertyType):
    capture_conditional: DslValue[ConditionalSpecification] | None = None
    capture_next_step: DslValue[DialogState] | None = None
    capture_response: DslValue[ResponseSpecification] | None = None
    code_hook: DslValue[DialogCodeHookInvocationSetting] | None = None
    elicitation_code_hook: DslValue[ElicitationCodeHookInvocationSetting] | None = None
    failure_conditional: DslValue[ConditionalSpecification] | None = None
    failure_next_step: DslValue[DialogState] | None = None
    failure_response: DslValue[ResponseSpecification] | None = None


@dataclass
class SlotDefaultValue(PropertyType):
    default_value: DslValue[str] | None = None


@dataclass
class SlotDefaultValueSpecification(PropertyType):
    default_value_list: list[DslValue[SlotDefaultValue]] = field(default_factory=list)


@dataclass
class SlotPriority(PropertyType):
    priority: DslValue[int] | None = None
    slot_name: DslValue[str] | None = None


@dataclass
class SlotResolutionImprovementSpecification(PropertyType):
    enabled: DslValue[bool] | None = None
    bedrock_model_specification: DslValue[BedrockModelSpecification] | None = None


@dataclass
class SlotType(PropertyType):
    name: DslValue[str] | None = None
    composite_slot_type_setting: DslValue[CompositeSlotTypeSetting] | None = None
    description: DslValue[str] | None = None
    external_source_setting: DslValue[ExternalSourceSetting] | None = None
    parent_slot_type_signature: DslValue[str] | None = None
    slot_type_values: list[DslValue[SlotTypeValue]] = field(default_factory=list)
    value_selection_setting: DslValue[SlotValueSelectionSetting] | None = None


@dataclass
class SlotTypeValue(PropertyType):
    sample_value: DslValue[SampleValue] | None = None
    synonyms: list[DslValue[SampleValue]] = field(default_factory=list)


@dataclass
class SlotValue(PropertyType):
    interpreted_value: DslValue[str] | None = None


@dataclass
class SlotValueElicitationSetting(PropertyType):
    slot_constraint: DslValue[str] | None = None
    default_value_specification: DslValue[SlotDefaultValueSpecification] | None = None
    prompt_specification: DslValue[PromptSpecification] | None = None
    sample_utterances: list[DslValue[SampleUtterance]] = field(default_factory=list)
    slot_capture_setting: DslValue[SlotCaptureSetting] | None = None
    wait_and_continue_specification: DslValue[WaitAndContinueSpecification] | None = (
        None
    )


@dataclass
class SlotValueOverride(PropertyType):
    shape: DslValue[str] | None = None
    value: DslValue[SlotValue] | None = None
    values: list[DslValue[SlotValueOverride]] = field(default_factory=list)


@dataclass
class SlotValueOverrideMap(PropertyType):
    slot_name: DslValue[str] | None = None
    slot_value_override: DslValue[SlotValueOverride] | None = None


@dataclass
class SlotValueRegexFilter(PropertyType):
    pattern: DslValue[str] | None = None


@dataclass
class SlotValueSelectionSetting(PropertyType):
    resolution_strategy: DslValue[str] | None = None
    advanced_recognition_setting: DslValue[AdvancedRecognitionSetting] | None = None
    regex_filter: DslValue[SlotValueRegexFilter] | None = None


@dataclass
class Specifications(PropertyType):
    value_elicitation_setting: DslValue[SubSlotValueElicitationSetting] | None = None
    slot_type_id: DslValue[str] | None = None
    slot_type_name: DslValue[str] | None = None


@dataclass
class SpeechFoundationModel(PropertyType):
    model_arn: DslValue[str] | None = None
    voice_id: DslValue[str] | None = None


@dataclass
class StillWaitingResponseSpecification(PropertyType):
    frequency_in_seconds: DslValue[int] | None = None
    message_groups_list: list[DslValue[MessageGroup]] = field(default_factory=list)
    timeout_in_seconds: DslValue[int] | None = None
    allow_interrupt: DslValue[bool] | None = None


@dataclass
class SubSlotSetting(PropertyType):
    expression: DslValue[str] | None = None
    slot_specifications: dict[str, DslValue[Specifications]] = field(
        default_factory=dict
    )


@dataclass
class SubSlotTypeComposition(PropertyType):
    name: DslValue[str] | None = None
    slot_type_id: DslValue[str] | None = None
    slot_type_name: DslValue[str] | None = None


@dataclass
class SubSlotValueElicitationSetting(PropertyType):
    default_value_specification: DslValue[SlotDefaultValueSpecification] | None = None
    prompt_specification: DslValue[PromptSpecification] | None = None
    sample_utterances: list[DslValue[SampleUtterance]] = field(default_factory=list)
    wait_and_continue_specification: DslValue[WaitAndContinueSpecification] | None = (
        None
    )


@dataclass
class TestBotAliasSettings(PropertyType):
    bot_alias_locale_settings: list[DslValue[BotAliasLocaleSettingsItem]] = field(
        default_factory=list
    )
    conversation_log_settings: DslValue[ConversationLogSettings] | None = None
    description: DslValue[str] | None = None
    sentiment_analysis_settings: DslValue[SentimentAnalysisSettings] | None = None


@dataclass
class TextInputSpecification(PropertyType):
    start_timeout_ms: DslValue[int] | None = None


@dataclass
class TextLogDestination(PropertyType):
    cloud_watch: DslValue[CloudWatchLogGroupLogDestination] | None = None


@dataclass
class TextLogSetting(PropertyType):
    destination: DslValue[TextLogDestination] | None = None
    enabled: DslValue[bool] | None = None


@dataclass
class UnifiedSpeechSettings(PropertyType):
    speech_foundation_model: DslValue[SpeechFoundationModel] | None = None


@dataclass
class VoiceSettings(PropertyType):
    voice_id: DslValue[str] | None = None
    engine: DslValue[str] | None = None


@dataclass
class WaitAndContinueSpecification(PropertyType):
    continue_response: DslValue[ResponseSpecification] | None = None
    waiting_response: DslValue[ResponseSpecification] | None = None
    is_active: DslValue[bool] | None = None
    still_waiting_response: DslValue[StillWaitingResponseSpecification] | None = None
