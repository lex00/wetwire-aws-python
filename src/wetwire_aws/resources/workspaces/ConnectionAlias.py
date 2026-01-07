"""PropertyTypes for AWS::WorkSpaces::ConnectionAlias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectionAliasAssociation(PropertyType):
    associated_account_id: DslValue[str] | None = None
    association_status: DslValue[str] | None = None
    connection_identifier: DslValue[str] | None = None
    resource_id: DslValue[str] | None = None
