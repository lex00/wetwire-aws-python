"""PropertyTypes for AWS::Lightsail::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DomainEntry(PropertyType):
    name: str | None = None
    target: str | None = None
    type_: str | None = None
    id: str | None = None
    is_alias: bool | None = None


@dataclass
class Location(PropertyType):
    availability_zone: str | None = None
    region_name: str | None = None
