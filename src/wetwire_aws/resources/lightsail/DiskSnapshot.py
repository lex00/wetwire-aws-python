"""PropertyTypes for AWS::Lightsail::DiskSnapshot."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Location(PropertyType):
    availability_zone: DslValue[str] | None = None
    region_name: DslValue[str] | None = None
