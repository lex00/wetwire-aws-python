"""PropertyTypes for AWS::Cases::Template."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LayoutConfiguration(PropertyType):
    default_layout: DslValue[str] | None = None


@dataclass
class RequiredField(PropertyType):
    field_id: DslValue[str] | None = None


@dataclass
class TemplateRule(PropertyType):
    case_rule_id: DslValue[str] | None = None
    field_id: DslValue[str] | None = None
