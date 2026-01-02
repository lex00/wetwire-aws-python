"""PropertyTypes for AWS::Connect::DataTableAttribute."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Enum(PropertyType):
    strict: bool | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class LockVersion(PropertyType):
    attribute: str | None = None
    data_table: str | None = None


@dataclass
class Validation(PropertyType):
    enum: Enum | None = None
    exclusive_maximum: float | None = None
    exclusive_minimum: float | None = None
    max_length: int | None = None
    max_values: int | None = None
    maximum: float | None = None
    min_length: int | None = None
    min_values: int | None = None
    minimum: float | None = None
    multiple_of: float | None = None
