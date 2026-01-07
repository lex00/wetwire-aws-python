"""PropertyTypes for AWS::IoT::ThingType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Mqtt5Configuration(PropertyType):
    propagating_attributes: list[DslValue[PropagatingAttribute]] = field(
        default_factory=list
    )


@dataclass
class PropagatingAttribute(PropertyType):
    user_property_key: DslValue[str] | None = None
    connection_attribute: DslValue[str] | None = None
    thing_attribute: DslValue[str] | None = None


@dataclass
class ThingTypeProperties(PropertyType):
    mqtt5_configuration: DslValue[Mqtt5Configuration] | None = None
    searchable_attributes: list[DslValue[str]] = field(default_factory=list)
    thing_type_description: DslValue[str] | None = None
