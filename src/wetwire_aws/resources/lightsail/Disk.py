"""PropertyTypes for AWS::Lightsail::Disk."""

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
class Location(PropertyType):
    availability_zone: DslValue[str] | None = None
    region_name: DslValue[str] | None = None
