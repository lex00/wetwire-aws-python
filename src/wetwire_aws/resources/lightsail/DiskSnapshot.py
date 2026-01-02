"""PropertyTypes for AWS::Lightsail::DiskSnapshot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Location(PropertyType):
    availability_zone: str | None = None
    region_name: str | None = None
