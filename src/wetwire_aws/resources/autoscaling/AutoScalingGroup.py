"""PropertyTypes for AWS::AutoScaling::AutoScalingGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AcceleratorCountRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class AcceleratorTotalMemoryMiBRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class AvailabilityZoneDistribution(PropertyType):
    capacity_distribution_strategy: DslValue[str] | None = None


@dataclass
class AvailabilityZoneImpairmentPolicy(PropertyType):
    impaired_zone_health_check_behavior: DslValue[str] | None = None
    zonal_shift_enabled: DslValue[bool] | None = None


@dataclass
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class BaselinePerformanceFactorsRequest(PropertyType):
    cpu: DslValue[CpuPerformanceFactorRequest] | None = None


@dataclass
class CapacityReservationSpecification(PropertyType):
    capacity_reservation_preference: DslValue[str] | None = None
    capacity_reservation_target: DslValue[CapacityReservationTarget] | None = None


@dataclass
class CapacityReservationTarget(PropertyType):
    capacity_reservation_ids: list[DslValue[str]] = field(default_factory=list)
    capacity_reservation_resource_group_arns: list[DslValue[str]] = field(
        default_factory=list
    )


@dataclass
class CpuPerformanceFactorRequest(PropertyType):
    references: list[DslValue[PerformanceFactorReferenceRequest]] = field(
        default_factory=list
    )


@dataclass
class InstanceLifecyclePolicy(PropertyType):
    retention_triggers: DslValue[RetentionTriggers] | None = None


@dataclass
class InstanceMaintenancePolicy(PropertyType):
    max_healthy_percentage: DslValue[int] | None = None
    min_healthy_percentage: DslValue[int] | None = None


@dataclass
class InstanceRequirements(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    memory_mi_b: DslValue[MemoryMiBRequest] | None = None
    v_cpu_count: DslValue[VCpuCountRequest] | None = None
    accelerator_count: DslValue[AcceleratorCountRequest] | None = None
    accelerator_manufacturers: list[DslValue[str]] = field(default_factory=list)
    accelerator_names: list[DslValue[str]] = field(default_factory=list)
    accelerator_total_memory_mi_b: DslValue[AcceleratorTotalMemoryMiBRequest] | None = (
        None
    )
    accelerator_types: list[DslValue[str]] = field(default_factory=list)
    allowed_instance_types: list[DslValue[str]] = field(default_factory=list)
    bare_metal: DslValue[str] | None = None
    baseline_ebs_bandwidth_mbps: DslValue[BaselineEbsBandwidthMbpsRequest] | None = None
    baseline_performance_factors: DslValue[BaselinePerformanceFactorsRequest] | None = (
        None
    )
    burstable_performance: DslValue[str] | None = None
    cpu_manufacturers: list[DslValue[str]] = field(default_factory=list)
    excluded_instance_types: list[DslValue[str]] = field(default_factory=list)
    instance_generations: list[DslValue[str]] = field(default_factory=list)
    local_storage: DslValue[str] | None = None
    local_storage_types: list[DslValue[str]] = field(default_factory=list)
    max_spot_price_as_percentage_of_optimal_on_demand_price: DslValue[int] | None = None
    memory_gi_b_per_v_cpu: DslValue[MemoryGiBPerVCpuRequest] | None = None
    network_bandwidth_gbps: DslValue[NetworkBandwidthGbpsRequest] | None = None
    network_interface_count: DslValue[NetworkInterfaceCountRequest] | None = None
    on_demand_max_price_percentage_over_lowest_price: DslValue[int] | None = None
    require_hibernate_support: DslValue[bool] | None = None
    spot_max_price_percentage_over_lowest_price: DslValue[int] | None = None
    total_local_storage_gb: DslValue[TotalLocalStorageGBRequest] | None = None


@dataclass
class InstancesDistribution(PropertyType):
    on_demand_allocation_strategy: DslValue[str] | None = None
    on_demand_base_capacity: DslValue[int] | None = None
    on_demand_percentage_above_base_capacity: DslValue[int] | None = None
    spot_allocation_strategy: DslValue[str] | None = None
    spot_instance_pools: DslValue[int] | None = None
    spot_max_price: DslValue[str] | None = None


@dataclass
class LaunchTemplate(PropertyType):
    launch_template_specification: DslValue[LaunchTemplateSpecification] | None = None
    overrides: list[DslValue[LaunchTemplateOverrides]] = field(default_factory=list)


@dataclass
class LaunchTemplateOverrides(PropertyType):
    image_id: DslValue[str] | None = None
    instance_requirements: DslValue[InstanceRequirements] | None = None
    instance_type: DslValue[str] | None = None
    launch_template_specification: DslValue[LaunchTemplateSpecification] | None = None
    weighted_capacity: DslValue[str] | None = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
    version: DslValue[str] | None = None
    launch_template_id: DslValue[str] | None = None
    launch_template_name: DslValue[str] | None = None


@dataclass
class LifecycleHookSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "notification_target_arn": "NotificationTargetARN",
        "role_arn": "RoleARN",
    }

    lifecycle_hook_name: DslValue[str] | None = None
    lifecycle_transition: DslValue[str] | None = None
    default_result: DslValue[str] | None = None
    heartbeat_timeout: DslValue[int] | None = None
    notification_metadata: DslValue[str] | None = None
    notification_target_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class MemoryGiBPerVCpuRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class MemoryMiBRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class MetricsCollection(PropertyType):
    granularity: DslValue[str] | None = None
    metrics: list[DslValue[str]] = field(default_factory=list)


@dataclass
class MixedInstancesPolicy(PropertyType):
    launch_template: DslValue[LaunchTemplate] | None = None
    instances_distribution: DslValue[InstancesDistribution] | None = None


@dataclass
class NetworkBandwidthGbpsRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class NetworkInterfaceCountRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "topic_arn": "TopicARN",
    }

    topic_arn: list[DslValue[str]] = field(default_factory=list)
    notification_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PerformanceFactorReferenceRequest(PropertyType):
    instance_family: DslValue[str] | None = None


@dataclass
class RetentionTriggers(PropertyType):
    terminate_hook_abandon: DslValue[str] | None = None


@dataclass
class TagProperty(PropertyType):
    key: DslValue[str] | None = None
    propagate_at_launch: DslValue[bool] | None = None
    value: DslValue[str] | None = None


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class TrafficSourceIdentifier(PropertyType):
    identifier: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class VCpuCountRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None
