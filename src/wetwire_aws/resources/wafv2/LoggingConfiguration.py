"""PropertyTypes for AWS::WAFv2::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActionCondition(PropertyType):
    action: DslValue[str] | None = None


@dataclass
class Condition(PropertyType):
    action_condition: DslValue[ActionCondition] | None = None
    label_name_condition: DslValue[LabelNameCondition] | None = None


@dataclass
class FieldToMatch(PropertyType):
    method: DslValue[dict[str, Any]] | None = None
    query_string: DslValue[dict[str, Any]] | None = None
    single_header: DslValue[SingleHeader] | None = None
    uri_path: DslValue[dict[str, Any]] | None = None


@dataclass
class Filter(PropertyType):
    behavior: DslValue[str] | None = None
    conditions: list[DslValue[Condition]] = field(default_factory=list)
    requirement: DslValue[str] | None = None


@dataclass
class LabelNameCondition(PropertyType):
    label_name: DslValue[str] | None = None


@dataclass
class LoggingFilter(PropertyType):
    default_behavior: DslValue[str] | None = None
    filters: list[DslValue[Filter]] = field(default_factory=list)


@dataclass
class SingleHeader(PropertyType):
    name: DslValue[str] | None = None
