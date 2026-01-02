"""PropertyTypes for AWS::Location::Map."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MapConfiguration(PropertyType):
    style: str | None = None
    custom_layers: list[String] = field(default_factory=list)
    political_view: str | None = None
