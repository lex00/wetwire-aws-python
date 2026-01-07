"""PropertyTypes for AWS::IoT::ThingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttributePayload(PropertyType):
    attributes: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class ThingGroupProperties(PropertyType):
    attribute_payload: DslValue[AttributePayload] | None = None
    thing_group_description: DslValue[str] | None = None
