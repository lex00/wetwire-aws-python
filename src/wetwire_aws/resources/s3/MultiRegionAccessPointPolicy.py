"""PropertyTypes for AWS::S3::MultiRegionAccessPointPolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PolicyStatus(PropertyType):
    is_public: str | None = None
