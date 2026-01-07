"""PropertyTypes for AWS::Pinpoint::Campaign."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttributeDimension(PropertyType):
    attribute_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CampaignCustomMessage(PropertyType):
    data: DslValue[str] | None = None


@dataclass
class CampaignEmailMessage(PropertyType):
    body: DslValue[str] | None = None
    from_address: DslValue[str] | None = None
    html_body: DslValue[str] | None = None
    title: DslValue[str] | None = None


@dataclass
class CampaignEventFilter(PropertyType):
    dimensions: DslValue[EventDimensions] | None = None
    filter_type: DslValue[str] | None = None


@dataclass
class CampaignHook(PropertyType):
    lambda_function_name: DslValue[str] | None = None
    mode: DslValue[str] | None = None
    web_url: DslValue[str] | None = None


@dataclass
class CampaignInAppMessage(PropertyType):
    content: list[DslValue[InAppMessageContent]] = field(default_factory=list)
    custom_config: DslValue[dict[str, Any]] | None = None
    layout: DslValue[str] | None = None


@dataclass
class CampaignSmsMessage(PropertyType):
    body: DslValue[str] | None = None
    entity_id: DslValue[str] | None = None
    message_type: DslValue[str] | None = None
    origination_number: DslValue[str] | None = None
    sender_id: DslValue[str] | None = None
    template_id: DslValue[str] | None = None


@dataclass
class CustomDeliveryConfiguration(PropertyType):
    delivery_uri: DslValue[str] | None = None
    endpoint_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DefaultButtonConfiguration(PropertyType):
    background_color: DslValue[str] | None = None
    border_radius: DslValue[int] | None = None
    button_action: DslValue[str] | None = None
    link: DslValue[str] | None = None
    text: DslValue[str] | None = None
    text_color: DslValue[str] | None = None


@dataclass
class EventDimensions(PropertyType):
    attributes: DslValue[dict[str, Any]] | None = None
    event_type: DslValue[SetDimension] | None = None
    metrics: DslValue[dict[str, Any]] | None = None


@dataclass
class InAppMessageBodyConfig(PropertyType):
    alignment: DslValue[str] | None = None
    body: DslValue[str] | None = None
    text_color: DslValue[str] | None = None


@dataclass
class InAppMessageButton(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ios": "IOS",
    }

    android: DslValue[OverrideButtonConfiguration] | None = None
    default_config: DslValue[DefaultButtonConfiguration] | None = None
    ios: DslValue[OverrideButtonConfiguration] | None = None
    web: DslValue[OverrideButtonConfiguration] | None = None


@dataclass
class InAppMessageContent(PropertyType):
    background_color: DslValue[str] | None = None
    body_config: DslValue[InAppMessageBodyConfig] | None = None
    header_config: DslValue[InAppMessageHeaderConfig] | None = None
    image_url: DslValue[str] | None = None
    primary_btn: DslValue[InAppMessageButton] | None = None
    secondary_btn: DslValue[InAppMessageButton] | None = None


@dataclass
class InAppMessageHeaderConfig(PropertyType):
    alignment: DslValue[str] | None = None
    header: DslValue[str] | None = None
    text_color: DslValue[str] | None = None


@dataclass
class Limits(PropertyType):
    daily: DslValue[int] | None = None
    maximum_duration: DslValue[int] | None = None
    messages_per_second: DslValue[int] | None = None
    session: DslValue[int] | None = None
    total: DslValue[int] | None = None


@dataclass
class Message(PropertyType):
    action: DslValue[str] | None = None
    body: DslValue[str] | None = None
    image_icon_url: DslValue[str] | None = None
    image_small_icon_url: DslValue[str] | None = None
    image_url: DslValue[str] | None = None
    json_body: DslValue[str] | None = None
    media_url: DslValue[str] | None = None
    raw_content: DslValue[str] | None = None
    silent_push: DslValue[bool] | None = None
    time_to_live: DslValue[int] | None = None
    title: DslValue[str] | None = None
    url: DslValue[str] | None = None


@dataclass
class MessageConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "adm_message": "ADMMessage",
        "apns_message": "APNSMessage",
        "gcm_message": "GCMMessage",
        "sms_message": "SMSMessage",
    }

    adm_message: DslValue[Message] | None = None
    apns_message: DslValue[Message] | None = None
    baidu_message: DslValue[Message] | None = None
    custom_message: DslValue[CampaignCustomMessage] | None = None
    default_message: DslValue[Message] | None = None
    email_message: DslValue[CampaignEmailMessage] | None = None
    gcm_message: DslValue[Message] | None = None
    in_app_message: DslValue[CampaignInAppMessage] | None = None
    sms_message: DslValue[CampaignSmsMessage] | None = None


@dataclass
class MetricDimension(PropertyType):
    comparison_operator: DslValue[str] | None = None
    value: DslValue[float] | None = None


@dataclass
class OverrideButtonConfiguration(PropertyType):
    button_action: DslValue[str] | None = None
    link: DslValue[str] | None = None


@dataclass
class QuietTime(PropertyType):
    end: DslValue[str] | None = None
    start: DslValue[str] | None = None


@dataclass
class Schedule(PropertyType):
    end_time: DslValue[str] | None = None
    event_filter: DslValue[CampaignEventFilter] | None = None
    frequency: DslValue[str] | None = None
    is_local_time: DslValue[bool] | None = None
    quiet_time: DslValue[QuietTime] | None = None
    start_time: DslValue[str] | None = None
    time_zone: DslValue[str] | None = None


@dataclass
class SetDimension(PropertyType):
    dimension_type: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Template(PropertyType):
    name: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class TemplateConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sms_template": "SMSTemplate",
    }

    email_template: DslValue[Template] | None = None
    push_template: DslValue[Template] | None = None
    sms_template: DslValue[Template] | None = None
    voice_template: DslValue[Template] | None = None


@dataclass
class WriteTreatmentResource(PropertyType):
    custom_delivery_configuration: DslValue[CustomDeliveryConfiguration] | None = None
    message_configuration: DslValue[MessageConfiguration] | None = None
    schedule: DslValue[Schedule] | None = None
    size_percent: DslValue[int] | None = None
    template_configuration: DslValue[TemplateConfiguration] | None = None
    treatment_description: DslValue[str] | None = None
    treatment_name: DslValue[str] | None = None
