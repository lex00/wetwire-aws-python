"""PropertyTypes for AWS::GameLift::ContainerFleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConnectionPortRange(PropertyType):
    from_port: int | None = None
    to_port: int | None = None


@dataclass
class DeploymentConfiguration(PropertyType):
    impairment_strategy: str | None = None
    minimum_healthy_percentage: int | None = None
    protection_strategy: str | None = None


@dataclass
class DeploymentDetails(PropertyType):
    latest_deployment_id: str | None = None


@dataclass
class GameSessionCreationLimitPolicy(PropertyType):
    new_game_sessions_per_creator: int | None = None
    policy_period_in_minutes: int | None = None


@dataclass
class IpPermission(PropertyType):
    from_port: int | None = None
    ip_range: str | None = None
    protocol: str | None = None
    to_port: int | None = None


@dataclass
class LocationCapacity(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "desired_ec2_instances": "DesiredEC2Instances",
    }

    max_size: int | None = None
    min_size: int | None = None
    desired_ec2_instances: int | None = None


@dataclass
class LocationConfiguration(PropertyType):
    location: str | None = None
    location_capacity: LocationCapacity | None = None
    stopped_actions: list[String] = field(default_factory=list)


@dataclass
class LogConfiguration(PropertyType):
    log_destination: str | None = None
    log_group_arn: str | None = None
    s3_bucket_name: str | None = None


@dataclass
class ScalingPolicy(PropertyType):
    metric_name: str | None = None
    name: str | None = None
    comparison_operator: str | None = None
    evaluation_periods: int | None = None
    policy_type: str | None = None
    scaling_adjustment: int | None = None
    scaling_adjustment_type: str | None = None
    target_configuration: TargetConfiguration | None = None
    threshold: float | None = None


@dataclass
class TargetConfiguration(PropertyType):
    target_value: float | None = None
