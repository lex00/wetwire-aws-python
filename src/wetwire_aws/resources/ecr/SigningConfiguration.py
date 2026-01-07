"""PropertyTypes for AWS::ECR::SigningConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RepositoryFilter(PropertyType):
    filter: DslValue[str] | None = None
    filter_type: DslValue[str] | None = None


@dataclass
class Rule(PropertyType):
    signing_profile_arn: DslValue[str] | None = None
    repository_filters: list[DslValue[RepositoryFilter]] = field(default_factory=list)
