"""PropertyTypes for AWS::GameLift::Fleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AnywhereConfiguration(PropertyType):
    cost: str | None = None


@dataclass
class CertificateConfiguration(PropertyType):
    certificate_type: str | None = None


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


@dataclass
class ResourceCreationLimitPolicy(PropertyType):
    new_game_sessions_per_creator: int | None = None
    policy_period_in_minutes: int | None = None


@dataclass
class RuntimeConfiguration(PropertyType):
    game_session_activation_timeout_seconds: int | None = None
    max_concurrent_game_session_activations: int | None = None
    server_processes: list[ServerProcess] = field(default_factory=list)


@dataclass
class ScalingPolicy(PropertyType):
    metric_name: str | None = None
    name: str | None = None
    comparison_operator: str | None = None
    evaluation_periods: int | None = None
    location: str | None = None
    policy_type: str | None = None
    scaling_adjustment: int | None = None
    scaling_adjustment_type: str | None = None
    status: str | None = None
    target_configuration: TargetConfiguration | None = None
    threshold: float | None = None
    update_status: str | None = None


@dataclass
class ServerProcess(PropertyType):
    concurrent_executions: int | None = None
    launch_path: str | None = None
    parameters: str | None = None


@dataclass
class TargetConfiguration(PropertyType):
    target_value: float | None = None
