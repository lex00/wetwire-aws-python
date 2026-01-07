"""PropertyTypes for AWS::Lightsail::Instance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AddOn(PropertyType):
    add_on_type: DslValue[str] | None = None
    auto_snapshot_add_on_request: DslValue[AutoSnapshotAddOn] | None = None
    status: DslValue[str] | None = None


@dataclass
class AutoSnapshotAddOn(PropertyType):
    snapshot_time_of_day: DslValue[str] | None = None


@dataclass
class Disk(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iops": "IOPS",
    }

    disk_name: DslValue[str] | None = None
    path: DslValue[str] | None = None
    attached_to: DslValue[str] | None = None
    attachment_state: DslValue[str] | None = None
    iops: DslValue[int] | None = None
    is_system_disk: DslValue[bool] | None = None
    size_in_gb: DslValue[str] | None = None


@dataclass
class Hardware(PropertyType):
    cpu_count: DslValue[int] | None = None
    disks: list[DslValue[Disk]] = field(default_factory=list)
    ram_size_in_gb: DslValue[int] | None = None


@dataclass
class Location(PropertyType):
    availability_zone: DslValue[str] | None = None
    region_name: DslValue[str] | None = None


@dataclass
class MonthlyTransfer(PropertyType):
    gb_per_month_allocated: DslValue[str] | None = None


@dataclass
class Networking(PropertyType):
    ports: list[DslValue[Port]] = field(default_factory=list)
    monthly_transfer: DslValue[MonthlyTransfer] | None = None


@dataclass
class Port(PropertyType):
    access_direction: DslValue[str] | None = None
    access_from: DslValue[str] | None = None
    access_type: DslValue[str] | None = None
    cidr_list_aliases: list[DslValue[str]] = field(default_factory=list)
    cidrs: list[DslValue[str]] = field(default_factory=list)
    common_name: DslValue[str] | None = None
    from_port: DslValue[int] | None = None
    ipv6_cidrs: list[DslValue[str]] = field(default_factory=list)
    protocol: DslValue[str] | None = None
    to_port: DslValue[int] | None = None


@dataclass
class State(PropertyType):
    code: DslValue[int] | None = None
    name: DslValue[str] | None = None
