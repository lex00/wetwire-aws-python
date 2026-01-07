"""PropertyTypes for AWS::Location::Map."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MapConfiguration(PropertyType):
    style: DslValue[str] | None = None
    custom_layers: list[DslValue[str]] = field(default_factory=list)
    political_view: DslValue[str] | None = None
