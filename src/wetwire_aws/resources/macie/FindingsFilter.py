"""PropertyTypes for AWS::Macie::FindingsFilter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


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

    eq: list[String] = field(default_factory=list)
    gt: int | None = None
    gte: int | None = None
    lt: int | None = None
    lte: int | None = None
    neq: list[String] = field(default_factory=list)


@dataclass
class FindingCriteria(PropertyType):
    criterion: dict[str, CriterionAdditionalProperties] = field(default_factory=dict)
