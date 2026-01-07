"""PropertyTypes for AWS::EC2::NetworkAclEntry."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Icmp(PropertyType):
    code: DslValue[int] | None = None
    type_: DslValue[int] | None = None


@dataclass
class PortRange(PropertyType):
    from_: DslValue[int] | None = None
    to: DslValue[int] | None = None
