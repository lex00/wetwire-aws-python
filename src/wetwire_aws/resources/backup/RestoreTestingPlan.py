"""PropertyTypes for AWS::Backup::RestoreTestingPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RestoreTestingRecoveryPointSelection(PropertyType):
    algorithm: DslValue[str] | None = None
    include_vaults: list[DslValue[str]] = field(default_factory=list)
    recovery_point_types: list[DslValue[str]] = field(default_factory=list)
    exclude_vaults: list[DslValue[str]] = field(default_factory=list)
    selection_window_days: DslValue[int] | None = None
