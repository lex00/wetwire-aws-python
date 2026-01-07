"""PropertyTypes for AWS::Cassandra::Keyspace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ReplicationSpecification(PropertyType):
    region_list: list[DslValue[str]] = field(default_factory=list)
    replication_strategy: DslValue[str] | None = None
