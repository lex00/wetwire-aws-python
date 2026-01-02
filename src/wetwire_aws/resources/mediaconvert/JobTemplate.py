"""PropertyTypes for AWS::MediaConvert::JobTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccelerationSettings(PropertyType):
    mode: str | None = None


@dataclass
class HopDestination(PropertyType):
    priority: int | None = None
    queue: str | None = None
    wait_minutes: int | None = None
