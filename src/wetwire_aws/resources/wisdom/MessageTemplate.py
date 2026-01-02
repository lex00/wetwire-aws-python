"""PropertyTypes for AWS::Wisdom::MessageTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AgentAttributes(PropertyType):
    first_name: str | None = None
    last_name: str | None = None


@dataclass
class Content(PropertyType):
    email_message_template_content: EmailMessageTemplateContent | None = None
    sms_message_template_content: SmsMessageTemplateContent | None = None


@dataclass
class CustomerProfileAttributes(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "profile_arn": "ProfileARN",
    }

    account_number: str | None = None
    additional_information: str | None = None
    address1: str | None = None
    address2: str | None = None
    address3: str | None = None
    address4: str | None = None
    billing_address1: str | None = None
    billing_address2: str | None = None
    billing_address3: str | None = None
    billing_address4: str | None = None
    billing_city: str | None = None
    billing_country: str | None = None
    billing_county: str | None = None
    billing_postal_code: str | None = None
    billing_province: str | None = None
    billing_state: str | None = None
    birth_date: str | None = None
    business_email_address: str | None = None
    business_name: str | None = None
    business_phone_number: str | None = None
    city: str | None = None
    country: str | None = None
    county: str | None = None
    custom: dict[str, String] = field(default_factory=dict)
    email_address: str | None = None
    first_name: str | None = None
    gender: str | None = None
    home_phone_number: str | None = None
    last_name: str | None = None
    mailing_address1: str | None = None
    mailing_address2: str | None = None
    mailing_address3: str | None = None
    mailing_address4: str | None = None
    mailing_city: str | None = None
    mailing_country: str | None = None
    mailing_county: str | None = None
    mailing_postal_code: str | None = None
    mailing_province: str | None = None
    mailing_state: str | None = None
    middle_name: str | None = None
    mobile_phone_number: str | None = None
    party_type: str | None = None
    phone_number: str | None = None
    postal_code: str | None = None
    profile_arn: str | None = None
    profile_id: str | None = None
    province: str | None = None
    shipping_address1: str | None = None
    shipping_address2: str | None = None
    shipping_address3: str | None = None
    shipping_address4: str | None = None
    shipping_city: str | None = None
    shipping_country: str | None = None
    shipping_county: str | None = None
    shipping_postal_code: str | None = None
    shipping_province: str | None = None
    shipping_state: str | None = None
    state: str | None = None


@dataclass
class EmailMessageTemplateContent(PropertyType):
    body: EmailMessageTemplateContentBody | None = None
    headers: list[EmailMessageTemplateHeader] = field(default_factory=list)
    subject: str | None = None


@dataclass
class EmailMessageTemplateContentBody(PropertyType):
    html: MessageTemplateBodyContentProvider | None = None
    plain_text: MessageTemplateBodyContentProvider | None = None


@dataclass
class EmailMessageTemplateHeader(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class GroupingConfiguration(PropertyType):
    criteria: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class MessageTemplateAttachment(PropertyType):
    attachment_name: str | None = None
    s3_presigned_url: str | None = None
    attachment_id: str | None = None


@dataclass
class MessageTemplateAttributes(PropertyType):
    agent_attributes: AgentAttributes | None = None
    custom_attributes: dict[str, String] = field(default_factory=dict)
    customer_profile_attributes: CustomerProfileAttributes | None = None
    system_attributes: SystemAttributes | None = None


@dataclass
class MessageTemplateBodyContentProvider(PropertyType):
    content: str | None = None


@dataclass
class SmsMessageTemplateContent(PropertyType):
    body: SmsMessageTemplateContentBody | None = None


@dataclass
class SmsMessageTemplateContentBody(PropertyType):
    plain_text: MessageTemplateBodyContentProvider | None = None


@dataclass
class SystemAttributes(PropertyType):
    customer_endpoint: SystemEndpointAttributes | None = None
    name: str | None = None
    system_endpoint: SystemEndpointAttributes | None = None


@dataclass
class SystemEndpointAttributes(PropertyType):
    address: str | None = None
