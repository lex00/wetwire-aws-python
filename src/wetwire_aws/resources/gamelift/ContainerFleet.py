"""PropertyTypes for AWS::GameLift::ContainerFleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConnectionPortRange(PropertyType):
    from_port: DslValue[int] | None = None
    to_port: DslValue[int] | None = None


@dataclass
class DeploymentConfiguration(PropertyType):
    impairment_strategy: DslValue[str] | None = None
    minimum_healthy_percentage: DslValue[int] | None = None
    protection_strategy: DslValue[str] | None = None


@dataclass
class DeploymentDetails(PropertyType):
    latest_deployment_id: DslValue[str] | None = None


@dataclass
class GameSessionCreationLimitPolicy(PropertyType):
    new_game_sessions_per_creator: DslValue[int] | None = None
    policy_period_in_minutes: DslValue[int] | None = None


@dataclass
class IpPermission(PropertyType):
    from_port: DslValue[int] | None = None
    ip_range: DslValue[str] | None = None
    protocol: DslValue[str] | None = None
    to_port: DslValue[int] | None = None


@dataclass
class LocationCapacity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "desired_ec2_instances": "DesiredEC2Instances",
    }

    max_size: DslValue[int] | None = None
    min_size: DslValue[int] | None = None
    desired_ec2_instances: DslValue[int] | None = None


@dataclass
class LocationConfiguration(PropertyType):
    location: DslValue[str] | None = None
    location_capacity: DslValue[LocationCapacity] | None = None
    stopped_actions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LogConfiguration(PropertyType):
    log_destination: DslValue[str] | None = None
    log_group_arn: DslValue[str] | None = None
    s3_bucket_name: DslValue[str] | None = None


@dataclass
class ScalingPolicy(PropertyType):
    metric_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
    comparison_operator: DslValue[str] | None = None
    evaluation_periods: DslValue[int] | None = None
    policy_type: DslValue[str] | None = None
    scaling_adjustment: DslValue[int] | None = None
    scaling_adjustment_type: DslValue[str] | None = None
    target_configuration: DslValue[TargetConfiguration] | None = None
    threshold: DslValue[float] | None = None


@dataclass
class TargetConfiguration(PropertyType):
    target_value: DslValue[float] | None = None
