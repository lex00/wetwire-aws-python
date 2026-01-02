"""PropertyTypes for AWS::WAFv2::LoggingConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActionCondition(PropertyType):
    action: str | None = None


@dataclass
class Condition(PropertyType):
    action_condition: ActionCondition | None = None
    label_name_condition: LabelNameCondition | None = None


@dataclass
class FieldToMatch(PropertyType):
    method: dict[str, Any] | None = None
    query_string: dict[str, Any] | None = None
    single_header: SingleHeader | None = None
    uri_path: dict[str, Any] | None = None


@dataclass
class Filter(PropertyType):
    behavior: str | None = None
    conditions: list[Condition] = field(default_factory=list)
    requirement: str | None = None


@dataclass
class LabelNameCondition(PropertyType):
    label_name: str | None = None


@dataclass
class LoggingFilter(PropertyType):
    default_behavior: str | None = None
    filters: list[Filter] = field(default_factory=list)


@dataclass
class SingleHeader(PropertyType):
    name: str | None = None
