"""PropertyTypes for AWS::ControlTower::EnabledBaseline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Parameter(PropertyType):
    key: str | None = None
    value: dict[str, Any] | None = None
