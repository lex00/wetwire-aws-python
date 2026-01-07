"""PropertyTypes for AWS::Connect::DataTableRecord."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataTableRecord(PropertyType):
    values: list[DslValue[Value]] = field(default_factory=list)
    primary_values: list[DslValue[Value]] = field(default_factory=list)


@dataclass
class Value(PropertyType):
    attribute_id: DslValue[str] | None = None
    attribute_value: DslValue[str] | None = None
