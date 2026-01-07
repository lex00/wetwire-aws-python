"""PropertyTypes for AWS::DevOpsGuru::ResourceCollection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CloudFormationCollectionFilter(PropertyType):
    stack_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ResourceCollectionFilter(PropertyType):
    cloud_formation: DslValue[CloudFormationCollectionFilter] | None = None
    tags: list[DslValue[TagCollection]] = field(default_factory=list)


@dataclass
class TagCollection(PropertyType):
    app_boundary_key: DslValue[str] | None = None
    tag_values: list[DslValue[str]] = field(default_factory=list)
