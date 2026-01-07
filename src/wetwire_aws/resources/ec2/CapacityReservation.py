"""PropertyTypes for AWS::EC2::CapacityReservation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapacityAllocation(PropertyType):
    allocation_type: DslValue[str] | None = None
    count: DslValue[int] | None = None


@dataclass
class CommitmentInfo(PropertyType):
    commitment_end_date: DslValue[str] | None = None
    committed_instance_count: DslValue[int] | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
