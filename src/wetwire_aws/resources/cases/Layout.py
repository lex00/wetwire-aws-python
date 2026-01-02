"""PropertyTypes for AWS::Cases::Layout."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BasicLayout(PropertyType):
    more_info: LayoutSections | None = None
    top_panel: LayoutSections | None = None


@dataclass
class FieldGroup(PropertyType):
    fields: list[FieldItem] = field(default_factory=list)
    name: str | None = None


@dataclass
class FieldItem(PropertyType):
    id: str | None = None


@dataclass
class LayoutContent(PropertyType):
    basic: BasicLayout | None = None


@dataclass
class LayoutSections(PropertyType):
    sections: list[Section] = field(default_factory=list)


@dataclass
class Section(PropertyType):
    field_group: FieldGroup | None = None
