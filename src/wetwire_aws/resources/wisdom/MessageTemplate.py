"""PropertyTypes for AWS::Wisdom::MessageTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AgentAttributes(PropertyType):
    first_name: DslValue[str] | None = None
    last_name: DslValue[str] | None = None


@dataclass
class Content(PropertyType):
    email_message_template_content: DslValue[EmailMessageTemplateContent] | None = None
    sms_message_template_content: DslValue[SmsMessageTemplateContent] | None = None


@dataclass
class CustomerProfileAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "profile_arn": "ProfileARN",
    }

    account_number: DslValue[str] | None = None
    additional_information: DslValue[str] | None = None
    address1: DslValue[str] | None = None
    address2: DslValue[str] | None = None
    address3: DslValue[str] | None = None
    address4: DslValue[str] | None = None
    billing_address1: DslValue[str] | None = None
    billing_address2: DslValue[str] | None = None
    billing_address3: DslValue[str] | None = None
    billing_address4: DslValue[str] | None = None
    billing_city: DslValue[str] | None = None
    billing_country: DslValue[str] | None = None
    billing_county: DslValue[str] | None = None
    billing_postal_code: DslValue[str] | None = None
    billing_province: DslValue[str] | None = None
    billing_state: DslValue[str] | None = None
    birth_date: DslValue[str] | None = None
    business_email_address: DslValue[str] | None = None
    business_name: DslValue[str] | None = None
    business_phone_number: DslValue[str] | None = None
    city: DslValue[str] | None = None
    country: DslValue[str] | None = None
    county: DslValue[str] | None = None
    custom: dict[str, DslValue[str]] = field(default_factory=dict)
    email_address: DslValue[str] | None = None
    first_name: DslValue[str] | None = None
    gender: DslValue[str] | None = None
    home_phone_number: DslValue[str] | None = None
    last_name: DslValue[str] | None = None
    mailing_address1: DslValue[str] | None = None
    mailing_address2: DslValue[str] | None = None
    mailing_address3: DslValue[str] | None = None
    mailing_address4: DslValue[str] | None = None
    mailing_city: DslValue[str] | None = None
    mailing_country: DslValue[str] | None = None
    mailing_county: DslValue[str] | None = None
    mailing_postal_code: DslValue[str] | None = None
    mailing_province: DslValue[str] | None = None
    mailing_state: DslValue[str] | None = None
    middle_name: DslValue[str] | None = None
    mobile_phone_number: DslValue[str] | None = None
    party_type: DslValue[str] | None = None
    phone_number: DslValue[str] | None = None
    postal_code: DslValue[str] | None = None
    profile_arn: DslValue[str] | None = None
    profile_id: DslValue[str] | None = None
    province: DslValue[str] | None = None
    shipping_address1: DslValue[str] | None = None
    shipping_address2: DslValue[str] | None = None
    shipping_address3: DslValue[str] | None = None
    shipping_address4: DslValue[str] | None = None
    shipping_city: DslValue[str] | None = None
    shipping_country: DslValue[str] | None = None
    shipping_county: DslValue[str] | None = None
    shipping_postal_code: DslValue[str] | None = None
    shipping_province: DslValue[str] | None = None
    shipping_state: DslValue[str] | None = None
    state: DslValue[str] | None = None


@dataclass
class EmailMessageTemplateContent(PropertyType):
    body: DslValue[EmailMessageTemplateContentBody] | None = None
    headers: list[DslValue[EmailMessageTemplateHeader]] = field(default_factory=list)
    subject: DslValue[str] | None = None


@dataclass
class EmailMessageTemplateContentBody(PropertyType):
    html: DslValue[MessageTemplateBodyContentProvider] | None = None
    plain_text: DslValue[MessageTemplateBodyContentProvider] | None = None


@dataclass
class EmailMessageTemplateHeader(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class GroupingConfiguration(PropertyType):
    criteria: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class MessageTemplateAttachment(PropertyType):
    attachment_name: DslValue[str] | None = None
    s3_presigned_url: DslValue[str] | None = None
    attachment_id: DslValue[str] | None = None


@dataclass
class MessageTemplateAttributes(PropertyType):
    agent_attributes: DslValue[AgentAttributes] | None = None
    custom_attributes: dict[str, DslValue[str]] = field(default_factory=dict)
    customer_profile_attributes: DslValue[CustomerProfileAttributes] | None = None
    system_attributes: DslValue[SystemAttributes] | None = None


@dataclass
class MessageTemplateBodyContentProvider(PropertyType):
    content: DslValue[str] | None = None


@dataclass
class SmsMessageTemplateContent(PropertyType):
    body: DslValue[SmsMessageTemplateContentBody] | None = None


@dataclass
class SmsMessageTemplateContentBody(PropertyType):
    plain_text: DslValue[MessageTemplateBodyContentProvider] | None = None


@dataclass
class SystemAttributes(PropertyType):
    customer_endpoint: DslValue[SystemEndpointAttributes] | None = None
    name: DslValue[str] | None = None
    system_endpoint: DslValue[SystemEndpointAttributes] | None = None


@dataclass
class SystemEndpointAttributes(PropertyType):
    address: DslValue[str] | None = None
