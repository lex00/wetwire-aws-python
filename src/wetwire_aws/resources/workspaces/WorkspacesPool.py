"""PropertyTypes for AWS::WorkSpaces::WorkspacesPool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ApplicationSettings(PropertyType):
    status: str | None = None
    settings_group: str | None = None


@dataclass
class Capacity(PropertyType):
    desired_user_sessions: int | None = None


@dataclass
class TimeoutSettings(PropertyType):
    disconnect_timeout_in_seconds: int | None = None
    idle_disconnect_timeout_in_seconds: int | None = None
    max_user_duration_in_seconds: int | None = None
