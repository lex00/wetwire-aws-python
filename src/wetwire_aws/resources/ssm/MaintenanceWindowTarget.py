"""PropertyTypes for AWS::SSM::MaintenanceWindowTarget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Targets(PropertyType):
    key: str | None = None
    values: list[String] = field(default_factory=list)
