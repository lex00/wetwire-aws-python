"""PropertyTypes for AWS::Macie::FindingsFilter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CriterionAdditionalProperties(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "eq": "eq",
        "gt": "gt",
        "gte": "gte",
        "lt": "lt",
        "lte": "lte",
        "neq": "neq",
    }

    eq: list[DslValue[str]] = field(default_factory=list)
    gt: DslValue[int] | None = None
    gte: DslValue[int] | None = None
    lt: DslValue[int] | None = None
    lte: DslValue[int] | None = None
    neq: list[DslValue[str]] = field(default_factory=list)


@dataclass
class FindingCriteria(PropertyType):
    criterion: dict[str, DslValue[CriterionAdditionalProperties]] = field(
        default_factory=dict
    )
