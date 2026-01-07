"""PropertyTypes for AWS::ControlTower::EnabledControl."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EnabledControlParameter(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[dict[str, Any]] | None = None
