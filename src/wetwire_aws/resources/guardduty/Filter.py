"""PropertyTypes for AWS::GuardDuty::Filter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Condition(PropertyType):
    eq: list[DslValue[str]] = field(default_factory=list)
    equals: list[DslValue[str]] = field(default_factory=list)
    greater_than: DslValue[int] | None = None
    greater_than_or_equal: DslValue[int] | None = None
    gt: DslValue[int] | None = None
    gte: DslValue[int] | None = None
    less_than: DslValue[int] | None = None
    less_than_or_equal: DslValue[int] | None = None
    lt: DslValue[int] | None = None
    lte: DslValue[int] | None = None
    neq: list[DslValue[str]] = field(default_factory=list)
    not_equals: list[DslValue[str]] = field(default_factory=list)


@dataclass
class FindingCriteria(PropertyType):
    criterion: dict[str, DslValue[Condition]] = field(default_factory=dict)


@dataclass
class TagItem(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
