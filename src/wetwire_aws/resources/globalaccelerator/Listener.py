"""PropertyTypes for AWS::GlobalAccelerator::Listener."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PortRange(PropertyType):
    from_port: int | None = None
    to_port: int | None = None
