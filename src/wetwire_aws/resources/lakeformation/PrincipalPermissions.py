"""PropertyTypes for AWS::LakeFormation::PrincipalPermissions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ColumnWildcard(PropertyType):
    excluded_column_names: list[String] = field(default_factory=list)


@dataclass
class DataCellsFilterResource(PropertyType):
    database_name: str | None = None
    name: str | None = None
    table_catalog_id: str | None = None
    table_name: str | None = None


@dataclass
class DataLakePrincipal(PropertyType):
    data_lake_principal_identifier: str | None = None


@dataclass
class DataLocationResource(PropertyType):
    catalog_id: str | None = None
    resource_arn: str | None = None


@dataclass
class DatabaseResource(PropertyType):
    catalog_id: str | None = None
    name: str | None = None


@dataclass
class LFTag(PropertyType):
    tag_key: str | None = None
    tag_values: list[String] = field(default_factory=list)


@dataclass
class LFTagKeyResource(PropertyType):
    catalog_id: str | None = None
    tag_key: str | None = None
    tag_values: list[String] = field(default_factory=list)


@dataclass
class LFTagPolicyResource(PropertyType):
    catalog_id: str | None = None
    expression: list[LFTag] = field(default_factory=list)
    resource_type: str | None = None


@dataclass
class Resource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lf_tag": "LFTag",
        "lf_tag_policy": "LFTagPolicy",
    }

    catalog: dict[str, Any] | None = None
    data_cells_filter: DataCellsFilterResource | None = None
    data_location: DataLocationResource | None = None
    database: DatabaseResource | None = None
    lf_tag: LFTagKeyResource | None = None
    lf_tag_policy: LFTagPolicyResource | None = None
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
    database_name: str | None = None
    name: str | None = None
    column_names: list[String] = field(default_factory=list)
    column_wildcard: ColumnWildcard | None = None
