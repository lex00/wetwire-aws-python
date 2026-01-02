"""PropertyTypes for AWS::GuardDuty::Filter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Condition(PropertyType):
    eq: list[String] = field(default_factory=list)
    equals: list[String] = field(default_factory=list)
    greater_than: int | None = None
    greater_than_or_equal: int | None = None
    gt: int | None = None
    gte: int | None = None
    less_than: int | None = None
    less_than_or_equal: int | None = None
    lt: int | None = None
    lte: int | None = None
    neq: list[String] = field(default_factory=list)
    not_equals: list[String] = field(default_factory=list)


@dataclass
class FindingCriteria(PropertyType):
    criterion: dict[str, Condition] = field(default_factory=dict)


@dataclass
class TagItem(PropertyType):
    key: str | None = None
    value: str | None = None
