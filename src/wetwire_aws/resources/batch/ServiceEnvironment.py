"""PropertyTypes for AWS::Batch::ServiceEnvironment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapacityLimit(PropertyType):
    capacity_unit: str | None = None
    max_capacity: int | None = None
