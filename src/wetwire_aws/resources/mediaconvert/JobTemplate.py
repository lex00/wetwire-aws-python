"""PropertyTypes for AWS::MediaConvert::JobTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccelerationSettings(PropertyType):
    mode: DslValue[str] | None = None


@dataclass
class HopDestination(PropertyType):
    priority: DslValue[int] | None = None
    queue: DslValue[str] | None = None
    wait_minutes: DslValue[int] | None = None
