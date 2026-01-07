"""PropertyTypes for AWS::EKS::Nodegroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class LaunchTemplateSpecification(PropertyType):
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class NodeRepairConfig(PropertyType):
    enabled: DslValue[bool] | None = None
    max_parallel_nodes_repaired_count: DslValue[int] | None = None
    max_parallel_nodes_repaired_percentage: DslValue[int] | None = None
    max_unhealthy_node_threshold_count: DslValue[int] | None = None
    max_unhealthy_node_threshold_percentage: DslValue[int] | None = None
    node_repair_config_overrides: list[DslValue[NodeRepairConfigOverrides]] = field(
        default_factory=list
    )


@dataclass
class NodeRepairConfigOverrides(PropertyType):
    min_repair_wait_time_mins: DslValue[int] | None = None
    node_monitoring_condition: DslValue[str] | None = None
    node_unhealthy_reason: DslValue[str] | None = None
    repair_action: DslValue[str] | None = None


@dataclass
class RemoteAccess(PropertyType):
    ec2_ssh_key: DslValue[str] | None = None
    source_security_groups: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ScalingConfig(PropertyType):
    desired_size: DslValue[int] | None = None
    max_size: DslValue[int] | None = None
    min_size: DslValue[int] | None = None


@dataclass
class Taint(PropertyType):
    effect: DslValue[str] | None = None
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class UpdateConfig(PropertyType):
    max_unavailable: DslValue[float] | None = None
    max_unavailable_percentage: DslValue[float] | None = None
    update_strategy: DslValue[str] | None = None
