"""PropertyTypes for AWS::SSM::MaintenanceWindowTarget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Targets(PropertyType):
    key: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)
