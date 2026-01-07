"""PropertyTypes for AWS::LakeFormation::Permissions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ColumnWildcard(PropertyType):
    excluded_column_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DataLakePrincipal(PropertyType):
    data_lake_principal_identifier: DslValue[str] | None = None


@dataclass
class DataLocationResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    s3_resource: DslValue[str] | None = None


@dataclass
class DatabaseResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class Resource(PropertyType):
    data_location_resource: DslValue[DataLocationResource] | None = None
    database_resource: DslValue[DatabaseResource] | None = None
    table_resource: DslValue[TableResource] | None = None
    table_with_columns_resource: DslValue[TableWithColumnsResource] | None = None


@dataclass
class TableResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
    table_wildcard: DslValue[TableWildcard] | None = None


@dataclass
class TableWildcard(PropertyType):
    pass


@dataclass
class TableWithColumnsResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    column_names: list[DslValue[str]] = field(default_factory=list)
    column_wildcard: DslValue[ColumnWildcard] | None = None
    database_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
