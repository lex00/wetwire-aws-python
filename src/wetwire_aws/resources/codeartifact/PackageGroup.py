"""PropertyTypes for AWS::CodeArtifact::PackageGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class OriginConfiguration(PropertyType):
    restrictions: DslValue[Restrictions] | None = None


@dataclass
class RestrictionType(PropertyType):
    restriction_mode: DslValue[str] | None = None
    repositories: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Restrictions(PropertyType):
    external_upstream: DslValue[RestrictionType] | None = None
    internal_upstream: DslValue[RestrictionType] | None = None
    publish: DslValue[RestrictionType] | None = None
