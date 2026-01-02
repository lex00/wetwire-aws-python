"""PropertyTypes for AWS::DevOpsGuru::ResourceCollection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CloudFormationCollectionFilter(PropertyType):
    stack_names: list[String] = field(default_factory=list)


@dataclass
class ResourceCollectionFilter(PropertyType):
    cloud_formation: CloudFormationCollectionFilter | None = None
    tags: list[TagCollection] = field(default_factory=list)


@dataclass
class TagCollection(PropertyType):
    app_boundary_key: str | None = None
    tag_values: list[String] = field(default_factory=list)
