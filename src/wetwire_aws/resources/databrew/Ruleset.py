"""PropertyTypes for AWS::DataBrew::Ruleset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ColumnSelector(PropertyType):
    name: str | None = None
    regex: str | None = None


@dataclass
class Rule(PropertyType):
    check_expression: str | None = None
    name: str | None = None
    column_selectors: list[ColumnSelector] = field(default_factory=list)
    disabled: bool | None = None
    substitution_map: list[SubstitutionValue] = field(default_factory=list)
    threshold: Threshold | None = None


@dataclass
class SubstitutionValue(PropertyType):
    value: str | None = None
    value_reference: str | None = None


@dataclass
class Threshold(PropertyType):
    value: float | None = None
    type_: str | None = None
    unit: str | None = None
