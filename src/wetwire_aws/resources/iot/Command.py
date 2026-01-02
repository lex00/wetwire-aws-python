"""PropertyTypes for AWS::IoT::Command."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CommandParameter(PropertyType):
    name: str | None = None
    default_value: CommandParameterValue | None = None
    description: str | None = None
    value: CommandParameterValue | None = None


@dataclass
class CommandParameterValue(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bin": "BIN",
        "ul": "UL",
    }

    b: bool | None = None
    bin: str | None = None
    d: float | None = None
    i: int | None = None
    l: str | None = None
    s: str | None = None
    ul: str | None = None


@dataclass
class CommandPayload(PropertyType):
    content: str | None = None
    content_type: str | None = None
