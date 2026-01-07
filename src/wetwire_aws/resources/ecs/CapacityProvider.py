"""PropertyTypes for AWS::ECS::CapacityProvider."""

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
class AutoScalingGroupProvider(PropertyType):
    auto_scaling_group_arn: DslValue[str] | None = None
    managed_draining: DslValue[str] | None = None
    managed_scaling: DslValue[ManagedScaling] | None = None
    managed_termination_protection: DslValue[str] | None = None


@dataclass
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class InfrastructureOptimization(PropertyType):
    scale_in_after: DslValue[int] | None = None


@dataclass
class InstanceLaunchTemplate(PropertyType):
    ec2_instance_profile_arn: DslValue[str] | None = None
    network_configuration: DslValue[ManagedInstancesNetworkConfiguration] | None = None
    capacity_option_type: DslValue[str] | None = None
    instance_requirements: DslValue[InstanceRequirementsRequest] | None = None
    monitoring: DslValue[str] | None = None
    storage_configuration: DslValue[ManagedInstancesStorageConfiguration] | None = None


@dataclass
class InstanceRequirementsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    memory_mi_b: DslValue[MemoryMiBRequest] | None = None
    v_cpu_count: DslValue[VCpuCountRangeRequest] | None = None
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
class ManagedInstancesNetworkConfiguration(PropertyType):
    subnets: list[DslValue[str]] = field(default_factory=list)
    security_groups: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ManagedInstancesProvider(PropertyType):
    infrastructure_role_arn: DslValue[str] | None = None
    instance_launch_template: DslValue[InstanceLaunchTemplate] | None = None
    infrastructure_optimization: DslValue[InfrastructureOptimization] | None = None
    propagate_tags: DslValue[str] | None = None


@dataclass
class ManagedInstancesStorageConfiguration(PropertyType):
    storage_size_gi_b: DslValue[int] | None = None


@dataclass
class ManagedScaling(PropertyType):
    instance_warmup_period: DslValue[int] | None = None
    maximum_scaling_step_size: DslValue[int] | None = None
    minimum_scaling_step_size: DslValue[int] | None = None
    status: DslValue[str] | None = None
    target_capacity: DslValue[int] | None = None


@dataclass
class MemoryGiBPerVCpuRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class MemoryMiBRequest(PropertyType):
    min: DslValue[int] | None = None
    max: DslValue[int] | None = None


@dataclass
class NetworkBandwidthGbpsRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class NetworkInterfaceCountRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class VCpuCountRangeRequest(PropertyType):
    min: DslValue[int] | None = None
    max: DslValue[int] | None = None
