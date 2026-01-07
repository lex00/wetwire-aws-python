"""PropertyTypes for AWS::OpsWorks::Layer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoScalingThresholds(PropertyType):
    cpu_threshold: DslValue[float] | None = None
    ignore_metrics_time: DslValue[int] | None = None
    instance_count: DslValue[int] | None = None
    load_threshold: DslValue[float] | None = None
    memory_threshold: DslValue[float] | None = None
    thresholds_wait_time: DslValue[int] | None = None


@dataclass
class LifecycleEventConfiguration(PropertyType):
    shutdown_event_configuration: DslValue[ShutdownEventConfiguration] | None = None


@dataclass
class LoadBasedAutoScaling(PropertyType):
    down_scaling: DslValue[AutoScalingThresholds] | None = None
    enable: DslValue[bool] | None = None
    up_scaling: DslValue[AutoScalingThresholds] | None = None


@dataclass
class Recipes(PropertyType):
    configure: list[DslValue[str]] = field(default_factory=list)
    deploy: list[DslValue[str]] = field(default_factory=list)
    setup: list[DslValue[str]] = field(default_factory=list)
    shutdown: list[DslValue[str]] = field(default_factory=list)
    undeploy: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ShutdownEventConfiguration(PropertyType):
    delay_until_elb_connections_drained: DslValue[bool] | None = None
    execution_timeout: DslValue[int] | None = None


@dataclass
class VolumeConfiguration(PropertyType):
    encrypted: DslValue[bool] | None = None
    iops: DslValue[int] | None = None
    mount_point: DslValue[str] | None = None
    number_of_disks: DslValue[int] | None = None
    raid_level: DslValue[int] | None = None
    size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None
