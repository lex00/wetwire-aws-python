"""PropertyTypes for AWS::EC2::TrafficMirrorFilterRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class TrafficMirrorPortRange(PropertyType):
    from_port: int | None = None
    to_port: int | None = None
