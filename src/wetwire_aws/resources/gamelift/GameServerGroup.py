"""PropertyTypes for AWS::GameLift::GameServerGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoScalingPolicy(PropertyType):
    target_tracking_configuration: TargetTrackingConfiguration | None = None
    estimated_instance_warmup: float | None = None


@dataclass
class InstanceDefinition(PropertyType):
    instance_type: str | None = None
    weighted_capacity: str | None = None


@dataclass
class LaunchTemplate(PropertyType):
    launch_template_id: str | None = None
    launch_template_name: str | None = None
    version: str | None = None


@dataclass
class TargetTrackingConfiguration(PropertyType):
    target_value: float | None = None
