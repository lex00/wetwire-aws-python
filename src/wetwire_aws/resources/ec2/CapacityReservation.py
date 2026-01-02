"""PropertyTypes for AWS::EC2::CapacityReservation."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapacityAllocation(PropertyType):
    allocation_type: str | None = None
    count: int | None = None


@dataclass
class CommitmentInfo(PropertyType):
    commitment_end_date: str | None = None
    committed_instance_count: int | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: str | None = None
    tags: list[Tag] = field(default_factory=list)
