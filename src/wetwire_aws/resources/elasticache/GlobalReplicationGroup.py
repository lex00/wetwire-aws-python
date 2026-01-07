"""PropertyTypes for AWS::ElastiCache::GlobalReplicationGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GlobalReplicationGroupMember(PropertyType):
    replication_group_id: DslValue[str] | None = None
    replication_group_region: DslValue[str] | None = None
    role: DslValue[str] | None = None


@dataclass
class RegionalConfiguration(PropertyType):
    replication_group_id: DslValue[str] | None = None
    replication_group_region: DslValue[str] | None = None
    resharding_configurations: list[DslValue[ReshardingConfiguration]] = field(
        default_factory=list
    )


@dataclass
class ReshardingConfiguration(PropertyType):
    node_group_id: DslValue[str] | None = None
    preferred_availability_zones: list[DslValue[str]] = field(default_factory=list)
