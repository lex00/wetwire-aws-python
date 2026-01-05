"""PropertyTypes for AWS::AutoScaling::AutoScalingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AcceleratorCountRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class AcceleratorTotalMemoryMiBRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class AvailabilityZoneDistribution(PropertyType):
    capacity_distribution_strategy: str | None = None


@dataclass
class AvailabilityZoneImpairmentPolicy(PropertyType):
    impaired_zone_health_check_behavior: str | None = None
    zonal_shift_enabled: bool | None = None


@dataclass
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class BaselinePerformanceFactorsRequest(PropertyType):
    cpu: CpuPerformanceFactorRequest | None = None


@dataclass
class CapacityReservationSpecification(PropertyType):
    capacity_reservation_preference: str | None = None
    capacity_reservation_target: CapacityReservationTarget | None = None


@dataclass
class CapacityReservationTarget(PropertyType):
    capacity_reservation_ids: list[String] = field(default_factory=list)
    capacity_reservation_resource_group_arns: list[String] = field(default_factory=list)


@dataclass
class CpuPerformanceFactorRequest(PropertyType):
    references: list[PerformanceFactorReferenceRequest] = field(default_factory=list)


@dataclass
class InstanceLifecyclePolicy(PropertyType):
    retention_triggers: RetentionTriggers | None = None


@dataclass
class InstanceMaintenancePolicy(PropertyType):
    max_healthy_percentage: int | None = None
    min_healthy_percentage: int | None = None


@dataclass
class InstanceRequirements(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    memory_mi_b: MemoryMiBRequest | None = None
    v_cpu_count: VCpuCountRequest | None = None
    accelerator_count: AcceleratorCountRequest | None = None
    accelerator_manufacturers: list[String] = field(default_factory=list)
    accelerator_names: list[String] = field(default_factory=list)
    accelerator_total_memory_mi_b: AcceleratorTotalMemoryMiBRequest | None = None
    accelerator_types: list[String] = field(default_factory=list)
    allowed_instance_types: list[String] = field(default_factory=list)
    bare_metal: str | None = None
    baseline_ebs_bandwidth_mbps: BaselineEbsBandwidthMbpsRequest | None = None
    baseline_performance_factors: BaselinePerformanceFactorsRequest | None = None
    burstable_performance: str | None = None
    cpu_manufacturers: list[String] = field(default_factory=list)
    excluded_instance_types: list[String] = field(default_factory=list)
    instance_generations: list[String] = field(default_factory=list)
    local_storage: str | None = None
    local_storage_types: list[String] = field(default_factory=list)
    max_spot_price_as_percentage_of_optimal_on_demand_price: int | None = None
    memory_gi_b_per_v_cpu: MemoryGiBPerVCpuRequest | None = None
    network_bandwidth_gbps: NetworkBandwidthGbpsRequest | None = None
    network_interface_count: NetworkInterfaceCountRequest | None = None
    on_demand_max_price_percentage_over_lowest_price: int | None = None
    require_hibernate_support: bool | None = None
    spot_max_price_percentage_over_lowest_price: int | None = None
    total_local_storage_gb: TotalLocalStorageGBRequest | None = None


@dataclass
class InstancesDistribution(PropertyType):
    on_demand_allocation_strategy: str | None = None
    on_demand_base_capacity: int | None = None
    on_demand_percentage_above_base_capacity: int | None = None
    spot_allocation_strategy: str | None = None
    spot_instance_pools: int | None = None
    spot_max_price: str | None = None


@dataclass
class LaunchTemplate(PropertyType):
    launch_template_specification: LaunchTemplateSpecification | None = None
    overrides: list[LaunchTemplateOverrides] = field(default_factory=list)


@dataclass
class LaunchTemplateOverrides(PropertyType):
    image_id: str | None = None
    instance_requirements: InstanceRequirements | None = None
    instance_type: str | None = None
    launch_template_specification: LaunchTemplateSpecification | None = None
    weighted_capacity: str | None = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
    version: str | None = None
    launch_template_id: str | None = None
    launch_template_name: str | None = None


@dataclass
class LifecycleHookSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "notification_target_arn": "NotificationTargetARN",
        "role_arn": "RoleARN",
    }

    lifecycle_hook_name: str | None = None
    lifecycle_transition: str | None = None
    default_result: str | None = None
    heartbeat_timeout: int | None = None
    notification_metadata: str | None = None
    notification_target_arn: str | None = None
    role_arn: str | None = None


@dataclass
class MemoryGiBPerVCpuRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class MemoryMiBRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class MetricsCollection(PropertyType):
    granularity: str | None = None
    metrics: list[String] = field(default_factory=list)


@dataclass
class MixedInstancesPolicy(PropertyType):
    launch_template: LaunchTemplate | None = None
    instances_distribution: InstancesDistribution | None = None


@dataclass
class NetworkBandwidthGbpsRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class NetworkInterfaceCountRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicARN",
    }

    topic_arn: list[String] = field(default_factory=list)
    notification_types: list[String] = field(default_factory=list)


@dataclass
class PerformanceFactorReferenceRequest(PropertyType):
    instance_family: str | None = None


@dataclass
class RetentionTriggers(PropertyType):
    terminate_hook_abandon: str | None = None


@dataclass
class TagProperty(PropertyType):
    key: str | None = None
    propagate_at_launch: bool | None = None
    value: str | None = None


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class TrafficSourceIdentifier(PropertyType):
    identifier: str | None = None
    type_: str | None = None


@dataclass
class VCpuCountRequest(PropertyType):
    max: int | None = None
    min: int | None = None
