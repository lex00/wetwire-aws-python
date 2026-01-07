"""PropertyTypes for AWS::WAFRegional::SizeConstraintSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FieldToMatch(PropertyType):
    type_: DslValue[str] | None = None
    data: DslValue[str] | None = None


@dataclass
class SizeConstraint(PropertyType):
    comparison_operator: DslValue[str] | None = None
    field_to_match: DslValue[FieldToMatch] | None = None
    size: DslValue[int] | None = None
    text_transformation: DslValue[str] | None = None
