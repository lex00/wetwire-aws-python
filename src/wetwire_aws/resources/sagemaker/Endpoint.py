"""PropertyTypes for AWS::SageMaker::Endpoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Alarm(PropertyType):
    alarm_name: DslValue[str] | None = None


@dataclass
class AutoRollbackConfig(PropertyType):
    alarms: list[DslValue[Alarm]] = field(default_factory=list)


@dataclass
class BlueGreenUpdatePolicy(PropertyType):
    traffic_routing_configuration: DslValue[TrafficRoutingConfig] | None = None
    maximum_execution_timeout_in_seconds: DslValue[int] | None = None
    termination_wait_in_seconds: DslValue[int] | None = None


@dataclass
class CapacitySize(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class DeploymentConfig(PropertyType):
    auto_rollback_configuration: DslValue[AutoRollbackConfig] | None = None
    blue_green_update_policy: DslValue[BlueGreenUpdatePolicy] | None = None
    rolling_update_policy: DslValue[RollingUpdatePolicy] | None = None


@dataclass
class RollingUpdatePolicy(PropertyType):
    maximum_batch_size: DslValue[CapacitySize] | None = None
    wait_interval_in_seconds: DslValue[int] | None = None
    maximum_execution_timeout_in_seconds: DslValue[int] | None = None
    rollback_maximum_batch_size: DslValue[CapacitySize] | None = None


@dataclass
class TrafficRoutingConfig(PropertyType):
    type_: DslValue[str] | None = None
    canary_size: DslValue[CapacitySize] | None = None
    linear_step_size: DslValue[CapacitySize] | None = None
    wait_interval_in_seconds: DslValue[int] | None = None


@dataclass
class VariantProperty(PropertyType):
    variant_property_type: DslValue[str] | None = None
