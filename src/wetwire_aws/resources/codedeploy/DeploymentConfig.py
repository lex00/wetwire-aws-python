"""PropertyTypes for AWS::CodeDeploy::DeploymentConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MinimumHealthyHosts(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class MinimumHealthyHostsPerZone(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class TimeBasedCanary(PropertyType):
    canary_interval: DslValue[int] | None = None
    canary_percentage: DslValue[int] | None = None


@dataclass
class TimeBasedLinear(PropertyType):
    linear_interval: DslValue[int] | None = None
    linear_percentage: DslValue[int] | None = None


@dataclass
class TrafficRoutingConfig(PropertyType):
    type_: DslValue[str] | None = None
    time_based_canary: DslValue[TimeBasedCanary] | None = None
    time_based_linear: DslValue[TimeBasedLinear] | None = None


@dataclass
class ZonalConfig(PropertyType):
    first_zone_monitor_duration_in_seconds: DslValue[int] | None = None
    minimum_healthy_hosts_per_zone: DslValue[MinimumHealthyHostsPerZone] | None = None
    monitor_duration_in_seconds: DslValue[int] | None = None
