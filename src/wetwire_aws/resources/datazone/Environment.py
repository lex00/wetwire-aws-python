"""PropertyTypes for AWS::DataZone::Environment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class EnvironmentParameter(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None
