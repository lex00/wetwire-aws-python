"""PropertyTypes for AWS::ImageBuilder::Workflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LatestVersion(PropertyType):
    arn: str | None = None
    major: str | None = None
    minor: str | None = None
    patch: str | None = None
