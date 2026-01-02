"""PropertyTypes for AWS::Lex::Bot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdvancedRecognitionSetting(PropertyType):
    audio_recognition_strategy: str | None = None


@dataclass
class AllowedInputTypes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "allow_dtmf_input": "AllowDTMFInput",
    }

    allow_audio_input: bool | None = None
    allow_dtmf_input: bool | None = None


@dataclass
class AudioAndDTMFInputSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "dtmf_specification": "DTMFSpecification",
    }

    start_timeout_ms: int | None = None
    audio_specification: AudioSpecification | None = None
    dtmf_specification: DTMFSpecification | None = None


@dataclass
class AudioLogDestination(PropertyType):
    s3_bucket: S3BucketLogDestination | None = None


@dataclass
class AudioLogSetting(PropertyType):
    destination: AudioLogDestination | None = None
    enabled: bool | None = None


@dataclass
class AudioSpecification(PropertyType):
    end_timeout_ms: int | None = None
    max_length_ms: int | None = None


@dataclass
class BKBExactResponseFields(PropertyType):
    answer_field: str | None = None


@dataclass
class BedrockAgentConfiguration(PropertyType):
    bedrock_agent_alias_id: str | None = None
    bedrock_agent_id: str | None = None


@dataclass
class BedrockAgentIntentConfiguration(PropertyType):
    bedrock_agent_configuration: BedrockAgentConfiguration | None = None
    bedrock_agent_intent_knowledge_base_configuration: (
        BedrockAgentIntentKnowledgeBaseConfiguration | None
    ) = None


@dataclass
class BedrockAgentIntentKnowledgeBaseConfiguration(PropertyType):
    bedrock_knowledge_base_arn: str | None = None
    bedrock_model_configuration: BedrockModelSpecification | None = None


@dataclass
class BedrockGuardrailConfiguration(PropertyType):
    bedrock_guardrail_identifier: str | None = None
    bedrock_guardrail_version: str | None = None


@dataclass
class BedrockKnowledgeStoreConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bkb_exact_response_fields": "BKBExactResponseFields",
    }

    bedrock_knowledge_base_arn: str | None = None
    bkb_exact_response_fields: BKBExactResponseFields | None = None
    exact_response: bool | None = None


@dataclass
class BedrockModelSpecification(PropertyType):
    model_arn: str | None = None
    bedrock_guardrail_configuration: BedrockGuardrailConfiguration | None = None
    bedrock_model_custom_prompt: str | None = None
    bedrock_trace_status: str | None = None


@dataclass
class BotAliasLocaleSettings(PropertyType):
    enabled: bool | None = None
    code_hook_specification: CodeHookSpecification | None = None


@dataclass
class BotAliasLocaleSettingsItem(PropertyType):
    bot_alias_locale_setting: BotAliasLocaleSettings | None = None
    locale_id: str | None = None


@dataclass
class BotLocale(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "generative_ai_settings": "GenerativeAISettings",
    }

    locale_id: str | None = None
    nlu_confidence_threshold: float | None = None
    custom_vocabulary: CustomVocabulary | None = None
    description: str | None = None
    generative_ai_settings: GenerativeAISettings | None = None
    intents: list[Intent] = field(default_factory=list)
    slot_types: list[SlotType] = field(default_factory=list)
    speech_detection_sensitivity: str | None = None
    unified_speech_settings: UnifiedSpeechSettings | None = None
    voice_settings: VoiceSettings | None = None


@dataclass
class BuildtimeSettings(PropertyType):
    descriptive_bot_builder_specification: DescriptiveBotBuilderSpecification | None = (
        None
    )
    sample_utterance_generation_specification: (
        SampleUtteranceGenerationSpecification | None
    ) = None


@dataclass
class Button(PropertyType):
    text: str | None = None
    value: str | None = None


@dataclass
class CloudWatchLogGroupLogDestination(PropertyType):
    cloud_watch_log_group_arn: str | None = None
    log_prefix: str | None = None


@dataclass
class CodeHookSpecification(PropertyType):
    lambda_code_hook: LambdaCodeHook | None = None


@dataclass
class CompositeSlotTypeSetting(PropertyType):
    sub_slots: list[SubSlotTypeComposition] = field(default_factory=list)


@dataclass
class Condition(PropertyType):
    expression_string: str | None = None


@dataclass
class ConditionalBranch(PropertyType):
    condition: Condition | None = None
    name: str | None = None
    next_step: DialogState | None = None
    response: ResponseSpecification | None = None


@dataclass
class ConditionalSpecification(PropertyType):
    conditional_branches: list[ConditionalBranch] = field(default_factory=list)
    default_branch: DefaultConditionalBranch | None = None
    is_active: bool | None = None


@dataclass
class ConversationLogSettings(PropertyType):
    audio_log_settings: list[AudioLogSetting] = field(default_factory=list)
    text_log_settings: list[TextLogSetting] = field(default_factory=list)


@dataclass
class CustomPayload(PropertyType):
    value: str | None = None


@dataclass
class CustomVocabulary(PropertyType):
    custom_vocabulary_items: list[CustomVocabularyItem] = field(default_factory=list)


@dataclass
class CustomVocabularyItem(PropertyType):
    phrase: str | None = None
    display_as: str | None = None
    weight: int | None = None


@dataclass
class DTMFSpecification(PropertyType):
    deletion_character: str | None = None
    end_character: str | None = None
    end_timeout_ms: int | None = None
    max_length: int | None = None


@dataclass
class DataPrivacy(PropertyType):
    child_directed: bool | None = None


@dataclass
class DataSourceConfiguration(PropertyType):
    bedrock_knowledge_store_configuration: BedrockKnowledgeStoreConfiguration | None = (
        None
    )
    kendra_configuration: QnAKendraConfiguration | None = None
    opensearch_configuration: OpensearchConfiguration | None = None


@dataclass
class DefaultConditionalBranch(PropertyType):
    next_step: DialogState | None = None
    response: ResponseSpecification | None = None


@dataclass
class DescriptiveBotBuilderSpecification(PropertyType):
    enabled: bool | None = None
    bedrock_model_specification: BedrockModelSpecification | None = None


@dataclass
class DialogAction(PropertyType):
    type_: str | None = None
    slot_to_elicit: str | None = None
    suppress_next_message: bool | None = None


@dataclass
class DialogCodeHookInvocationSetting(PropertyType):
    enable_code_hook_invocation: bool | None = None
    is_active: bool | None = None
    post_code_hook_specification: PostDialogCodeHookInvocationSpecification | None = (
        None
    )
    invocation_label: str | None = None


@dataclass
class DialogCodeHookSetting(PropertyType):
    enabled: bool | None = None


@dataclass
class DialogState(PropertyType):
    dialog_action: DialogAction | None = None
    intent: IntentOverride | None = None
    session_attributes: list[SessionAttribute] = field(default_factory=list)


@dataclass
class ElicitationCodeHookInvocationSetting(PropertyType):
    enable_code_hook_invocation: bool | None = None
    invocation_label: str | None = None


@dataclass
class ErrorLogSettings(PropertyType):
    enabled: bool | None = None


@dataclass
class ExactResponseFields(PropertyType):
    answer_field: str | None = None
    question_field: str | None = None


@dataclass
class ExternalSourceSetting(PropertyType):
    grammar_slot_type_setting: GrammarSlotTypeSetting | None = None


@dataclass
class FulfillmentCodeHookSetting(PropertyType):
    enabled: bool | None = None
    fulfillment_updates_specification: FulfillmentUpdatesSpecification | None = None
    is_active: bool | None = None
    post_fulfillment_status_specification: PostFulfillmentStatusSpecification | None = (
        None
    )


@dataclass
class FulfillmentStartResponseSpecification(PropertyType):
    delay_in_seconds: int | None = None
    message_groups: list[MessageGroup] = field(default_factory=list)
    allow_interrupt: bool | None = None


@dataclass
class FulfillmentUpdateResponseSpecification(PropertyType):
    frequency_in_seconds: int | None = None
    message_groups: list[MessageGroup] = field(default_factory=list)
    allow_interrupt: bool | None = None


@dataclass
class FulfillmentUpdatesSpecification(PropertyType):
    active: bool | None = None
    start_response: FulfillmentStartResponseSpecification | None = None
    timeout_in_seconds: int | None = None
    update_response: FulfillmentUpdateResponseSpecification | None = None


@dataclass
class GenerativeAISettings(PropertyType):
    buildtime_settings: BuildtimeSettings | None = None
    runtime_settings: RuntimeSettings | None = None


@dataclass
class GrammarSlotTypeSetting(PropertyType):
    source: GrammarSlotTypeSource | None = None


@dataclass
class GrammarSlotTypeSource(PropertyType):
    s3_bucket_name: str | None = None
    s3_object_key: str | None = None
    kms_key_arn: str | None = None


@dataclass
class ImageResponseCard(PropertyType):
    title: str | None = None
    buttons: list[Button] = field(default_factory=list)
    image_url: str | None = None
    subtitle: str | None = None


@dataclass
class InitialResponseSetting(PropertyType):
    code_hook: DialogCodeHookInvocationSetting | None = None
    conditional: ConditionalSpecification | None = None
    initial_response: ResponseSpecification | None = None
    next_step: DialogState | None = None


@dataclass
class InputContext(PropertyType):
    name: str | None = None


@dataclass
class Intent(PropertyType):
    name: str | None = None
    bedrock_agent_intent_configuration: BedrockAgentIntentConfiguration | None = None
    description: str | None = None
    dialog_code_hook: DialogCodeHookSetting | None = None
    display_name: str | None = None
    fulfillment_code_hook: FulfillmentCodeHookSetting | None = None
    initial_response_setting: InitialResponseSetting | None = None
    input_contexts: list[InputContext] = field(default_factory=list)
    intent_closing_setting: IntentClosingSetting | None = None
    intent_confirmation_setting: IntentConfirmationSetting | None = None
    kendra_configuration: KendraConfiguration | None = None
    output_contexts: list[OutputContext] = field(default_factory=list)
    parent_intent_signature: str | None = None
    q_in_connect_intent_configuration: QInConnectIntentConfiguration | None = None
    qn_a_intent_configuration: QnAIntentConfiguration | None = None
    sample_utterances: list[SampleUtterance] = field(default_factory=list)
    slot_priorities: list[SlotPriority] = field(default_factory=list)
    slots: list[Slot] = field(default_factory=list)


@dataclass
class IntentClosingSetting(PropertyType):
    closing_response: ResponseSpecification | None = None
    conditional: ConditionalSpecification | None = None
    is_active: bool | None = None
    next_step: DialogState | None = None


@dataclass
class IntentConfirmationSetting(PropertyType):
    prompt_specification: PromptSpecification | None = None
    code_hook: DialogCodeHookInvocationSetting | None = None
    confirmation_conditional: ConditionalSpecification | None = None
    confirmation_next_step: DialogState | None = None
    confirmation_response: ResponseSpecification | None = None
    declination_conditional: ConditionalSpecification | None = None
    declination_next_step: DialogState | None = None
    declination_response: ResponseSpecification | None = None
    elicitation_code_hook: ElicitationCodeHookInvocationSetting | None = None
    failure_conditional: ConditionalSpecification | None = None
    failure_next_step: DialogState | None = None
    failure_response: ResponseSpecification | None = None
    is_active: bool | None = None


@dataclass
class IntentDisambiguationSettings(PropertyType):
    enabled: bool | None = None
    custom_disambiguation_message: str | None = None
    max_disambiguation_intents: int | None = None


@dataclass
class IntentOverride(PropertyType):
    name: str | None = None
    slots: list[SlotValueOverrideMap] = field(default_factory=list)


@dataclass
class KendraConfiguration(PropertyType):
    kendra_index: str | None = None
    query_filter_string: str | None = None
    query_filter_string_enabled: bool | None = None


@dataclass
class LambdaCodeHook(PropertyType):
    code_hook_interface_version: str | None = None
    lambda_arn: str | None = None


@dataclass
class Message(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ssml_message": "SSMLMessage",
    }

    custom_payload: CustomPayload | None = None
    image_response_card: ImageResponseCard | None = None
    plain_text_message: PlainTextMessage | None = None
    ssml_message: SSMLMessage | None = None


@dataclass
class MessageGroup(PropertyType):
    message: Message | None = None
    variations: list[Message] = field(default_factory=list)


@dataclass
class MultipleValuesSetting(PropertyType):
    allow_multiple_values: bool | None = None


@dataclass
class NluImprovementSpecification(PropertyType):
    enabled: bool | None = None
    assisted_nlu_mode: str | None = None
    intent_disambiguation_settings: IntentDisambiguationSettings | None = None


@dataclass
class ObfuscationSetting(PropertyType):
    obfuscation_setting_type: str | None = None


@dataclass
class OpensearchConfiguration(PropertyType):
    domain_endpoint: str | None = None
    exact_response: bool | None = None
    exact_response_fields: ExactResponseFields | None = None
    include_fields: list[String] = field(default_factory=list)
    index_name: str | None = None


@dataclass
class OutputContext(PropertyType):
    name: str | None = None
    time_to_live_in_seconds: int | None = None
    turns_to_live: int | None = None


@dataclass
class PlainTextMessage(PropertyType):
    value: str | None = None


@dataclass
class PostDialogCodeHookInvocationSpecification(PropertyType):
    failure_conditional: ConditionalSpecification | None = None
    failure_next_step: DialogState | None = None
    failure_response: ResponseSpecification | None = None
    success_conditional: ConditionalSpecification | None = None
    success_next_step: DialogState | None = None
    success_response: ResponseSpecification | None = None
    timeout_conditional: ConditionalSpecification | None = None
    timeout_next_step: DialogState | None = None
    timeout_response: ResponseSpecification | None = None


@dataclass
class PostFulfillmentStatusSpecification(PropertyType):
    failure_conditional: ConditionalSpecification | None = None
    failure_next_step: DialogState | None = None
    failure_response: ResponseSpecification | None = None
    success_conditional: ConditionalSpecification | None = None
    success_next_step: DialogState | None = None
    success_response: ResponseSpecification | None = None
    timeout_conditional: ConditionalSpecification | None = None
    timeout_next_step: DialogState | None = None
    timeout_response: ResponseSpecification | None = None


@dataclass
class PromptAttemptSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "audio_and_dtmf_input_specification": "AudioAndDTMFInputSpecification",
    }

    allowed_input_types: AllowedInputTypes | None = None
    allow_interrupt: bool | None = None
    audio_and_dtmf_input_specification: AudioAndDTMFInputSpecification | None = None
    text_input_specification: TextInputSpecification | None = None


@dataclass
class PromptSpecification(PropertyType):
    max_retries: int | None = None
    message_groups_list: list[MessageGroup] = field(default_factory=list)
    allow_interrupt: bool | None = None
    message_selection_strategy: str | None = None
    prompt_attempts_specification: dict[str, PromptAttemptSpecification] = field(
        default_factory=dict
    )


@dataclass
class QInConnectAssistantConfiguration(PropertyType):
    assistant_arn: str | None = None


@dataclass
class QInConnectIntentConfiguration(PropertyType):
    q_in_connect_assistant_configuration: QInConnectAssistantConfiguration | None = None


@dataclass
class QnAIntentConfiguration(PropertyType):
    bedrock_model_configuration: BedrockModelSpecification | None = None
    data_source_configuration: DataSourceConfiguration | None = None


@dataclass
class QnAKendraConfiguration(PropertyType):
    exact_response: bool | None = None
    kendra_index: str | None = None
    query_filter_string_enabled: bool | None = None
    query_filter_string: str | None = None


@dataclass
class Replication(PropertyType):
    replica_regions: list[String] = field(default_factory=list)


@dataclass
class ResponseSpecification(PropertyType):
    message_groups_list: list[MessageGroup] = field(default_factory=list)
    allow_interrupt: bool | None = None


@dataclass
class RuntimeSettings(PropertyType):
    nlu_improvement_specification: NluImprovementSpecification | None = None
    slot_resolution_improvement_specification: (
        SlotResolutionImprovementSpecification | None
    ) = None


@dataclass
class S3BucketLogDestination(PropertyType):
    log_prefix: str | None = None
    s3_bucket_arn: str | None = None
    kms_key_arn: str | None = None


@dataclass
class S3Location(PropertyType):
    s3_bucket: str | None = None
    s3_object_key: str | None = None
    s3_object_version: str | None = None


@dataclass
class SSMLMessage(PropertyType):
    value: str | None = None


@dataclass
class SampleUtterance(PropertyType):
    utterance: str | None = None


@dataclass
class SampleUtteranceGenerationSpecification(PropertyType):
    enabled: bool | None = None
    bedrock_model_specification: BedrockModelSpecification | None = None


@dataclass
class SampleValue(PropertyType):
    value: str | None = None


@dataclass
class SentimentAnalysisSettings(PropertyType):
    detect_sentiment: bool | None = None


@dataclass
class SessionAttribute(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class Slot(PropertyType):
    name: str | None = None
    slot_type_name: str | None = None
    value_elicitation_setting: SlotValueElicitationSetting | None = None
    description: str | None = None
    multiple_values_setting: MultipleValuesSetting | None = None
    obfuscation_setting: ObfuscationSetting | None = None
    sub_slot_setting: SubSlotSetting | None = None


@dataclass
class SlotCaptureSetting(PropertyType):
    capture_conditional: ConditionalSpecification | None = None
    capture_next_step: DialogState | None = None
    capture_response: ResponseSpecification | None = None
    code_hook: DialogCodeHookInvocationSetting | None = None
    elicitation_code_hook: ElicitationCodeHookInvocationSetting | None = None
    failure_conditional: ConditionalSpecification | None = None
    failure_next_step: DialogState | None = None
    failure_response: ResponseSpecification | None = None


@dataclass
class SlotDefaultValue(PropertyType):
    default_value: str | None = None


@dataclass
class SlotDefaultValueSpecification(PropertyType):
    default_value_list: list[SlotDefaultValue] = field(default_factory=list)


@dataclass
class SlotPriority(PropertyType):
    priority: int | None = None
    slot_name: str | None = None


@dataclass
class SlotResolutionImprovementSpecification(PropertyType):
    enabled: bool | None = None
    bedrock_model_specification: BedrockModelSpecification | None = None


@dataclass
class SlotType(PropertyType):
    name: str | None = None
    composite_slot_type_setting: CompositeSlotTypeSetting | None = None
    description: str | None = None
    external_source_setting: ExternalSourceSetting | None = None
    parent_slot_type_signature: str | None = None
    slot_type_values: list[SlotTypeValue] = field(default_factory=list)
    value_selection_setting: SlotValueSelectionSetting | None = None


@dataclass
class SlotTypeValue(PropertyType):
    sample_value: SampleValue | None = None
    synonyms: list[SampleValue] = field(default_factory=list)


@dataclass
class SlotValue(PropertyType):
    interpreted_value: str | None = None


@dataclass
class SlotValueElicitationSetting(PropertyType):
    slot_constraint: str | None = None
    default_value_specification: SlotDefaultValueSpecification | None = None
    prompt_specification: PromptSpecification | None = None
    sample_utterances: list[SampleUtterance] = field(default_factory=list)
    slot_capture_setting: SlotCaptureSetting | None = None
    wait_and_continue_specification: WaitAndContinueSpecification | None = None


@dataclass
class SlotValueOverride(PropertyType):
    shape: str | None = None
    value: SlotValue | None = None
    values: list[SlotValueOverride] = field(default_factory=list)


@dataclass
class SlotValueOverrideMap(PropertyType):
    slot_name: str | None = None
    slot_value_override: SlotValueOverride | None = None


@dataclass
class SlotValueRegexFilter(PropertyType):
    pattern: str | None = None


@dataclass
class SlotValueSelectionSetting(PropertyType):
    resolution_strategy: str | None = None
    advanced_recognition_setting: AdvancedRecognitionSetting | None = None
    regex_filter: SlotValueRegexFilter | None = None


@dataclass
class Specifications(PropertyType):
    value_elicitation_setting: SubSlotValueElicitationSetting | None = None
    slot_type_id: str | None = None
    slot_type_name: str | None = None


@dataclass
class SpeechFoundationModel(PropertyType):
    model_arn: str | None = None
    voice_id: str | None = None


@dataclass
class StillWaitingResponseSpecification(PropertyType):
    frequency_in_seconds: int | None = None
    message_groups_list: list[MessageGroup] = field(default_factory=list)
    timeout_in_seconds: int | None = None
    allow_interrupt: bool | None = None


@dataclass
class SubSlotSetting(PropertyType):
    expression: str | None = None
    slot_specifications: dict[str, Specifications] = field(default_factory=dict)


@dataclass
class SubSlotTypeComposition(PropertyType):
    name: str | None = None
    slot_type_id: str | None = None
    slot_type_name: str | None = None


@dataclass
class SubSlotValueElicitationSetting(PropertyType):
    default_value_specification: SlotDefaultValueSpecification | None = None
    prompt_specification: PromptSpecification | None = None
    sample_utterances: list[SampleUtterance] = field(default_factory=list)
    wait_and_continue_specification: WaitAndContinueSpecification | None = None


@dataclass
class TestBotAliasSettings(PropertyType):
    bot_alias_locale_settings: list[BotAliasLocaleSettingsItem] = field(
        default_factory=list
    )
    conversation_log_settings: ConversationLogSettings | None = None
    description: str | None = None
    sentiment_analysis_settings: SentimentAnalysisSettings | None = None


@dataclass
class TextInputSpecification(PropertyType):
    start_timeout_ms: int | None = None


@dataclass
class TextLogDestination(PropertyType):
    cloud_watch: CloudWatchLogGroupLogDestination | None = None


@dataclass
class TextLogSetting(PropertyType):
    destination: TextLogDestination | None = None
    enabled: bool | None = None


@dataclass
class UnifiedSpeechSettings(PropertyType):
    speech_foundation_model: SpeechFoundationModel | None = None


@dataclass
class VoiceSettings(PropertyType):
    voice_id: str | None = None
    engine: str | None = None


@dataclass
class WaitAndContinueSpecification(PropertyType):
    continue_response: ResponseSpecification | None = None
    waiting_response: ResponseSpecification | None = None
    is_active: bool | None = None
    still_waiting_response: StillWaitingResponseSpecification | None = None
