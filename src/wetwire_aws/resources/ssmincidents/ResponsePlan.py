"""PropertyTypes for AWS::SSMIncidents::ResponsePlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    ssm_automation: DslValue[SsmAutomation] | None = None


@dataclass
class ChatChannel(PropertyType):
    chatbot_sns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DynamicSsmParameter(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[DynamicSsmParameterValue] | None = None


@dataclass
class DynamicSsmParameterValue(PropertyType):
    variable: DslValue[str] | None = None


@dataclass
class IncidentTemplate(PropertyType):
    impact: DslValue[int] | None = None
    title: DslValue[str] | None = None
    dedupe_string: DslValue[str] | None = None
    incident_tags: list[DslValue[Tag]] = field(default_factory=list)
    notification_targets: list[DslValue[NotificationTargetItem]] = field(
        default_factory=list
    )
    summary: DslValue[str] | None = None


@dataclass
class Integration(PropertyType):
    pager_duty_configuration: DslValue[PagerDutyConfiguration] | None = None


@dataclass
class NotificationTargetItem(PropertyType):
    sns_topic_arn: DslValue[str] | None = None


@dataclass
class PagerDutyConfiguration(PropertyType):
    name: DslValue[str] | None = None
    pager_duty_incident_configuration: (
        DslValue[PagerDutyIncidentConfiguration] | None
    ) = None
    secret_id: DslValue[str] | None = None


@dataclass
class PagerDutyIncidentConfiguration(PropertyType):
    service_id: DslValue[str] | None = None


@dataclass
class SsmAutomation(PropertyType):
    document_name: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    document_version: DslValue[str] | None = None
    dynamic_parameters: list[DslValue[DynamicSsmParameter]] = field(
        default_factory=list
    )
    parameters: list[DslValue[SsmParameter]] = field(default_factory=list)
    target_account: DslValue[str] | None = None


@dataclass
class SsmParameter(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)
