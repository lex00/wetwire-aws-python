"""PropertyTypes for AWS::Glue::Database."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataLakePrincipal(PropertyType):
    data_lake_principal_identifier: str | None = None


@dataclass
class DatabaseIdentifier(PropertyType):
    catalog_id: str | None = None
    database_name: str | None = None
    region: str | None = None


@dataclass
class DatabaseInput(PropertyType):
    create_table_default_permissions: list[PrincipalPrivileges] = field(
        default_factory=list
    )
    description: str | None = None
    federated_database: FederatedDatabase | None = None
    location_uri: str | None = None
    name: str | None = None
    parameters: dict[str, Any] | None = None
    target_database: DatabaseIdentifier | None = None


@dataclass
class FederatedDatabase(PropertyType):
    connection_name: str | None = None
    identifier: str | None = None


@dataclass
class PrincipalPrivileges(PropertyType):
    permissions: list[String] = field(default_factory=list)
    principal: DataLakePrincipal | None = None
