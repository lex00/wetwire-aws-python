"""PropertyTypes for AWS::MSK::Configuration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LatestRevision(PropertyType):
    creation_time: str | None = None
    description: str | None = None
    revision: int | None = None
