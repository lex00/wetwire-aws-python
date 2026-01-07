"""PropertyTypes for AWS::ECR::ReplicationConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ReplicationConfiguration(PropertyType):
    rules: list[DslValue[ReplicationRule]] = field(default_factory=list)


@dataclass
class ReplicationDestination(PropertyType):
    region: DslValue[str] | None = None
    registry_id: DslValue[str] | None = None


@dataclass
class ReplicationRule(PropertyType):
    destinations: list[DslValue[ReplicationDestination]] = field(default_factory=list)
    repository_filters: list[DslValue[RepositoryFilter]] = field(default_factory=list)


@dataclass
class RepositoryFilter(PropertyType):
    filter: DslValue[str] | None = None
    filter_type: DslValue[str] | None = None
