"""PropertyTypes for AWS::EC2::CapacityReservationFleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class InstanceTypeSpecification(PropertyType):
    availability_zone: str | None = None
    availability_zone_id: str | None = None
    ebs_optimized: bool | None = None
    instance_platform: str | None = None
    instance_type: str | None = None
    priority: int | None = None
    weight: float | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: str | None = None
    tags: list[Tag] = field(default_factory=list)
