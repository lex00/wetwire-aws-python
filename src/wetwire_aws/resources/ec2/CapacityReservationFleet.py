"""PropertyTypes for AWS::EC2::CapacityReservationFleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class InstanceTypeSpecification(PropertyType):
    availability_zone: DslValue[str] | None = None
    availability_zone_id: DslValue[str] | None = None
    ebs_optimized: DslValue[bool] | None = None
    instance_platform: DslValue[str] | None = None
    instance_type: DslValue[str] | None = None
    priority: DslValue[int] | None = None
    weight: DslValue[float] | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
