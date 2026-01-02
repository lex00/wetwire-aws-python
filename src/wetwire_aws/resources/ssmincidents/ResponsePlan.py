"""PropertyTypes for AWS::SSMIncidents::ResponsePlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    ssm_automation: SsmAutomation | None = None


@dataclass
class ChatChannel(PropertyType):
    chatbot_sns: list[String] = field(default_factory=list)


@dataclass
class DynamicSsmParameter(PropertyType):
    key: str | None = None
    value: DynamicSsmParameterValue | None = None


@dataclass
class DynamicSsmParameterValue(PropertyType):
    variable: str | None = None


@dataclass
class IncidentTemplate(PropertyType):
    impact: int | None = None
    title: str | None = None
    dedupe_string: str | None = None
    incident_tags: list[Tag] = field(default_factory=list)
    notification_targets: list[NotificationTargetItem] = field(default_factory=list)
    summary: str | None = None


@dataclass
class Integration(PropertyType):
    pager_duty_configuration: PagerDutyConfiguration | None = None


@dataclass
class NotificationTargetItem(PropertyType):
    sns_topic_arn: str | None = None


@dataclass
class PagerDutyConfiguration(PropertyType):
    name: str | None = None
    pager_duty_incident_configuration: PagerDutyIncidentConfiguration | None = None
    secret_id: str | None = None


@dataclass
class PagerDutyIncidentConfiguration(PropertyType):
    service_id: str | None = None


@dataclass
class SsmAutomation(PropertyType):
    document_name: str | None = None
    role_arn: str | None = None
    document_version: str | None = None
    dynamic_parameters: list[DynamicSsmParameter] = field(default_factory=list)
    parameters: list[SsmParameter] = field(default_factory=list)
    target_account: str | None = None


@dataclass
class SsmParameter(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)
