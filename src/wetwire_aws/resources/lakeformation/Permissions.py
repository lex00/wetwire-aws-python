"""PropertyTypes for AWS::LakeFormation::Permissions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ColumnWildcard(PropertyType):
    excluded_column_names: list[String] = field(default_factory=list)


@dataclass
class DataLakePrincipal(PropertyType):
    data_lake_principal_identifier: str | None = None


@dataclass
class DataLocationResource(PropertyType):
    catalog_id: str | None = None
    s3_resource: str | None = None


@dataclass
class DatabaseResource(PropertyType):
    catalog_id: str | None = None
    name: str | None = None


@dataclass
class Resource(PropertyType):
    data_location_resource: DataLocationResource | None = None
    database_resource: DatabaseResource | None = None
    table_resource: TableResource | None = None
    table_with_columns_resource: TableWithColumnsResource | None = None


@dataclass
class TableResource(PropertyType):
    catalog_id: str | None = None
    database_name: str | None = None
    name: str | None = None
    table_wildcard: TableWildcard | None = None


@dataclass
class TableWildcard(PropertyType):
    pass


@dataclass
class TableWithColumnsResource(PropertyType):
    catalog_id: str | None = None
    column_names: list[String] = field(default_factory=list)
    column_wildcard: ColumnWildcard | None = None
    database_name: str | None = None
    name: str | None = None
