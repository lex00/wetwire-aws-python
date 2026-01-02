"""PropertyTypes for AWS::ApplicationAutoScaling::ScalableTarget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ScalableTargetAction(PropertyType):
    max_capacity: int | None = None
    min_capacity: int | None = None


@dataclass
class ScheduledAction(PropertyType):
    schedule: str | None = None
    scheduled_action_name: str | None = None
    end_time: str | None = None
    scalable_target_action: ScalableTargetAction | None = None
    start_time: str | None = None
    timezone: str | None = None


@dataclass
class SuspendedState(PropertyType):
    dynamic_scaling_in_suspended: bool | None = None
    dynamic_scaling_out_suspended: bool | None = None
    scheduled_scaling_suspended: bool | None = None
