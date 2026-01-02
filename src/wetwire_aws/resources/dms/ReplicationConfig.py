"""PropertyTypes for AWS::DMS::ReplicationConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComputeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "multi_az": "MultiAZ",
    }

    max_capacity_units: int | None = None
    availability_zone: str | None = None
    dns_name_servers: str | None = None
    kms_key_id: str | None = None
    min_capacity_units: int | None = None
    multi_az: bool | None = None
    preferred_maintenance_window: str | None = None
    replication_subnet_group_id: str | None = None
    vpc_security_group_ids: list[String] = field(default_factory=list)
