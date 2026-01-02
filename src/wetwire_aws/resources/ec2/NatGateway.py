"""PropertyTypes for AWS::EC2::NatGateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AvailabilityZoneAddress(PropertyType):
    allocation_ids: list[String] = field(default_factory=list)
    availability_zone: str | None = None
    availability_zone_id: str | None = None
