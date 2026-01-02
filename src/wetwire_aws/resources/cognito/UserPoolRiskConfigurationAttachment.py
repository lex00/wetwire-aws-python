"""PropertyTypes for AWS::Cognito::UserPoolRiskConfigurationAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccountTakeoverActionType(PropertyType):
    event_action: str | None = None
    notify: bool | None = None


@dataclass
class AccountTakeoverActionsType(PropertyType):
    high_action: AccountTakeoverActionType | None = None
    low_action: AccountTakeoverActionType | None = None
    medium_action: AccountTakeoverActionType | None = None


@dataclass
class AccountTakeoverRiskConfigurationType(PropertyType):
    actions: AccountTakeoverActionsType | None = None
    notify_configuration: NotifyConfigurationType | None = None


@dataclass
class CompromisedCredentialsActionsType(PropertyType):
    event_action: str | None = None


@dataclass
class CompromisedCredentialsRiskConfigurationType(PropertyType):
    actions: CompromisedCredentialsActionsType | None = None
    event_filter: list[String] = field(default_factory=list)


@dataclass
class NotifyConfigurationType(PropertyType):
    source_arn: str | None = None
    block_email: NotifyEmailType | None = None
    from_: str | None = None
    mfa_email: NotifyEmailType | None = None
    no_action_email: NotifyEmailType | None = None
    reply_to: str | None = None


@dataclass
class NotifyEmailType(PropertyType):
    subject: str | None = None
    html_body: str | None = None
    text_body: str | None = None


@dataclass
class RiskExceptionConfigurationType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "blocked_ip_range_list": "BlockedIPRangeList",
        "skipped_ip_range_list": "SkippedIPRangeList",
    }

    blocked_ip_range_list: list[String] = field(default_factory=list)
    skipped_ip_range_list: list[String] = field(default_factory=list)
