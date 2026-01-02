"""PropertyTypes for AWS::LakeFormation::TagAssociation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DatabaseResource(PropertyType):
    catalog_id: str | None = None
    name: str | None = None


@dataclass
class LFTagPair(PropertyType):
    catalog_id: str | None = None
    tag_key: str | None = None
    tag_values: list[String] = field(default_factory=list)


@dataclass
class Resource(PropertyType):
    catalog: dict[str, Any] | None = None
    database: DatabaseResource | None = None
    table: TableResource | None = None
    table_with_columns: TableWithColumnsResource | None = None


@dataclass
class TableResource(PropertyType):
    catalog_id: str | None = None
    database_name: str | None = None
    name: str | None = None
    table_wildcard: dict[str, Any] | None = None


@dataclass
class TableWithColumnsResource(PropertyType):
    catalog_id: str | None = None
    column_names: list[String] = field(default_factory=list)
    database_name: str | None = None
    name: str | None = None
