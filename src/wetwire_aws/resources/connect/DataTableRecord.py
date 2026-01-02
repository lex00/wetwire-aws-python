"""PropertyTypes for AWS::Connect::DataTableRecord."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataTableRecord(PropertyType):
    values: list[Value] = field(default_factory=list)
    primary_values: list[Value] = field(default_factory=list)


@dataclass
class Value(PropertyType):
    attribute_id: str | None = None
    attribute_value: str | None = None
