"""PropertyTypes for AWS::CloudTrail::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Destination(PropertyType):
    location: str | None = None
    type_: str | None = None
