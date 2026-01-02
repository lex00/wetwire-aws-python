"""PropertyTypes for AWS::ECR::PublicRepository."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RepositoryCatalogData(PropertyType):
    about_text: str | None = None
    architectures: list[String] = field(default_factory=list)
    operating_systems: list[String] = field(default_factory=list)
    repository_description: str | None = None
    usage_text: str | None = None
