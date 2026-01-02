"""PropertyTypes for AWS::IoT::ThingType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Mqtt5Configuration(PropertyType):
    propagating_attributes: list[PropagatingAttribute] = field(default_factory=list)


@dataclass
class PropagatingAttribute(PropertyType):
    user_property_key: str | None = None
    connection_attribute: str | None = None
    thing_attribute: str | None = None


@dataclass
class ThingTypeProperties(PropertyType):
    mqtt5_configuration: Mqtt5Configuration | None = None
    searchable_attributes: list[String] = field(default_factory=list)
    thing_type_description: str | None = None
