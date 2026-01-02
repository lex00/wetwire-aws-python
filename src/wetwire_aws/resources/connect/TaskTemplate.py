"""PropertyTypes for AWS::Connect::TaskTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Constraints(PropertyType):
    invisible_fields: list[InvisibleFieldInfo] = field(default_factory=list)
    read_only_fields: list[ReadOnlyFieldInfo] = field(default_factory=list)
    required_fields: list[RequiredFieldInfo] = field(default_factory=list)


@dataclass
class DefaultFieldValue(PropertyType):
    default_value: str | None = None
    id: FieldIdentifier | None = None


@dataclass
class Field(PropertyType):
    id: FieldIdentifier | None = None
    type_: str | None = None
    description: str | None = None
    single_select_options: list[String] = field(default_factory=list)


@dataclass
class FieldIdentifier(PropertyType):
    name: str | None = None


@dataclass
class InvisibleFieldInfo(PropertyType):
    id: FieldIdentifier | None = None


@dataclass
class ReadOnlyFieldInfo(PropertyType):
    id: FieldIdentifier | None = None


@dataclass
class RequiredFieldInfo(PropertyType):
    id: FieldIdentifier | None = None
