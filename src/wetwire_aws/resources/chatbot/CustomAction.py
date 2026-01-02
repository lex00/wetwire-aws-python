"""PropertyTypes for AWS::Chatbot::CustomAction."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CustomActionAttachment(PropertyType):
    button_text: str | None = None
    criteria: list[CustomActionAttachmentCriteria] = field(default_factory=list)
    notification_type: str | None = None
    variables: dict[str, String] = field(default_factory=dict)


@dataclass
class CustomActionAttachmentCriteria(PropertyType):
    operator: str | None = None
    variable_name: str | None = None
    value: str | None = None


@dataclass
class CustomActionDefinition(PropertyType):
    command_text: str | None = None
