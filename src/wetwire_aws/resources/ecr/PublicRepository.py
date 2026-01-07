"""PropertyTypes for AWS::ECR::PublicRepository."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RepositoryCatalogData(PropertyType):
    about_text: DslValue[str] | None = None
    architectures: list[DslValue[str]] = field(default_factory=list)
    operating_systems: list[DslValue[str]] = field(default_factory=list)
    repository_description: DslValue[str] | None = None
    usage_text: DslValue[str] | None = None
