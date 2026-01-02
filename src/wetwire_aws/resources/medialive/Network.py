"""PropertyTypes for AWS::MediaLive::Network."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IpPool(PropertyType):
    cidr: str | None = None


@dataclass
class Route(PropertyType):
    cidr: str | None = None
    gateway: str | None = None


@dataclass
class Tags(PropertyType):
    key: str | None = None
    value: str | None = None
