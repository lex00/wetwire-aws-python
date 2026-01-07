"""PropertyTypes for AWS::GameLift::Fleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AnywhereConfiguration(PropertyType):
    cost: DslValue[str] | None = None


@dataclass
class CertificateConfiguration(PropertyType):
    certificate_type: DslValue[str] | None = None


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


@dataclass
class ResourceCreationLimitPolicy(PropertyType):
    new_game_sessions_per_creator: DslValue[int] | None = None
    policy_period_in_minutes: DslValue[int] | None = None


@dataclass
class RuntimeConfiguration(PropertyType):
    game_session_activation_timeout_seconds: DslValue[int] | None = None
    max_concurrent_game_session_activations: DslValue[int] | None = None
    server_processes: list[DslValue[ServerProcess]] = field(default_factory=list)


@dataclass
class ScalingPolicy(PropertyType):
    metric_name: DslValue[str] | None = None
    name: DslValue[str] | None = None
    comparison_operator: DslValue[str] | None = None
    evaluation_periods: DslValue[int] | None = None
    location: DslValue[str] | None = None
    policy_type: DslValue[str] | None = None
    scaling_adjustment: DslValue[int] | None = None
    scaling_adjustment_type: DslValue[str] | None = None
    status: DslValue[str] | None = None
    target_configuration: DslValue[TargetConfiguration] | None = None
    threshold: DslValue[float] | None = None
    update_status: DslValue[str] | None = None


@dataclass
class ServerProcess(PropertyType):
    concurrent_executions: DslValue[int] | None = None
    launch_path: DslValue[str] | None = None
    parameters: DslValue[str] | None = None


@dataclass
class TargetConfiguration(PropertyType):
    target_value: DslValue[float] | None = None
