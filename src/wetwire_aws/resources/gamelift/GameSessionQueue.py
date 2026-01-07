"""PropertyTypes for AWS::GameLift::GameSessionQueue."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FilterConfiguration(PropertyType):
    allowed_locations: list[DslValue[str]] = field(default_factory=list)


@dataclass
class GameSessionQueueDestination(PropertyType):
    destination_arn: DslValue[str] | None = None


@dataclass
class PlayerLatencyPolicy(PropertyType):
    maximum_individual_player_latency_milliseconds: DslValue[int] | None = None
    policy_duration_seconds: DslValue[int] | None = None


@dataclass
class PriorityConfiguration(PropertyType):
    location_order: list[DslValue[str]] = field(default_factory=list)
    priority_order: list[DslValue[str]] = field(default_factory=list)
