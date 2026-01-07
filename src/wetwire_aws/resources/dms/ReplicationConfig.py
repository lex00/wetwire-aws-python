"""PropertyTypes for AWS::DMS::ReplicationConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComputeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "multi_az": "MultiAZ",
    }

    max_capacity_units: DslValue[int] | None = None
    availability_zone: DslValue[str] | None = None
    dns_name_servers: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
    min_capacity_units: DslValue[int] | None = None
    multi_az: DslValue[bool] | None = None
    preferred_maintenance_window: DslValue[str] | None = None
    replication_subnet_group_id: DslValue[str] | None = None
    vpc_security_group_ids: list[DslValue[str]] = field(default_factory=list)
