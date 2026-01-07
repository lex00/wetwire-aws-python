"""PropertyTypes for AWS::Route53::CidrCollection."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Location(PropertyType):
    cidr_list: list[DslValue[str]] = field(default_factory=list)
    location_name: DslValue[str] | None = None
