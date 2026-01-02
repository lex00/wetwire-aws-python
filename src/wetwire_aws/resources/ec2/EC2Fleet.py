"""PropertyTypes for AWS::EC2::EC2Fleet."""

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
class BaselineEbsBandwidthMbpsRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class BaselinePerformanceFactorsRequest(PropertyType):
    cpu: CpuPerformanceFactorRequest | None = None


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: str | None = None
    ebs: EbsBlockDevice | None = None
    no_device: str | None = None
    virtual_name: str | None = None


@dataclass
class CapacityRebalance(PropertyType):
    replacement_strategy: str | None = None
    termination_delay: int | None = None


@dataclass
class CapacityReservationOptionsRequest(PropertyType):
    usage_strategy: str | None = None


@dataclass
class CpuPerformanceFactorRequest(PropertyType):
    references: list[PerformanceFactorReferenceRequest] = field(default_factory=list)


@dataclass
class EbsBlockDevice(PropertyType):
    delete_on_termination: bool | None = None
    encrypted: bool | None = None
    iops: int | None = None
    kms_key_id: str | None = None
    snapshot_id: str | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class FleetLaunchTemplateConfigRequest(PropertyType):
    launch_template_specification: FleetLaunchTemplateSpecificationRequest | None = None
    overrides: list[FleetLaunchTemplateOverridesRequest] = field(default_factory=list)


@dataclass
class FleetLaunchTemplateOverridesRequest(PropertyType):
    availability_zone: str | None = None
    block_device_mappings: list[BlockDeviceMapping] = field(default_factory=list)
    instance_requirements: InstanceRequirementsRequest | None = None
    instance_type: str | None = None
    max_price: str | None = None
    placement: Placement | None = None
    priority: float | None = None
    subnet_id: str | None = None
    weighted_capacity: float | None = None


@dataclass
class FleetLaunchTemplateSpecificationRequest(PropertyType):
    version: str | None = None
    launch_template_id: str | None = None
    launch_template_name: str | None = None


@dataclass
class InstanceRequirementsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

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
    memory_mi_b: MemoryMiBRequest | None = None
    network_bandwidth_gbps: NetworkBandwidthGbpsRequest | None = None
    network_interface_count: NetworkInterfaceCountRequest | None = None
    on_demand_max_price_percentage_over_lowest_price: int | None = None
    require_encryption_in_transit: bool | None = None
    require_hibernate_support: bool | None = None
    spot_max_price_percentage_over_lowest_price: int | None = None
    total_local_storage_gb: TotalLocalStorageGBRequest | None = None
    v_cpu_count: VCpuCountRangeRequest | None = None


@dataclass
class MaintenanceStrategies(PropertyType):
    capacity_rebalance: CapacityRebalance | None = None


@dataclass
class MemoryGiBPerVCpuRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class MemoryMiBRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class NetworkBandwidthGbpsRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class NetworkInterfaceCountRequest(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class OnDemandOptionsRequest(PropertyType):
    allocation_strategy: str | None = None
    capacity_reservation_options: CapacityReservationOptionsRequest | None = None
    max_total_price: str | None = None
    min_target_capacity: int | None = None
    single_availability_zone: bool | None = None
    single_instance_type: bool | None = None


@dataclass
class PerformanceFactorReferenceRequest(PropertyType):
    instance_family: str | None = None


@dataclass
class Placement(PropertyType):
    affinity: str | None = None
    availability_zone: str | None = None
    group_name: str | None = None
    host_id: str | None = None
    host_resource_group_arn: str | None = None
    partition_number: int | None = None
    spread_domain: str | None = None
    tenancy: str | None = None


@dataclass
class SpotOptionsRequest(PropertyType):
    allocation_strategy: str | None = None
    instance_interruption_behavior: str | None = None
    instance_pools_to_use_count: int | None = None
    maintenance_strategies: MaintenanceStrategies | None = None
    max_total_price: str | None = None
    min_target_capacity: int | None = None
    single_availability_zone: bool | None = None
    single_instance_type: bool | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: str | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class TargetCapacitySpecificationRequest(PropertyType):
    total_target_capacity: int | None = None
    default_target_capacity_type: str | None = None
    on_demand_target_capacity: int | None = None
    spot_target_capacity: int | None = None
    target_capacity_unit_type: str | None = None


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class VCpuCountRangeRequest(PropertyType):
    max: int | None = None
    min: int | None = None
