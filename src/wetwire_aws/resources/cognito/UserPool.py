"""PropertyTypes for AWS::Cognito::UserPool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccountRecoverySetting(PropertyType):
    recovery_mechanisms: list[RecoveryOption] = field(default_factory=list)


@dataclass
class AdminCreateUserConfig(PropertyType):
    allow_admin_create_user_only: bool | None = None
    invite_message_template: InviteMessageTemplate | None = None
    unused_account_validity_days: int | None = None


@dataclass
class AdvancedSecurityAdditionalFlows(PropertyType):
    custom_auth_mode: str | None = None


@dataclass
class CustomEmailSender(PropertyType):
    lambda_arn: str | None = None
    lambda_version: str | None = None


@dataclass
class CustomSMSSender(PropertyType):
    lambda_arn: str | None = None
    lambda_version: str | None = None


@dataclass
class DeviceConfiguration(PropertyType):
    challenge_required_on_new_device: bool | None = None
    device_only_remembered_on_user_prompt: bool | None = None


@dataclass
class EmailConfiguration(PropertyType):
    configuration_set: str | None = None
    email_sending_account: str | None = None
    from_: str | None = None
    reply_to_email_address: str | None = None
    source_arn: str | None = None


@dataclass
class InviteMessageTemplate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sms_message": "SMSMessage",
    }

    email_message: str | None = None
    email_subject: str | None = None
    sms_message: str | None = None


@dataclass
class LambdaConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_sms_sender": "CustomSMSSender",
        "kms_key_id": "KMSKeyID",
    }

    create_auth_challenge: str | None = None
    custom_email_sender: CustomEmailSender | None = None
    custom_message: str | None = None
    custom_sms_sender: CustomSMSSender | None = None
    define_auth_challenge: str | None = None
    kms_key_id: str | None = None
    post_authentication: str | None = None
    post_confirmation: str | None = None
    pre_authentication: str | None = None
    pre_sign_up: str | None = None
    pre_token_generation: str | None = None
    pre_token_generation_config: PreTokenGenerationConfig | None = None
    user_migration: str | None = None
    verify_auth_challenge_response: str | None = None


@dataclass
class NumberAttributeConstraints(PropertyType):
    max_value: str | None = None
    min_value: str | None = None


@dataclass
class PasswordPolicy(PropertyType):
    minimum_length: int | None = None
    password_history_size: int | None = None
    require_lowercase: bool | None = None
    require_numbers: bool | None = None
    require_symbols: bool | None = None
    require_uppercase: bool | None = None
    temporary_password_validity_days: int | None = None


@dataclass
class Policies(PropertyType):
    password_policy: PasswordPolicy | None = None
    sign_in_policy: SignInPolicy | None = None


@dataclass
class PreTokenGenerationConfig(PropertyType):
    lambda_arn: str | None = None
    lambda_version: str | None = None


@dataclass
class RecoveryOption(PropertyType):
    name: str | None = None
    priority: int | None = None


@dataclass
class SchemaAttribute(PropertyType):
    attribute_data_type: str | None = None
    developer_only_attribute: bool | None = None
    mutable: bool | None = None
    name: str | None = None
    number_attribute_constraints: NumberAttributeConstraints | None = None
    required: bool | None = None
    string_attribute_constraints: StringAttributeConstraints | None = None


@dataclass
class SignInPolicy(PropertyType):
    allowed_first_auth_factors: list[String] = field(default_factory=list)


@dataclass
class SmsConfiguration(PropertyType):
    external_id: str | None = None
    sns_caller_arn: str | None = None
    sns_region: str | None = None


@dataclass
class StringAttributeConstraints(PropertyType):
    max_length: str | None = None
    min_length: str | None = None


@dataclass
class UserAttributeUpdateSettings(PropertyType):
    attributes_require_verification_before_update: list[String] = field(
        default_factory=list
    )


@dataclass
class UserPoolAddOns(PropertyType):
    advanced_security_additional_flows: AdvancedSecurityAdditionalFlows | None = None
    advanced_security_mode: str | None = None


@dataclass
class UsernameConfiguration(PropertyType):
    case_sensitive: bool | None = None


@dataclass
class VerificationMessageTemplate(PropertyType):
    default_email_option: str | None = None
    email_message: str | None = None
    email_message_by_link: str | None = None
    email_subject: str | None = None
    email_subject_by_link: str | None = None
    sms_message: str | None = None
