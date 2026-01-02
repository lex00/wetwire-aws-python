"""PropertyTypes for AWS::GameLift::GameSessionQueue."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FilterConfiguration(PropertyType):
    allowed_locations: list[String] = field(default_factory=list)


@dataclass
class GameSessionQueueDestination(PropertyType):
    destination_arn: str | None = None


@dataclass
class PlayerLatencyPolicy(PropertyType):
    maximum_individual_player_latency_milliseconds: int | None = None
    policy_duration_seconds: int | None = None


@dataclass
class PriorityConfiguration(PropertyType):
    location_order: list[String] = field(default_factory=list)
    priority_order: list[String] = field(default_factory=list)
