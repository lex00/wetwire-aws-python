"""PropertyTypes for AWS::Lightsail::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DomainEntry(PropertyType):
    name: DslValue[str] | None = None
    target: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    id: DslValue[str] | None = None
    is_alias: DslValue[bool] | None = None


@dataclass
class Location(PropertyType):
    availability_zone: DslValue[str] | None = None
    region_name: DslValue[str] | None = None
