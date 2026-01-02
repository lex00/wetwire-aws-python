"""PropertyTypes for AWS::EKS::Nodegroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class LaunchTemplateSpecification(PropertyType):
    id: str | None = None
    name: str | None = None
    version: str | None = None


@dataclass
class NodeRepairConfig(PropertyType):
    enabled: bool | None = None
    max_parallel_nodes_repaired_count: int | None = None
    max_parallel_nodes_repaired_percentage: int | None = None
    max_unhealthy_node_threshold_count: int | None = None
    max_unhealthy_node_threshold_percentage: int | None = None
    node_repair_config_overrides: list[NodeRepairConfigOverrides] = field(
        default_factory=list
    )


@dataclass
class NodeRepairConfigOverrides(PropertyType):
    min_repair_wait_time_mins: int | None = None
    node_monitoring_condition: str | None = None
    node_unhealthy_reason: str | None = None
    repair_action: str | None = None


@dataclass
class RemoteAccess(PropertyType):
    ec2_ssh_key: str | None = None
    source_security_groups: list[String] = field(default_factory=list)


@dataclass
class ScalingConfig(PropertyType):
    desired_size: int | None = None
    max_size: int | None = None
    min_size: int | None = None


@dataclass
class Taint(PropertyType):
    effect: str | None = None
    key: str | None = None
    value: str | None = None


@dataclass
class UpdateConfig(PropertyType):
    max_unavailable: float | None = None
    max_unavailable_percentage: float | None = None
    update_strategy: str | None = None
