"""PropertyTypes for AWS::ECR::ReplicationConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ReplicationConfiguration(PropertyType):
    rules: list[ReplicationRule] = field(default_factory=list)


@dataclass
class ReplicationDestination(PropertyType):
    region: str | None = None
    registry_id: str | None = None


@dataclass
class ReplicationRule(PropertyType):
    destinations: list[ReplicationDestination] = field(default_factory=list)
    repository_filters: list[RepositoryFilter] = field(default_factory=list)


@dataclass
class RepositoryFilter(PropertyType):
    filter: str | None = None
    filter_type: str | None = None
