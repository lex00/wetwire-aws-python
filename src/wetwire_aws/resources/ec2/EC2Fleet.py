"""PropertyTypes for AWS::EC2::EC2Fleet."""

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
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class BaselinePerformanceFactorsRequest(PropertyType):
    cpu: DslValue[CpuPerformanceFactorRequest] | None = None


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: DslValue[str] | None = None
    ebs: DslValue[EbsBlockDevice] | None = None
    no_device: DslValue[str] | None = None
    virtual_name: DslValue[str] | None = None


@dataclass
class CapacityRebalance(PropertyType):
    replacement_strategy: DslValue[str] | None = None
    termination_delay: DslValue[int] | None = None


@dataclass
class CapacityReservationOptionsRequest(PropertyType):
    usage_strategy: DslValue[str] | None = None


@dataclass
class CpuPerformanceFactorRequest(PropertyType):
    references: list[DslValue[PerformanceFactorReferenceRequest]] = field(
        default_factory=list
    )


@dataclass
class EbsBlockDevice(PropertyType):
    delete_on_termination: DslValue[bool] | None = None
    encrypted: DslValue[bool] | None = None
    iops: DslValue[int] | None = None
    kms_key_id: DslValue[str] | None = None
    snapshot_id: DslValue[str] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class FleetLaunchTemplateConfigRequest(PropertyType):
    launch_template_specification: (
        DslValue[FleetLaunchTemplateSpecificationRequest] | None
    ) = None
    overrides: list[DslValue[FleetLaunchTemplateOverridesRequest]] = field(
        default_factory=list
    )


@dataclass
class FleetLaunchTemplateOverridesRequest(PropertyType):
    availability_zone: DslValue[str] | None = None
    availability_zone_id: DslValue[str] | None = None
    block_device_mappings: list[DslValue[BlockDeviceMapping]] = field(
        default_factory=list
    )
    instance_requirements: DslValue[InstanceRequirementsRequest] | None = None
    instance_type: DslValue[str] | None = None
    max_price: DslValue[str] | None = None
    placement: DslValue[Placement] | None = None
    priority: DslValue[float] | None = None
    subnet_id: DslValue[str] | None = None
    weighted_capacity: DslValue[float] | None = None


@dataclass
class FleetLaunchTemplateSpecificationRequest(PropertyType):
    version: DslValue[str] | None = None
    launch_template_id: DslValue[str] | None = None
    launch_template_name: DslValue[str] | None = None


@dataclass
class InstanceRequirementsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

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
    memory_mi_b: DslValue[MemoryMiBRequest] | None = None
    network_bandwidth_gbps: DslValue[NetworkBandwidthGbpsRequest] | None = None
    network_interface_count: DslValue[NetworkInterfaceCountRequest] | None = None
    on_demand_max_price_percentage_over_lowest_price: DslValue[int] | None = None
    require_encryption_in_transit: DslValue[bool] | None = None
    require_hibernate_support: DslValue[bool] | None = None
    spot_max_price_percentage_over_lowest_price: DslValue[int] | None = None
    total_local_storage_gb: DslValue[TotalLocalStorageGBRequest] | None = None
    v_cpu_count: DslValue[VCpuCountRangeRequest] | None = None


@dataclass
class MaintenanceStrategies(PropertyType):
    capacity_rebalance: DslValue[CapacityRebalance] | None = None


@dataclass
class MemoryGiBPerVCpuRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class MemoryMiBRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class NetworkBandwidthGbpsRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class NetworkInterfaceCountRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class OnDemandOptionsRequest(PropertyType):
    allocation_strategy: DslValue[str] | None = None
    capacity_reservation_options: DslValue[CapacityReservationOptionsRequest] | None = (
        None
    )
    max_total_price: DslValue[str] | None = None
    min_target_capacity: DslValue[int] | None = None
    single_availability_zone: DslValue[bool] | None = None
    single_instance_type: DslValue[bool] | None = None


@dataclass
class PerformanceFactorReferenceRequest(PropertyType):
    instance_family: DslValue[str] | None = None


@dataclass
class Placement(PropertyType):
    affinity: DslValue[str] | None = None
    availability_zone: DslValue[str] | None = None
    group_name: DslValue[str] | None = None
    host_id: DslValue[str] | None = None
    host_resource_group_arn: DslValue[str] | None = None
    partition_number: DslValue[int] | None = None
    spread_domain: DslValue[str] | None = None
    tenancy: DslValue[str] | None = None


@dataclass
class SpotOptionsRequest(PropertyType):
    allocation_strategy: DslValue[str] | None = None
    instance_interruption_behavior: DslValue[str] | None = None
    instance_pools_to_use_count: DslValue[int] | None = None
    maintenance_strategies: DslValue[MaintenanceStrategies] | None = None
    max_total_price: DslValue[str] | None = None
    min_target_capacity: DslValue[int] | None = None
    single_availability_zone: DslValue[bool] | None = None
    single_instance_type: DslValue[bool] | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class TargetCapacitySpecificationRequest(PropertyType):
    total_target_capacity: DslValue[int] | None = None
    default_target_capacity_type: DslValue[str] | None = None
    on_demand_target_capacity: DslValue[int] | None = None
    spot_target_capacity: DslValue[int] | None = None
    target_capacity_unit_type: DslValue[str] | None = None


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class VCpuCountRangeRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None
