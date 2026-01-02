"""PropertyTypes for AWS::Route53::CidrCollection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Location(PropertyType):
    cidr_list: list[String] = field(default_factory=list)
    location_name: str | None = None
