"""PropertyTypes for AWS::CustomerProfiles::ObjectType."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FieldMap(PropertyType):
    name: DslValue[str] | None = None
    object_type_field: DslValue[ObjectTypeField] | None = None


@dataclass
class KeyMap(PropertyType):
    name: DslValue[str] | None = None
    object_type_key_list: list[DslValue[ObjectTypeKey]] = field(default_factory=list)


@dataclass
class ObjectTypeField(PropertyType):
    content_type: DslValue[str] | None = None
    source: DslValue[str] | None = None
    target: DslValue[str] | None = None


@dataclass
class ObjectTypeKey(PropertyType):
    field_names: list[DslValue[str]] = field(default_factory=list)
    standard_identifiers: list[DslValue[str]] = field(default_factory=list)
