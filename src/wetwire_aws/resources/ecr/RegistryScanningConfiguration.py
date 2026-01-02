"""PropertyTypes for AWS::ECR::RegistryScanningConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RepositoryFilter(PropertyType):
    filter: str | None = None
    filter_type: str | None = None


@dataclass
class ScanningRule(PropertyType):
    repository_filters: list[RepositoryFilter] = field(default_factory=list)
    scan_frequency: str | None = None
