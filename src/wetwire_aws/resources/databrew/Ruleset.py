"""PropertyTypes for AWS::DataBrew::Ruleset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ColumnSelector(PropertyType):
    name: DslValue[str] | None = None
    regex: DslValue[str] | None = None


@dataclass
class Rule(PropertyType):
    check_expression: DslValue[str] | None = None
    name: DslValue[str] | None = None
    column_selectors: list[DslValue[ColumnSelector]] = field(default_factory=list)
    disabled: DslValue[bool] | None = None
    substitution_map: list[DslValue[SubstitutionValue]] = field(default_factory=list)
    threshold: DslValue[Threshold] | None = None


@dataclass
class SubstitutionValue(PropertyType):
    value: DslValue[str] | None = None
    value_reference: DslValue[str] | None = None


@dataclass
class Threshold(PropertyType):
    value: DslValue[float] | None = None
    type_: DslValue[str] | None = None
    unit: DslValue[str] | None = None
