"""PropertyTypes for AWS::IoT::ThingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributePayload(PropertyType):
    attributes: dict[str, String] = field(default_factory=dict)


@dataclass
class ThingGroupProperties(PropertyType):
    attribute_payload: AttributePayload | None = None
    thing_group_description: str | None = None
