"""PropertyTypes for AWS::SageMaker::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AlarmDetails(PropertyType):
    alarm_name: DslValue[str] | None = None


@dataclass
class CapacitySizeConfig(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class ClusterAutoScalingConfig(PropertyType):
    mode: DslValue[str] | None = None
    auto_scaler_type: DslValue[str] | None = None


@dataclass
class ClusterCapacityRequirements(PropertyType):
    on_demand: DslValue[dict[str, Any]] | None = None
    spot: DslValue[dict[str, Any]] | None = None


@dataclass
class ClusterEbsVolumeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_size_in_gb": "VolumeSizeInGB",
    }

    root_volume: DslValue[bool] | None = None
    volume_kms_key_id: DslValue[str] | None = None
    volume_size_in_gb: DslValue[int] | None = None


@dataclass
class ClusterInstanceGroup(PropertyType):
    execution_role: DslValue[str] | None = None
    instance_count: DslValue[int] | None = None
    instance_group_name: DslValue[str] | None = None
    instance_type: DslValue[str] | None = None
    life_cycle_config: DslValue[ClusterLifeCycleConfig] | None = None
    capacity_requirements: DslValue[ClusterCapacityRequirements] | None = None
    current_count: DslValue[int] | None = None
    image_id: DslValue[str] | None = None
    instance_storage_configs: list[DslValue[ClusterInstanceStorageConfig]] = field(
        default_factory=list
    )
    kubernetes_config: DslValue[ClusterKubernetesConfig] | None = None
    min_instance_count: DslValue[int] | None = None
    on_start_deep_health_checks: list[DslValue[str]] = field(default_factory=list)
    override_vpc_config: DslValue[VpcConfig] | None = None
    scheduled_update_config: DslValue[ScheduledUpdateConfig] | None = None
    threads_per_core: DslValue[int] | None = None
    training_plan_arn: DslValue[str] | None = None


@dataclass
class ClusterInstanceStorageConfig(PropertyType):
    ebs_volume_config: DslValue[ClusterEbsVolumeConfig] | None = None


@dataclass
class ClusterKubernetesConfig(PropertyType):
    labels: dict[str, DslValue[str]] = field(default_factory=dict)
    taints: list[DslValue[ClusterKubernetesTaint]] = field(default_factory=list)


@dataclass
class ClusterKubernetesTaint(PropertyType):
    effect: DslValue[str] | None = None
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ClusterLifeCycleConfig(PropertyType):
    on_create: DslValue[str] | None = None
    source_s3_uri: DslValue[str] | None = None


@dataclass
class ClusterOrchestratorEksConfig(PropertyType):
    cluster_arn: DslValue[str] | None = None


@dataclass
class ClusterRestrictedInstanceGroup(PropertyType):
    environment_config: DslValue[EnvironmentConfig] | None = None
    execution_role: DslValue[str] | None = None
    instance_count: DslValue[int] | None = None
    instance_group_name: DslValue[str] | None = None
    instance_type: DslValue[str] | None = None
    current_count: DslValue[int] | None = None
    instance_storage_configs: list[DslValue[ClusterInstanceStorageConfig]] = field(
        default_factory=list
    )
    on_start_deep_health_checks: list[DslValue[str]] = field(default_factory=list)
    override_vpc_config: DslValue[VpcConfig] | None = None
    threads_per_core: DslValue[int] | None = None
    training_plan_arn: DslValue[str] | None = None


@dataclass
class DeploymentConfig(PropertyType):
    auto_rollback_configuration: list[DslValue[AlarmDetails]] = field(
        default_factory=list
    )
    rolling_update_policy: DslValue[RollingUpdatePolicy] | None = None
    wait_interval_in_seconds: DslValue[int] | None = None


@dataclass
class EnvironmentConfig(PropertyType):
    f_sx_lustre_config: DslValue[FSxLustreConfig] | None = None


@dataclass
class FSxLustreConfig(PropertyType):
    per_unit_storage_throughput: DslValue[int] | None = None
    size_in_gi_b: DslValue[int] | None = None


@dataclass
class Orchestrator(PropertyType):
    eks: DslValue[ClusterOrchestratorEksConfig] | None = None


@dataclass
class RollingUpdatePolicy(PropertyType):
    maximum_batch_size: DslValue[CapacitySizeConfig] | None = None
    rollback_maximum_batch_size: DslValue[CapacitySizeConfig] | None = None


@dataclass
class ScheduledUpdateConfig(PropertyType):
    schedule_expression: DslValue[str] | None = None
    deployment_config: DslValue[DeploymentConfig] | None = None


@dataclass
class TieredStorageConfig(PropertyType):
    mode: DslValue[str] | None = None
    instance_memory_allocation_percentage: DslValue[int] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
