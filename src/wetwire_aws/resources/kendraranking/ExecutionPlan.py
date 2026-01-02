"""PropertyTypes for AWS::KendraRanking::ExecutionPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapacityUnitsConfiguration(PropertyType):
    rescore_capacity_units: int | None = None
