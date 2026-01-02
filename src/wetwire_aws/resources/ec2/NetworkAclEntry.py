"""PropertyTypes for AWS::EC2::NetworkAclEntry."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Icmp(PropertyType):
    code: int | None = None
    type_: int | None = None


@dataclass
class PortRange(PropertyType):
    from_: int | None = None
    to: int | None = None
