"""PropertyTypes for AWS::SageMaker::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AlarmDetails(PropertyType):
    alarm_name: str | None = None


@dataclass
class CapacitySizeConfig(PropertyType):
    type_: str | None = None
    value: int | None = None


@dataclass
class ClusterAutoScalingConfig(PropertyType):
    mode: str | None = None
    auto_scaler_type: str | None = None


@dataclass
class ClusterCapacityRequirements(PropertyType):
    on_demand: dict[str, Any] | None = None
    spot: dict[str, Any] | None = None


@dataclass
class ClusterEbsVolumeConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "volume_size_in_gb": "VolumeSizeInGB",
    }

    root_volume: bool | None = None
    volume_kms_key_id: str | None = None
    volume_size_in_gb: int | None = None


@dataclass
class ClusterInstanceGroup(PropertyType):
    execution_role: str | None = None
    instance_count: int | None = None
    instance_group_name: str | None = None
    instance_type: str | None = None
    life_cycle_config: ClusterLifeCycleConfig | None = None
    capacity_requirements: ClusterCapacityRequirements | None = None
    current_count: int | None = None
    image_id: str | None = None
    instance_storage_configs: list[ClusterInstanceStorageConfig] = field(
        default_factory=list
    )
    kubernetes_config: ClusterKubernetesConfig | None = None
    min_instance_count: int | None = None
    on_start_deep_health_checks: list[String] = field(default_factory=list)
    override_vpc_config: VpcConfig | None = None
    scheduled_update_config: ScheduledUpdateConfig | None = None
    threads_per_core: int | None = None
    training_plan_arn: str | None = None


@dataclass
class ClusterInstanceStorageConfig(PropertyType):
    ebs_volume_config: ClusterEbsVolumeConfig | None = None


@dataclass
class ClusterKubernetesConfig(PropertyType):
    labels: dict[str, String] = field(default_factory=dict)
    taints: list[ClusterKubernetesTaint] = field(default_factory=list)


@dataclass
class ClusterKubernetesTaint(PropertyType):
    effect: str | None = None
    key: str | None = None
    value: str | None = None


@dataclass
class ClusterLifeCycleConfig(PropertyType):
    on_create: str | None = None
    source_s3_uri: str | None = None


@dataclass
class ClusterOrchestratorEksConfig(PropertyType):
    cluster_arn: str | None = None


@dataclass
class ClusterRestrictedInstanceGroup(PropertyType):
    environment_config: EnvironmentConfig | None = None
    execution_role: str | None = None
    instance_count: int | None = None
    instance_group_name: str | None = None
    instance_type: str | None = None
    current_count: int | None = None
    instance_storage_configs: list[ClusterInstanceStorageConfig] = field(
        default_factory=list
    )
    on_start_deep_health_checks: list[String] = field(default_factory=list)
    override_vpc_config: VpcConfig | None = None
    threads_per_core: int | None = None
    training_plan_arn: str | None = None


@dataclass
class DeploymentConfig(PropertyType):
    auto_rollback_configuration: list[AlarmDetails] = field(default_factory=list)
    rolling_update_policy: RollingUpdatePolicy | None = None
    wait_interval_in_seconds: int | None = None


@dataclass
class EnvironmentConfig(PropertyType):
    f_sx_lustre_config: FSxLustreConfig | None = None


@dataclass
class FSxLustreConfig(PropertyType):
    per_unit_storage_throughput: int | None = None
    size_in_gi_b: int | None = None


@dataclass
class Orchestrator(PropertyType):
    eks: ClusterOrchestratorEksConfig | None = None


@dataclass
class RollingUpdatePolicy(PropertyType):
    maximum_batch_size: CapacitySizeConfig | None = None
    rollback_maximum_batch_size: CapacitySizeConfig | None = None


@dataclass
class ScheduledUpdateConfig(PropertyType):
    schedule_expression: str | None = None
    deployment_config: DeploymentConfig | None = None


@dataclass
class TieredStorageConfig(PropertyType):
    mode: str | None = None
    instance_memory_allocation_percentage: int | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
