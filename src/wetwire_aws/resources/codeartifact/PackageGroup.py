"""PropertyTypes for AWS::CodeArtifact::PackageGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class OriginConfiguration(PropertyType):
    restrictions: Restrictions | None = None


@dataclass
class RestrictionType(PropertyType):
    restriction_mode: str | None = None
    repositories: list[String] = field(default_factory=list)


@dataclass
class Restrictions(PropertyType):
    external_upstream: RestrictionType | None = None
    internal_upstream: RestrictionType | None = None
    publish: RestrictionType | None = None
