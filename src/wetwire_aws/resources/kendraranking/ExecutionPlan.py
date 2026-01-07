"""PropertyTypes for AWS::KendraRanking::ExecutionPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapacityUnitsConfiguration(PropertyType):
    rescore_capacity_units: DslValue[int] | None = None
