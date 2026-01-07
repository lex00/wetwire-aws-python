"""PropertyTypes for AWS::MediaLive::Network."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IpPool(PropertyType):
    cidr: DslValue[str] | None = None


@dataclass
class Route(PropertyType):
    cidr: DslValue[str] | None = None
    gateway: DslValue[str] | None = None


@dataclass
class Tags(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None
