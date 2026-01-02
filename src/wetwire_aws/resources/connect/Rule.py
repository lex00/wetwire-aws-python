"""PropertyTypes for AWS::Connect::Rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Actions(PropertyType):
    assign_contact_category_actions: list[Json] = field(default_factory=list)
    create_case_actions: list[CreateCaseAction] = field(default_factory=list)
    end_associated_tasks_actions: list[Json] = field(default_factory=list)
    event_bridge_actions: list[EventBridgeAction] = field(default_factory=list)
    send_notification_actions: list[SendNotificationAction] = field(
        default_factory=list
    )
    submit_auto_evaluation_actions: list[SubmitAutoEvaluationAction] = field(
        default_factory=list
    )
    task_actions: list[TaskAction] = field(default_factory=list)
    update_case_actions: list[UpdateCaseAction] = field(default_factory=list)


@dataclass
class CreateCaseAction(PropertyType):
    fields: list[Field] = field(default_factory=list)
    template_id: str | None = None


@dataclass
class EventBridgeAction(PropertyType):
    name: str | None = None


@dataclass
class Field(PropertyType):
    id: str | None = None
    value: FieldValue | None = None


@dataclass
class FieldValue(PropertyType):
    boolean_value: bool | None = None
    double_value: float | None = None
    empty_value: dict[str, Any] | None = None
    string_value: str | None = None


@dataclass
class NotificationRecipientType(PropertyType):
    user_arns: list[String] = field(default_factory=list)
    user_tags: dict[str, String] = field(default_factory=dict)


@dataclass
class Reference(PropertyType):
    type_: str | None = None
    value: str | None = None


@dataclass
class RuleTriggerEventSource(PropertyType):
    event_source_name: str | None = None
    integration_association_arn: str | None = None


@dataclass
class SendNotificationAction(PropertyType):
    content: str | None = None
    content_type: str | None = None
    delivery_method: str | None = None
    recipient: NotificationRecipientType | None = None
    subject: str | None = None


@dataclass
class SubmitAutoEvaluationAction(PropertyType):
    evaluation_form_arn: str | None = None


@dataclass
class TaskAction(PropertyType):
    contact_flow_arn: str | None = None
    name: str | None = None
    description: str | None = None
    references: dict[str, Reference] = field(default_factory=dict)


@dataclass
class UpdateCaseAction(PropertyType):
    fields: list[Field] = field(default_factory=list)
