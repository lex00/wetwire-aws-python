"""PropertyTypes for AWS::Lightsail::Instance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AddOn(PropertyType):
    add_on_type: str | None = None
    auto_snapshot_add_on_request: AutoSnapshotAddOn | None = None
    status: str | None = None


@dataclass
class AutoSnapshotAddOn(PropertyType):
    snapshot_time_of_day: str | None = None


@dataclass
class Disk(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iops": "IOPS",
    }

    disk_name: str | None = None
    path: str | None = None
    attached_to: str | None = None
    attachment_state: str | None = None
    iops: int | None = None
    is_system_disk: bool | None = None
    size_in_gb: str | None = None


@dataclass
class Hardware(PropertyType):
    cpu_count: int | None = None
    disks: list[Disk] = field(default_factory=list)
    ram_size_in_gb: int | None = None


@dataclass
class Location(PropertyType):
    availability_zone: str | None = None
    region_name: str | None = None


@dataclass
class MonthlyTransfer(PropertyType):
    gb_per_month_allocated: str | None = None


@dataclass
class Networking(PropertyType):
    ports: list[Port] = field(default_factory=list)
    monthly_transfer: MonthlyTransfer | None = None


@dataclass
class Port(PropertyType):
    access_direction: str | None = None
    access_from: str | None = None
    access_type: str | None = None
    cidr_list_aliases: list[String] = field(default_factory=list)
    cidrs: list[String] = field(default_factory=list)
    common_name: str | None = None
    from_port: int | None = None
    ipv6_cidrs: list[String] = field(default_factory=list)
    protocol: str | None = None
    to_port: int | None = None


@dataclass
class State(PropertyType):
    code: int | None = None
    name: str | None = None
