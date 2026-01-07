"""PropertyTypes for AWS::LakeFormation::DataLakeSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Admins(PropertyType):
    pass


@dataclass
class CreateDatabaseDefaultPermissions(PropertyType):
    pass


@dataclass
class CreateTableDefaultPermissions(PropertyType):
    pass


@dataclass
class DataLakePrincipal(PropertyType):
    data_lake_principal_identifier: DslValue[str] | None = None


@dataclass
class ExternalDataFilteringAllowList(PropertyType):
    pass


@dataclass
class PrincipalPermissions(PropertyType):
    permissions: list[DslValue[str]] = field(default_factory=list)
    principal: DslValue[DataLakePrincipal] | None = None


@dataclass
class ReadOnlyAdmins(PropertyType):
    pass
