"""PropertyTypes for AWS::EC2::NetworkInsightsPath."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FilterPortRange(PropertyType):
    from_port: int | None = None
    to_port: int | None = None


@dataclass
class PathFilter(PropertyType):
    destination_address: str | None = None
    destination_port_range: FilterPortRange | None = None
    source_address: str | None = None
    source_port_range: FilterPortRange | None = None
