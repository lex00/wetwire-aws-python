"""PropertyTypes for AWS::GameLift::Alias."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RoutingStrategy(PropertyType):
    type_: str | None = None
    fleet_id: str | None = None
    message: str | None = None
