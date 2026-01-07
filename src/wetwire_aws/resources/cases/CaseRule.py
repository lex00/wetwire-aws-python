"""PropertyTypes for AWS::Cases::CaseRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BooleanCondition(PropertyType):
    equal_to: DslValue[BooleanOperands] | None = None
    not_equal_to: DslValue[BooleanOperands] | None = None


@dataclass
class BooleanOperands(PropertyType):
    operand_one: DslValue[OperandOne] | None = None
    operand_two: DslValue[OperandTwo] | None = None
    result: DslValue[bool] | None = None


@dataclass
class CaseRuleDetails(PropertyType):
    hidden: DslValue[HiddenCaseRule] | None = None
    required: DslValue[RequiredCaseRule] | None = None


@dataclass
class HiddenCaseRule(PropertyType):
    conditions: list[DslValue[BooleanCondition]] = field(default_factory=list)
    default_value: DslValue[bool] | None = None


@dataclass
class OperandOne(PropertyType):
    field_id: DslValue[str] | None = None


@dataclass
class OperandTwo(PropertyType):
    boolean_value: DslValue[bool] | None = None
    double_value: DslValue[float] | None = None
    empty_value: DslValue[dict[str, Any]] | None = None
    string_value: DslValue[str] | None = None


@dataclass
class RequiredCaseRule(PropertyType):
    conditions: list[DslValue[BooleanCondition]] = field(default_factory=list)
    default_value: DslValue[bool] | None = None
