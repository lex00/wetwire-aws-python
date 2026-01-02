"""PropertyTypes for AWS::CustomerProfiles::ObjectType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FieldMap(PropertyType):
    name: str | None = None
    object_type_field: ObjectTypeField | None = None


@dataclass
class KeyMap(PropertyType):
    name: str | None = None
    object_type_key_list: list[ObjectTypeKey] = field(default_factory=list)


@dataclass
class ObjectTypeField(PropertyType):
    content_type: str | None = None
    source: str | None = None
    target: str | None = None


@dataclass
class ObjectTypeKey(PropertyType):
    field_names: list[String] = field(default_factory=list)
    standard_identifiers: list[String] = field(default_factory=list)
