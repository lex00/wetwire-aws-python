"""PropertyTypes for AWS::ApplicationAutoScaling::ScalableTarget."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ScalableTargetAction(PropertyType):
    max_capacity: DslValue[int] | None = None
    min_capacity: DslValue[int] | None = None


@dataclass
class ScheduledAction(PropertyType):
    schedule: DslValue[str] | None = None
    scheduled_action_name: DslValue[str] | None = None
    end_time: DslValue[str] | None = None
    scalable_target_action: DslValue[ScalableTargetAction] | None = None
    start_time: DslValue[str] | None = None
    timezone: DslValue[str] | None = None


@dataclass
class SuspendedState(PropertyType):
    dynamic_scaling_in_suspended: DslValue[bool] | None = None
    dynamic_scaling_out_suspended: DslValue[bool] | None = None
    scheduled_scaling_suspended: DslValue[bool] | None = None
