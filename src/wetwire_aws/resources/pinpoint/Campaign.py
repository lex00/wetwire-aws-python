"""PropertyTypes for AWS::Pinpoint::Campaign."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeDimension(PropertyType):
    attribute_type: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class CampaignCustomMessage(PropertyType):
    data: str | None = None


@dataclass
class CampaignEmailMessage(PropertyType):
    body: str | None = None
    from_address: str | None = None
    html_body: str | None = None
    title: str | None = None


@dataclass
class CampaignEventFilter(PropertyType):
    dimensions: EventDimensions | None = None
    filter_type: str | None = None


@dataclass
class CampaignHook(PropertyType):
    lambda_function_name: str | None = None
    mode: str | None = None
    web_url: str | None = None


@dataclass
class CampaignInAppMessage(PropertyType):
    content: list[InAppMessageContent] = field(default_factory=list)
    custom_config: dict[str, Any] | None = None
    layout: str | None = None


@dataclass
class CampaignSmsMessage(PropertyType):
    body: str | None = None
    entity_id: str | None = None
    message_type: str | None = None
    origination_number: str | None = None
    sender_id: str | None = None
    template_id: str | None = None


@dataclass
class CustomDeliveryConfiguration(PropertyType):
    delivery_uri: str | None = None
    endpoint_types: list[String] = field(default_factory=list)


@dataclass
class DefaultButtonConfiguration(PropertyType):
    background_color: str | None = None
    border_radius: int | None = None
    button_action: str | None = None
    link: str | None = None
    text: str | None = None
    text_color: str | None = None


@dataclass
class EventDimensions(PropertyType):
    attributes: dict[str, Any] | None = None
    event_type: SetDimension | None = None
    metrics: dict[str, Any] | None = None


@dataclass
class InAppMessageBodyConfig(PropertyType):
    alignment: str | None = None
    body: str | None = None
    text_color: str | None = None


@dataclass
class InAppMessageButton(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ios": "IOS",
    }

    android: OverrideButtonConfiguration | None = None
    default_config: DefaultButtonConfiguration | None = None
    ios: OverrideButtonConfiguration | None = None
    web: OverrideButtonConfiguration | None = None


@dataclass
class InAppMessageContent(PropertyType):
    background_color: str | None = None
    body_config: InAppMessageBodyConfig | None = None
    header_config: InAppMessageHeaderConfig | None = None
    image_url: str | None = None
    primary_btn: InAppMessageButton | None = None
    secondary_btn: InAppMessageButton | None = None


@dataclass
class InAppMessageHeaderConfig(PropertyType):
    alignment: str | None = None
    header: str | None = None
    text_color: str | None = None


@dataclass
class Limits(PropertyType):
    daily: int | None = None
    maximum_duration: int | None = None
    messages_per_second: int | None = None
    session: int | None = None
    total: int | None = None


@dataclass
class Message(PropertyType):
    action: str | None = None
    body: str | None = None
    image_icon_url: str | None = None
    image_small_icon_url: str | None = None
    image_url: str | None = None
    json_body: str | None = None
    media_url: str | None = None
    raw_content: str | None = None
    silent_push: bool | None = None
    time_to_live: int | None = None
    title: str | None = None
    url: str | None = None


@dataclass
class MessageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "adm_message": "ADMMessage",
        "apns_message": "APNSMessage",
        "gcm_message": "GCMMessage",
        "sms_message": "SMSMessage",
    }

    adm_message: Message | None = None
    apns_message: Message | None = None
    baidu_message: Message | None = None
    custom_message: CampaignCustomMessage | None = None
    default_message: Message | None = None
    email_message: CampaignEmailMessage | None = None
    gcm_message: Message | None = None
    in_app_message: CampaignInAppMessage | None = None
    sms_message: CampaignSmsMessage | None = None


@dataclass
class MetricDimension(PropertyType):
    comparison_operator: str | None = None
    value: float | None = None


@dataclass
class OverrideButtonConfiguration(PropertyType):
    button_action: str | None = None
    link: str | None = None


@dataclass
class QuietTime(PropertyType):
    end: str | None = None
    start: str | None = None


@dataclass
class Schedule(PropertyType):
    end_time: str | None = None
    event_filter: CampaignEventFilter | None = None
    frequency: str | None = None
    is_local_time: bool | None = None
    quiet_time: QuietTime | None = None
    start_time: str | None = None
    time_zone: str | None = None


@dataclass
class SetDimension(PropertyType):
    dimension_type: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class Template(PropertyType):
    name: str | None = None
    version: str | None = None


@dataclass
class TemplateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sms_template": "SMSTemplate",
    }

    email_template: Template | None = None
    push_template: Template | None = None
    sms_template: Template | None = None
    voice_template: Template | None = None


@dataclass
class WriteTreatmentResource(PropertyType):
    custom_delivery_configuration: CustomDeliveryConfiguration | None = None
    message_configuration: MessageConfiguration | None = None
    schedule: Schedule | None = None
    size_percent: int | None = None
    template_configuration: TemplateConfiguration | None = None
    treatment_description: str | None = None
    treatment_name: str | None = None
