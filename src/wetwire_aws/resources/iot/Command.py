"""PropertyTypes for AWS::IoT::Command."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CommandParameter(PropertyType):
    name: DslValue[str] | None = None
    default_value: DslValue[CommandParameterValue] | None = None
    description: DslValue[str] | None = None
    value: DslValue[CommandParameterValue] | None = None


@dataclass
class CommandParameterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bin": "BIN",
        "ul": "UL",
    }

    b: DslValue[bool] | None = None
    bin: DslValue[str] | None = None
    d: DslValue[float] | None = None
    i: DslValue[int] | None = None
    l: DslValue[str] | None = None
    s: DslValue[str] | None = None
    ul: DslValue[str] | None = None


@dataclass
class CommandPayload(PropertyType):
    content: DslValue[str] | None = None
    content_type: DslValue[str] | None = None
