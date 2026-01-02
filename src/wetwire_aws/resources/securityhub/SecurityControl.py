"""PropertyTypes for AWS::SecurityHub::SecurityControl."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ParameterConfiguration(PropertyType):
    value_type: str | None = None
    value: ParameterValue | None = None


@dataclass
class ParameterValue(PropertyType):
    boolean: bool | None = None
    double: float | None = None
    enum: str | None = None
    enum_list: list[String] = field(default_factory=list)
    integer: int | None = None
    integer_list: list[Integer] = field(default_factory=list)
    string: str | None = None
    string_list: list[String] = field(default_factory=list)
