"""PropertyTypes for AWS::WAF::SizeConstraintSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FieldToMatch(PropertyType):
    type_: str | None = None
    data: str | None = None


@dataclass
class SizeConstraint(PropertyType):
    comparison_operator: str | None = None
    field_to_match: FieldToMatch | None = None
    size: int | None = None
    text_transformation: str | None = None
