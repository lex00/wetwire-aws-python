"""PropertyTypes for AWS::Backup::RestoreTestingPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RestoreTestingRecoveryPointSelection(PropertyType):
    algorithm: str | None = None
    include_vaults: list[String] = field(default_factory=list)
    recovery_point_types: list[String] = field(default_factory=list)
    exclude_vaults: list[String] = field(default_factory=list)
    selection_window_days: int | None = None
