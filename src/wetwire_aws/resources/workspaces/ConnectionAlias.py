"""PropertyTypes for AWS::WorkSpaces::ConnectionAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConnectionAliasAssociation(PropertyType):
    associated_account_id: str | None = None
    association_status: str | None = None
    connection_identifier: str | None = None
    resource_id: str | None = None
