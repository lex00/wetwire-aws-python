"""PropertyTypes for AWS::Cognito::UserPool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccountRecoverySetting(PropertyType):
    recovery_mechanisms: list[DslValue[RecoveryOption]] = field(default_factory=list)


@dataclass
class AdminCreateUserConfig(PropertyType):
    allow_admin_create_user_only: DslValue[bool] | None = None
    invite_message_template: DslValue[InviteMessageTemplate] | None = None
    unused_account_validity_days: DslValue[int] | None = None


@dataclass
class AdvancedSecurityAdditionalFlows(PropertyType):
    custom_auth_mode: DslValue[str] | None = None


@dataclass
class CustomEmailSender(PropertyType):
    lambda_arn: DslValue[str] | None = None
    lambda_version: DslValue[str] | None = None


@dataclass
class CustomSMSSender(PropertyType):
    lambda_arn: DslValue[str] | None = None
    lambda_version: DslValue[str] | None = None


@dataclass
class DeviceConfiguration(PropertyType):
    challenge_required_on_new_device: DslValue[bool] | None = None
    device_only_remembered_on_user_prompt: DslValue[bool] | None = None


@dataclass
class EmailConfiguration(PropertyType):
    configuration_set: DslValue[str] | None = None
    email_sending_account: DslValue[str] | None = None
    from_: DslValue[str] | None = None
    reply_to_email_address: DslValue[str] | None = None
    source_arn: DslValue[str] | None = None


@dataclass
class InviteMessageTemplate(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sms_message": "SMSMessage",
    }

    email_message: DslValue[str] | None = None
    email_subject: DslValue[str] | None = None
    sms_message: DslValue[str] | None = None


@dataclass
class LambdaConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "custom_sms_sender": "CustomSMSSender",
        "kms_key_id": "KMSKeyID",
    }

    create_auth_challenge: DslValue[str] | None = None
    custom_email_sender: DslValue[CustomEmailSender] | None = None
    custom_message: DslValue[str] | None = None
    custom_sms_sender: DslValue[CustomSMSSender] | None = None
    define_auth_challenge: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
    post_authentication: DslValue[str] | None = None
    post_confirmation: DslValue[str] | None = None
    pre_authentication: DslValue[str] | None = None
    pre_sign_up: DslValue[str] | None = None
    pre_token_generation: DslValue[str] | None = None
    pre_token_generation_config: DslValue[PreTokenGenerationConfig] | None = None
    user_migration: DslValue[str] | None = None
    verify_auth_challenge_response: DslValue[str] | None = None


@dataclass
class NumberAttributeConstraints(PropertyType):
    max_value: DslValue[str] | None = None
    min_value: DslValue[str] | None = None


@dataclass
class PasswordPolicy(PropertyType):
    minimum_length: DslValue[int] | None = None
    password_history_size: DslValue[int] | None = None
    require_lowercase: DslValue[bool] | None = None
    require_numbers: DslValue[bool] | None = None
    require_symbols: DslValue[bool] | None = None
    require_uppercase: DslValue[bool] | None = None
    temporary_password_validity_days: DslValue[int] | None = None


@dataclass
class Policies(PropertyType):
    password_policy: DslValue[PasswordPolicy] | None = None
    sign_in_policy: DslValue[SignInPolicy] | None = None


@dataclass
class PreTokenGenerationConfig(PropertyType):
    lambda_arn: DslValue[str] | None = None
    lambda_version: DslValue[str] | None = None


@dataclass
class RecoveryOption(PropertyType):
    name: DslValue[str] | None = None
    priority: DslValue[int] | None = None


@dataclass
class SchemaAttribute(PropertyType):
    attribute_data_type: DslValue[str] | None = None
    developer_only_attribute: DslValue[bool] | None = None
    mutable: DslValue[bool] | None = None
    name: DslValue[str] | None = None
    number_attribute_constraints: DslValue[NumberAttributeConstraints] | None = None
    required: DslValue[bool] | None = None
    string_attribute_constraints: DslValue[StringAttributeConstraints] | None = None


@dataclass
class SignInPolicy(PropertyType):
    allowed_first_auth_factors: list[DslValue[str]] = field(default_factory=list)


@dataclass
class SmsConfiguration(PropertyType):
    external_id: DslValue[str] | None = None
    sns_caller_arn: DslValue[str] | None = None
    sns_region: DslValue[str] | None = None


@dataclass
class StringAttributeConstraints(PropertyType):
    max_length: DslValue[str] | None = None
    min_length: DslValue[str] | None = None


@dataclass
class UserAttributeUpdateSettings(PropertyType):
    attributes_require_verification_before_update: list[DslValue[str]] = field(
        default_factory=list
    )


@dataclass
class UserPoolAddOns(PropertyType):
    advanced_security_additional_flows: (
        DslValue[AdvancedSecurityAdditionalFlows] | None
    ) = None
    advanced_security_mode: DslValue[str] | None = None


@dataclass
class UsernameConfiguration(PropertyType):
    case_sensitive: DslValue[bool] | None = None


@dataclass
class VerificationMessageTemplate(PropertyType):
    default_email_option: DslValue[str] | None = None
    email_message: DslValue[str] | None = None
    email_message_by_link: DslValue[str] | None = None
    email_subject: DslValue[str] | None = None
    email_subject_by_link: DslValue[str] | None = None
    sms_message: DslValue[str] | None = None
