"""PropertyTypes for AWS::EC2::TrafficMirrorFilterRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class TrafficMirrorPortRange(PropertyType):
    from_port: DslValue[int] | None = None
    to_port: DslValue[int] | None = None
