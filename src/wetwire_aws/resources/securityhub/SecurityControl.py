"""PropertyTypes for AWS::SecurityHub::SecurityControl."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ParameterConfiguration(PropertyType):
    value_type: DslValue[str] | None = None
    value: DslValue[ParameterValue] | None = None


@dataclass
class ParameterValue(PropertyType):
    boolean: DslValue[bool] | None = None
    double: DslValue[float] | None = None
    enum: DslValue[str] | None = None
    enum_list: list[DslValue[str]] = field(default_factory=list)
    integer: DslValue[int] | None = None
    integer_list: list[DslValue[int]] = field(default_factory=list)
    string: DslValue[str] | None = None
    string_list: list[DslValue[str]] = field(default_factory=list)
