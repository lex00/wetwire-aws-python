"""PropertyTypes for AWS::Glue::Database."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataLakePrincipal(PropertyType):
    data_lake_principal_identifier: DslValue[str] | None = None


@dataclass
class DatabaseIdentifier(PropertyType):
    catalog_id: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    region: DslValue[str] | None = None


@dataclass
class DatabaseInput(PropertyType):
    create_table_default_permissions: list[DslValue[PrincipalPrivileges]] = field(
        default_factory=list
    )
    description: DslValue[str] | None = None
    federated_database: DslValue[FederatedDatabase] | None = None
    location_uri: DslValue[str] | None = None
    name: DslValue[str] | None = None
    parameters: DslValue[dict[str, Any]] | None = None
    target_database: DslValue[DatabaseIdentifier] | None = None


@dataclass
class FederatedDatabase(PropertyType):
    connection_name: DslValue[str] | None = None
    identifier: DslValue[str] | None = None


@dataclass
class PrincipalPrivileges(PropertyType):
    permissions: list[DslValue[str]] = field(default_factory=list)
    principal: DslValue[DataLakePrincipal] | None = None
