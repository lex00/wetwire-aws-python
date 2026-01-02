"""PropertyTypes for AWS::OpsWorks::Layer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoScalingThresholds(PropertyType):
    cpu_threshold: float | None = None
    ignore_metrics_time: int | None = None
    instance_count: int | None = None
    load_threshold: float | None = None
    memory_threshold: float | None = None
    thresholds_wait_time: int | None = None


@dataclass
class LifecycleEventConfiguration(PropertyType):
    shutdown_event_configuration: ShutdownEventConfiguration | None = None


@dataclass
class LoadBasedAutoScaling(PropertyType):
    down_scaling: AutoScalingThresholds | None = None
    enable: bool | None = None
    up_scaling: AutoScalingThresholds | None = None


@dataclass
class Recipes(PropertyType):
    configure: list[String] = field(default_factory=list)
    deploy: list[String] = field(default_factory=list)
    setup: list[String] = field(default_factory=list)
    shutdown: list[String] = field(default_factory=list)
    undeploy: list[String] = field(default_factory=list)


@dataclass
class ShutdownEventConfiguration(PropertyType):
    delay_until_elb_connections_drained: bool | None = None
    execution_timeout: int | None = None


@dataclass
class VolumeConfiguration(PropertyType):
    encrypted: bool | None = None
    iops: int | None = None
    mount_point: str | None = None
    number_of_disks: int | None = None
    raid_level: int | None = None
    size: int | None = None
    volume_type: str | None = None
