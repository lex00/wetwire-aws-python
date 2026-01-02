"""PropertyTypes for AWS::Cases::CaseRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BooleanCondition(PropertyType):
    equal_to: BooleanOperands | None = None
    not_equal_to: BooleanOperands | None = None


@dataclass
class BooleanOperands(PropertyType):
    operand_one: OperandOne | None = None
    operand_two: OperandTwo | None = None
    result: bool | None = None


@dataclass
class CaseRuleDetails(PropertyType):
    hidden: HiddenCaseRule | None = None
    required: RequiredCaseRule | None = None


@dataclass
class HiddenCaseRule(PropertyType):
    conditions: list[BooleanCondition] = field(default_factory=list)
    default_value: bool | None = None


@dataclass
class OperandOne(PropertyType):
    field_id: str | None = None


@dataclass
class OperandTwo(PropertyType):
    boolean_value: bool | None = None
    double_value: float | None = None
    empty_value: dict[str, Any] | None = None
    string_value: str | None = None


@dataclass
class RequiredCaseRule(PropertyType):
    conditions: list[BooleanCondition] = field(default_factory=list)
    default_value: bool | None = None
