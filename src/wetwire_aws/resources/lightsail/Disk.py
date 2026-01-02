"""PropertyTypes for AWS::Lightsail::Disk."""

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
class Location(PropertyType):
    availability_zone: str | None = None
    region_name: str | None = None
