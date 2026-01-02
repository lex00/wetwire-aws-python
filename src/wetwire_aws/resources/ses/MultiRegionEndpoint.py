"""PropertyTypes for AWS::SES::MultiRegionEndpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Details(PropertyType):
    route_details: list[RouteDetailsItems] = field(default_factory=list)


@dataclass
class RouteDetailsItems(PropertyType):
    region: str | None = None
