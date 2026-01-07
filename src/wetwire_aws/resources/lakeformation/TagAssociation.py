"""PropertyTypes for AWS::LakeFormation::TagAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DatabaseResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class LFTagPair(PropertyType):
    catalog_id: DslValue[str] | None = None
    tag_key: DslValue[str] | None = None
    tag_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Resource(PropertyType):
    catalog: DslValue[dict[str, Any]] | None = None
    database: DslValue[DatabaseResource] | None = None
    table: DslValue[TableResource] | None = None
    table_with_columns: DslValue[TableWithColumnsResource] | None = None


@dataclass
class TableResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
    table_wildcard: DslValue[dict[str, Any]] | None = None


@dataclass
class TableWithColumnsResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    column_names: list[DslValue[str]] = field(default_factory=list)
    database_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
