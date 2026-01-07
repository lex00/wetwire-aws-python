"""PropertyTypes for AWS::GlobalAccelerator::Listener."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PortRange(PropertyType):
    from_port: DslValue[int] | None = None
    to_port: DslValue[int] | None = None
