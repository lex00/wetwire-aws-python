"""PropertyTypes for AWS::SES::MultiRegionEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Details(PropertyType):
    route_details: list[DslValue[RouteDetailsItems]] = field(default_factory=list)


@dataclass
class RouteDetailsItems(PropertyType):
    region: DslValue[str] | None = None
