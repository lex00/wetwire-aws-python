"""PropertyTypes for AWS::SageMaker::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Alarm(PropertyType):
    alarm_name: str | None = None


@dataclass
class AutoRollbackConfig(PropertyType):
    alarms: list[Alarm] = field(default_factory=list)


@dataclass
class BlueGreenUpdatePolicy(PropertyType):
    traffic_routing_configuration: TrafficRoutingConfig | None = None
    maximum_execution_timeout_in_seconds: int | None = None
    termination_wait_in_seconds: int | None = None


@dataclass
class CapacitySize(PropertyType):
    type_: str | None = None
    value: int | None = None


@dataclass
class DeploymentConfig(PropertyType):
    auto_rollback_configuration: AutoRollbackConfig | None = None
    blue_green_update_policy: BlueGreenUpdatePolicy | None = None
    rolling_update_policy: RollingUpdatePolicy | None = None


@dataclass
class RollingUpdatePolicy(PropertyType):
    maximum_batch_size: CapacitySize | None = None
    wait_interval_in_seconds: int | None = None
    maximum_execution_timeout_in_seconds: int | None = None
    rollback_maximum_batch_size: CapacitySize | None = None


@dataclass
class TrafficRoutingConfig(PropertyType):
    type_: str | None = None
    canary_size: CapacitySize | None = None
    linear_step_size: CapacitySize | None = None
    wait_interval_in_seconds: int | None = None


@dataclass
class VariantProperty(PropertyType):
    variant_property_type: str | None = None
