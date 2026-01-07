"""PropertyTypes for AWS::CloudTrail::Channel."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Destination(PropertyType):
    location: DslValue[str] | None = None
    type_: DslValue[str] | None = None
