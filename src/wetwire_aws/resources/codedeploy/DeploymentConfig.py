"""PropertyTypes for AWS::CodeDeploy::DeploymentConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MinimumHealthyHosts(PropertyType):
    type_: str | None = None
    value: int | None = None


@dataclass
class MinimumHealthyHostsPerZone(PropertyType):
    type_: str | None = None
    value: int | None = None


@dataclass
class TimeBasedCanary(PropertyType):
    canary_interval: int | None = None
    canary_percentage: int | None = None


@dataclass
class TimeBasedLinear(PropertyType):
    linear_interval: int | None = None
    linear_percentage: int | None = None


@dataclass
class TrafficRoutingConfig(PropertyType):
    type_: str | None = None
    time_based_canary: TimeBasedCanary | None = None
    time_based_linear: TimeBasedLinear | None = None


@dataclass
class ZonalConfig(PropertyType):
    first_zone_monitor_duration_in_seconds: int | None = None
    minimum_healthy_hosts_per_zone: MinimumHealthyHostsPerZone | None = None
    monitor_duration_in_seconds: int | None = None
