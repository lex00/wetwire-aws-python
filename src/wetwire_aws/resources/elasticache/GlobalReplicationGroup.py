"""PropertyTypes for AWS::ElastiCache::GlobalReplicationGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GlobalReplicationGroupMember(PropertyType):
    replication_group_id: str | None = None
    replication_group_region: str | None = None
    role: str | None = None


@dataclass
class RegionalConfiguration(PropertyType):
    replication_group_id: str | None = None
    replication_group_region: str | None = None
    resharding_configurations: list[ReshardingConfiguration] = field(
        default_factory=list
    )


@dataclass
class ReshardingConfiguration(PropertyType):
    node_group_id: str | None = None
    preferred_availability_zones: list[String] = field(default_factory=list)
