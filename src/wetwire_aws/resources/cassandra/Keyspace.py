"""PropertyTypes for AWS::Cassandra::Keyspace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ReplicationSpecification(PropertyType):
    region_list: list[String] = field(default_factory=list)
    replication_strategy: str | None = None
