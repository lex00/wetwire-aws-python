"""PropertyTypes for AWS::ECS::CapacityProvider."""

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
class AutoScalingGroupProvider(PropertyType):
    auto_scaling_group_arn: str | None = None
    managed_draining: str | None = None
    managed_scaling: ManagedScaling | None = None
    managed_termination_protection: str | None = None


@dataclass
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class InfrastructureOptimization(PropertyType):
    scale_in_after: int | None = None


@dataclass
class InstanceLaunchTemplate(PropertyType):
    ec2_instance_profile_arn: str | None = None
    network_configuration: ManagedInstancesNetworkConfiguration | None = None
    capacity_option_type: str | None = None
    instance_requirements: InstanceRequirementsRequest | None = None
    monitoring: str | None = None
    storage_configuration: ManagedInstancesStorageConfiguration | None = None


@dataclass
class InstanceRequirementsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    memory_mi_b: MemoryMiBRequest | None = None
    v_cpu_count: VCpuCountRangeRequest | None = None
    accelerator_count: AcceleratorCountRequest | None = None
    accelerator_manufacturers: list[String] = field(default_factory=list)
    accelerator_names: list[String] = field(default_factory=list)
    accelerator_total_memory_mi_b: AcceleratorTotalMemoryMiBRequest | None = None
    accelerator_types: list[String] = field(default_factory=list)
    allowed_instance_types: list[String] = field(default_factory=list)
    bare_metal: str | None = None
    baseline_ebs_bandwidth_mbps: BaselineEbsBandwidthMbpsRequest | None = None
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
class ManagedInstancesNetworkConfiguration(PropertyType):
    subnets: list[String] = field(default_factory=list)
    security_groups: list[String] = field(default_factory=list)


@dataclass
class ManagedInstancesProvider(PropertyType):
    infrastructure_role_arn: str | None = None
    instance_launch_template: InstanceLaunchTemplate | None = None
    infrastructure_optimization: InfrastructureOptimization | None = None
    propagate_tags: str | None = None


@dataclass
class ManagedInstancesStorageConfiguration(PropertyType):
    storage_size_gi_b: int | None = None


@dataclass
class ManagedScaling(PropertyType):
    instance_warmup_period: int | None = None
    maximum_scaling_step_size: int | None = None
    minimum_scaling_step_size: int | None = None
    status: str | None = None
    target_capacity: int | None = None


@dataclass
class MemoryGiBPerVCpuRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class MemoryMiBRequest(PropertyType):
    min: int | None = None
    max: int | None = None


@dataclass
class NetworkBandwidthGbpsRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class NetworkInterfaceCountRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class VCpuCountRangeRequest(PropertyType):
    min: int | None = None
    max: int | None = None
