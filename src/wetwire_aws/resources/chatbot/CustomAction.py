"""PropertyTypes for AWS::Chatbot::CustomAction."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CustomActionAttachment(PropertyType):
    button_text: DslValue[str] | None = None
    criteria: list[DslValue[CustomActionAttachmentCriteria]] = field(
        default_factory=list
    )
    notification_type: DslValue[str] | None = None
    variables: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class CustomActionAttachmentCriteria(PropertyType):
    operator: DslValue[str] | None = None
    variable_name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class CustomActionDefinition(PropertyType):
    command_text: DslValue[str] | None = None
