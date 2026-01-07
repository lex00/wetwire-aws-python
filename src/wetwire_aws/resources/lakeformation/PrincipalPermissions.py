"""PropertyTypes for AWS::LakeFormation::PrincipalPermissions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ColumnWildcard(PropertyType):
    excluded_column_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DataCellsFilterResource(PropertyType):
    database_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
    table_catalog_id: DslValue[str] | None = None
    table_name: DslValue[str] | None = None


@dataclass
class DataLakePrincipal(PropertyType):
    data_lake_principal_identifier: DslValue[str] | None = None


@dataclass
class DataLocationResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    resource_arn: DslValue[str] | None = None


@dataclass
class DatabaseResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class LFTag(PropertyType):
    tag_key: DslValue[str] | None = None
    tag_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LFTagKeyResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    tag_key: DslValue[str] | None = None
    tag_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LFTagPolicyResource(PropertyType):
    catalog_id: DslValue[str] | None = None
    expression: list[DslValue[LFTag]] = field(default_factory=list)
    resource_type: DslValue[str] | None = None


@dataclass
class Resource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "lf_tag": "LFTag",
        "lf_tag_policy": "LFTagPolicy",
    }

    catalog: DslValue[dict[str, Any]] | None = None
    data_cells_filter: DslValue[DataCellsFilterResource] | None = None
    data_location: DslValue[DataLocationResource] | None = None
    database: DslValue[DatabaseResource] | None = None
    lf_tag: DslValue[LFTagKeyResource] | None = None
    lf_tag_policy: DslValue[LFTagPolicyResource] | None = None
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
    database_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
    column_names: list[DslValue[str]] = field(default_factory=list)
    column_wildcard: DslValue[ColumnWildcard] | None = None
