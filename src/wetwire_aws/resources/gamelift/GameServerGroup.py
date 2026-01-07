"""PropertyTypes for AWS::GameLift::GameServerGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoScalingPolicy(PropertyType):
    target_tracking_configuration: DslValue[TargetTrackingConfiguration] | None = None
    estimated_instance_warmup: DslValue[float] | None = None


@dataclass
class InstanceDefinition(PropertyType):
    instance_type: DslValue[str] | None = None
    weighted_capacity: DslValue[str] | None = None


@dataclass
class LaunchTemplate(PropertyType):
    launch_template_id: DslValue[str] | None = None
    launch_template_name: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class TargetTrackingConfiguration(PropertyType):
    target_value: DslValue[float] | None = None
