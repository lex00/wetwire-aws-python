"""PropertyTypes for AWS::Connect::TaskTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Constraints(PropertyType):
    invisible_fields: list[DslValue[InvisibleFieldInfo]] = field(default_factory=list)
    read_only_fields: list[DslValue[ReadOnlyFieldInfo]] = field(default_factory=list)
    required_fields: list[DslValue[RequiredFieldInfo]] = field(default_factory=list)


@dataclass
class DefaultFieldValue(PropertyType):
    default_value: DslValue[str] | None = None
    id: DslValue[FieldIdentifier] | None = None


@dataclass
class Field(PropertyType):
    id: DslValue[FieldIdentifier] | None = None
    type_: DslValue[str] | None = None
    description: DslValue[str] | None = None
    single_select_options: list[DslValue[str]] = field(default_factory=list)


@dataclass
class FieldIdentifier(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class InvisibleFieldInfo(PropertyType):
    id: DslValue[FieldIdentifier] | None = None


@dataclass
class ReadOnlyFieldInfo(PropertyType):
    id: DslValue[FieldIdentifier] | None = None


@dataclass
class RequiredFieldInfo(PropertyType):
    id: DslValue[FieldIdentifier] | None = None
