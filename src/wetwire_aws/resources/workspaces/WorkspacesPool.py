"""PropertyTypes for AWS::WorkSpaces::WorkspacesPool."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ApplicationSettings(PropertyType):
    status: DslValue[str] | None = None
    settings_group: DslValue[str] | None = None


@dataclass
class Capacity(PropertyType):
    desired_user_sessions: DslValue[int] | None = None


@dataclass
class TimeoutSettings(PropertyType):
    disconnect_timeout_in_seconds: DslValue[int] | None = None
    idle_disconnect_timeout_in_seconds: DslValue[int] | None = None
    max_user_duration_in_seconds: DslValue[int] | None = None
