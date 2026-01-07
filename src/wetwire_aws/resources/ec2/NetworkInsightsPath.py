"""PropertyTypes for AWS::EC2::NetworkInsightsPath."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FilterPortRange(PropertyType):
    from_port: DslValue[int] | None = None
    to_port: DslValue[int] | None = None


@dataclass
class PathFilter(PropertyType):
    destination_address: DslValue[str] | None = None
    destination_port_range: DslValue[FilterPortRange] | None = None
    source_address: DslValue[str] | None = None
    source_port_range: DslValue[FilterPortRange] | None = None
