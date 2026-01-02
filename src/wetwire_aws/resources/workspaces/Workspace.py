"""PropertyTypes for AWS::WorkSpaces::Workspace."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class WorkspaceProperties(PropertyType):
    compute_type_name: str | None = None
    root_volume_size_gib: int | None = None
    running_mode: str | None = None
    running_mode_auto_stop_timeout_in_minutes: int | None = None
    user_volume_size_gib: int | None = None
