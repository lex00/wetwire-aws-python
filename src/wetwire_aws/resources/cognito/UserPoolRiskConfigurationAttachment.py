"""PropertyTypes for AWS::Cognito::UserPoolRiskConfigurationAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccountTakeoverActionType(PropertyType):
    event_action: DslValue[str] | None = None
    notify: DslValue[bool] | None = None


@dataclass
class AccountTakeoverActionsType(PropertyType):
    high_action: DslValue[AccountTakeoverActionType] | None = None
    low_action: DslValue[AccountTakeoverActionType] | None = None
    medium_action: DslValue[AccountTakeoverActionType] | None = None


@dataclass
class AccountTakeoverRiskConfigurationType(PropertyType):
    actions: DslValue[AccountTakeoverActionsType] | None = None
    notify_configuration: DslValue[NotifyConfigurationType] | None = None


@dataclass
class CompromisedCredentialsActionsType(PropertyType):
    event_action: DslValue[str] | None = None


@dataclass
class CompromisedCredentialsRiskConfigurationType(PropertyType):
    actions: DslValue[CompromisedCredentialsActionsType] | None = None
    event_filter: list[DslValue[str]] = field(default_factory=list)


@dataclass
class NotifyConfigurationType(PropertyType):
    source_arn: DslValue[str] | None = None
    block_email: DslValue[NotifyEmailType] | None = None
    from_: DslValue[str] | None = None
    mfa_email: DslValue[NotifyEmailType] | None = None
    no_action_email: DslValue[NotifyEmailType] | None = None
    reply_to: DslValue[str] | None = None


@dataclass
class NotifyEmailType(PropertyType):
    subject: DslValue[str] | None = None
    html_body: DslValue[str] | None = None
    text_body: DslValue[str] | None = None


@dataclass
class RiskExceptionConfigurationType(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "blocked_ip_range_list": "BlockedIPRangeList",
        "skipped_ip_range_list": "SkippedIPRangeList",
    }

    blocked_ip_range_list: list[DslValue[str]] = field(default_factory=list)
    skipped_ip_range_list: list[DslValue[str]] = field(default_factory=list)
