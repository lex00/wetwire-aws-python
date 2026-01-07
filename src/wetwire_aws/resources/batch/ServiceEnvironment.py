"""PropertyTypes for AWS::Batch::ServiceEnvironment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapacityLimit(PropertyType):
    capacity_unit: DslValue[str] | None = None
    max_capacity: DslValue[int] | None = None
