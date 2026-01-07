"""PropertyTypes for AWS::GameLift::Alias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RoutingStrategy(PropertyType):
    type_: DslValue[str] | None = None
    fleet_id: DslValue[str] | None = None
    message: DslValue[str] | None = None
