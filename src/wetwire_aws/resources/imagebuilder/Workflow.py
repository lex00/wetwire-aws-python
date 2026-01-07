"""PropertyTypes for AWS::ImageBuilder::Workflow."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LatestVersion(PropertyType):
    arn: DslValue[str] | None = None
    major: DslValue[str] | None = None
    minor: DslValue[str] | None = None
    patch: DslValue[str] | None = None
