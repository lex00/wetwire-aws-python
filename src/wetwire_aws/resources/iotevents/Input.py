"""PropertyTypes for AWS::IoTEvents::Input."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Attribute(PropertyType):
    json_path: DslValue[str] | None = None


@dataclass
class InputDefinition(PropertyType):
    attributes: list[DslValue[Attribute]] = field(default_factory=list)
