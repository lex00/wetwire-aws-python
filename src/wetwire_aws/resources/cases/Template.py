"""PropertyTypes for AWS::Cases::Template."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LayoutConfiguration(PropertyType):
    default_layout: str | None = None


@dataclass
class RequiredField(PropertyType):
    field_id: str | None = None


@dataclass
class TemplateRule(PropertyType):
    case_rule_id: str | None = None
    field_id: str | None = None
