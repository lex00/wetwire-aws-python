"""PropertyTypes for AWS::Connect::DataTableAttribute."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Enum(PropertyType):
    strict: DslValue[bool] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LockVersion(PropertyType):
    attribute: DslValue[str] | None = None
    data_table: DslValue[str] | None = None


@dataclass
class Validation(PropertyType):
    enum: DslValue[Enum] | None = None
    exclusive_maximum: DslValue[float] | None = None
    exclusive_minimum: DslValue[float] | None = None
    max_length: DslValue[int] | None = None
    max_values: DslValue[int] | None = None
    maximum: DslValue[float] | None = None
    min_length: DslValue[int] | None = None
    min_values: DslValue[int] | None = None
    minimum: DslValue[float] | None = None
    multiple_of: DslValue[float] | None = None
