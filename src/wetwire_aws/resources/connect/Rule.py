"""PropertyTypes for AWS::Connect::Rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Actions(PropertyType):
    assign_contact_category_actions: list[DslValue[dict[str, Any]]] = field(
        default_factory=list
    )
    create_case_actions: list[DslValue[CreateCaseAction]] = field(default_factory=list)
    end_associated_tasks_actions: list[DslValue[dict[str, Any]]] = field(
        default_factory=list
    )
    event_bridge_actions: list[DslValue[EventBridgeAction]] = field(
        default_factory=list
    )
    send_notification_actions: list[DslValue[SendNotificationAction]] = field(
        default_factory=list
    )
    submit_auto_evaluation_actions: list[DslValue[SubmitAutoEvaluationAction]] = field(
        default_factory=list
    )
    task_actions: list[DslValue[TaskAction]] = field(default_factory=list)
    update_case_actions: list[DslValue[UpdateCaseAction]] = field(default_factory=list)


@dataclass
class CreateCaseAction(PropertyType):
    fields: list[DslValue[Field]] = field(default_factory=list)
    template_id: DslValue[str] | None = None


@dataclass
class EventBridgeAction(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class Field(PropertyType):
    id: DslValue[str] | None = None
    value: DslValue[FieldValue] | None = None


@dataclass
class FieldValue(PropertyType):
    boolean_value: DslValue[bool] | None = None
    double_value: DslValue[float] | None = None
    empty_value: DslValue[dict[str, Any]] | None = None
    string_value: DslValue[str] | None = None


@dataclass
class NotificationRecipientType(PropertyType):
    user_arns: list[DslValue[str]] = field(default_factory=list)
    user_tags: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class Reference(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class RuleTriggerEventSource(PropertyType):
    event_source_name: DslValue[str] | None = None
    integration_association_arn: DslValue[str] | None = None


@dataclass
class SendNotificationAction(PropertyType):
    content: DslValue[str] | None = None
    content_type: DslValue[str] | None = None
    delivery_method: DslValue[str] | None = None
    recipient: DslValue[NotificationRecipientType] | None = None
    subject: DslValue[str] | None = None


@dataclass
class SubmitAutoEvaluationAction(PropertyType):
    evaluation_form_arn: DslValue[str] | None = None


@dataclass
class TaskAction(PropertyType):
    contact_flow_arn: DslValue[str] | None = None
    name: DslValue[str] | None = None
    description: DslValue[str] | None = None
    references: dict[str, DslValue[Reference]] = field(default_factory=dict)


@dataclass
class UpdateCaseAction(PropertyType):
    fields: list[DslValue[Field]] = field(default_factory=list)
