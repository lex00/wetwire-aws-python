"""PropertyTypes for AWS::ECR::SigningConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RepositoryFilter(PropertyType):
    filter: str | None = None
    filter_type: str | None = None


@dataclass
class Rule(PropertyType):
    signing_profile_arn: str | None = None
    repository_filters: list[RepositoryFilter] = field(default_factory=list)
