"""PropertyTypes for AWS::Cases::Layout."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BasicLayout(PropertyType):
    more_info: DslValue[LayoutSections] | None = None
    top_panel: DslValue[LayoutSections] | None = None


@dataclass
class FieldGroup(PropertyType):
    fields: list[DslValue[FieldItem]] = field(default_factory=list)
    name: DslValue[str] | None = None


@dataclass
class FieldItem(PropertyType):
    id: DslValue[str] | None = None


@dataclass
class LayoutContent(PropertyType):
    basic: DslValue[BasicLayout] | None = None


@dataclass
class LayoutSections(PropertyType):
    sections: list[DslValue[Section]] = field(default_factory=list)


@dataclass
class Section(PropertyType):
    field_group: DslValue[FieldGroup] | None = None
