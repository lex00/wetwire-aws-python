"""PropertyTypes for AWS::EC2::NatGateway."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AvailabilityZoneAddress(PropertyType):
    allocation_ids: list[DslValue[str]] = field(default_factory=list)
    availability_zone: DslValue[str] | None = None
    availability_zone_id: DslValue[str] | None = None
