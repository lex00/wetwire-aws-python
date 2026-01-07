"""PropertyTypes for AWS::LakeFormation::DataCellsFilter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ColumnWildcard(PropertyType):
    excluded_column_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RowFilter(PropertyType):
    all_rows_wildcard: DslValue[dict[str, Any]] | None = None
    filter_expression: DslValue[str] | None = None
