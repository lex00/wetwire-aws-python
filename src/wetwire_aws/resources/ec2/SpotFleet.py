"""PropertyTypes for AWS::EC2::SpotFleet."""

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
class ClassicLoadBalancer(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class ClassicLoadBalancersConfig(PropertyType):
    classic_load_balancers: list[DslValue[ClassicLoadBalancer]] = field(
        default_factory=list
    )


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
    snapshot_id: DslValue[str] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class FleetLaunchTemplateSpecification(PropertyType):
    version: DslValue[str] | None = None
    launch_template_id: DslValue[str] | None = None
    launch_template_name: DslValue[str] | None = None


@dataclass
class GroupIdentifier(PropertyType):
    group_id: DslValue[str] | None = None


@dataclass
class IamInstanceProfileSpecification(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class InstanceIpv6Address(PropertyType):
    ipv6_address: DslValue[str] | None = None


@dataclass
class InstanceNetworkInterfaceSpecification(PropertyType):
    associate_public_ip_address: DslValue[bool] | None = None
    delete_on_termination: DslValue[bool] | None = None
    description: DslValue[str] | None = None
    device_index: DslValue[int] | None = None
    groups: list[DslValue[str]] = field(default_factory=list)
    ipv6_address_count: DslValue[int] | None = None
    ipv6_addresses: list[DslValue[InstanceIpv6Address]] = field(default_factory=list)
    network_interface_id: DslValue[str] | None = None
    private_ip_addresses: list[DslValue[PrivateIpAddressSpecification]] = field(
        default_factory=list
    )
    secondary_private_ip_address_count: DslValue[int] | None = None
    subnet_id: DslValue[str] | None = None


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
class LaunchTemplateConfig(PropertyType):
    launch_template_specification: DslValue[FleetLaunchTemplateSpecification] | None = (
        None
    )
    overrides: list[DslValue[LaunchTemplateOverrides]] = field(default_factory=list)


@dataclass
class LaunchTemplateOverrides(PropertyType):
    availability_zone: DslValue[str] | None = None
    availability_zone_id: DslValue[str] | None = None
    instance_requirements: DslValue[InstanceRequirementsRequest] | None = None
    instance_type: DslValue[str] | None = None
    priority: DslValue[float] | None = None
    spot_price: DslValue[str] | None = None
    subnet_id: DslValue[str] | None = None
    weighted_capacity: DslValue[float] | None = None


@dataclass
class LoadBalancersConfig(PropertyType):
    classic_load_balancers_config: DslValue[ClassicLoadBalancersConfig] | None = None
    target_groups_config: DslValue[TargetGroupsConfig] | None = None


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
class PerformanceFactorReferenceRequest(PropertyType):
    instance_family: DslValue[str] | None = None


@dataclass
class PrivateIpAddressSpecification(PropertyType):
    private_ip_address: DslValue[str] | None = None
    primary: DslValue[bool] | None = None


@dataclass
class SpotCapacityRebalance(PropertyType):
    replacement_strategy: DslValue[str] | None = None
    termination_delay: DslValue[int] | None = None


@dataclass
class SpotFleetLaunchSpecification(PropertyType):
    image_id: DslValue[str] | None = None
    block_device_mappings: list[DslValue[BlockDeviceMapping]] = field(
        default_factory=list
    )
    ebs_optimized: DslValue[bool] | None = None
    iam_instance_profile: DslValue[IamInstanceProfileSpecification] | None = None
    instance_requirements: DslValue[InstanceRequirementsRequest] | None = None
    instance_type: DslValue[str] | None = None
    kernel_id: DslValue[str] | None = None
    key_name: DslValue[str] | None = None
    monitoring: DslValue[SpotFleetMonitoring] | None = None
    network_interfaces: list[DslValue[InstanceNetworkInterfaceSpecification]] = field(
        default_factory=list
    )
    placement: DslValue[SpotPlacement] | None = None
    ramdisk_id: DslValue[str] | None = None
    security_groups: list[DslValue[GroupIdentifier]] = field(default_factory=list)
    spot_price: DslValue[str] | None = None
    subnet_id: DslValue[str] | None = None
    tag_specifications: list[DslValue[SpotFleetTagSpecification]] = field(
        default_factory=list
    )
    user_data: DslValue[str] | None = None
    weighted_capacity: DslValue[float] | None = None


@dataclass
class SpotFleetMonitoring(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class SpotFleetRequestConfigData(PropertyType):
    iam_fleet_role: DslValue[str] | None = None
    target_capacity: DslValue[int] | None = None
    allocation_strategy: DslValue[str] | None = None
    context: DslValue[str] | None = None
    excess_capacity_termination_policy: DslValue[str] | None = None
    instance_interruption_behavior: DslValue[str] | None = None
    instance_pools_to_use_count: DslValue[int] | None = None
    launch_specifications: list[DslValue[SpotFleetLaunchSpecification]] = field(
        default_factory=list
    )
    launch_template_configs: list[DslValue[LaunchTemplateConfig]] = field(
        default_factory=list
    )
    load_balancers_config: DslValue[LoadBalancersConfig] | None = None
    on_demand_allocation_strategy: DslValue[str] | None = None
    on_demand_max_total_price: DslValue[str] | None = None
    on_demand_target_capacity: DslValue[int] | None = None
    replace_unhealthy_instances: DslValue[bool] | None = None
    spot_maintenance_strategies: DslValue[SpotMaintenanceStrategies] | None = None
    spot_max_total_price: DslValue[str] | None = None
    spot_price: DslValue[str] | None = None
    tag_specifications: list[DslValue[SpotFleetTagSpecification]] = field(
        default_factory=list
    )
    target_capacity_unit_type: DslValue[str] | None = None
    terminate_instances_with_expiration: DslValue[bool] | None = None
    type_: DslValue[str] | None = None
    valid_from: DslValue[str] | None = None
    valid_until: DslValue[str] | None = None


@dataclass
class SpotFleetTagSpecification(PropertyType):
    resource_type: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class SpotMaintenanceStrategies(PropertyType):
    capacity_rebalance: DslValue[SpotCapacityRebalance] | None = None


@dataclass
class SpotPlacement(PropertyType):
    availability_zone: DslValue[str] | None = None
    availability_zone_id: DslValue[str] | None = None
    group_name: DslValue[str] | None = None
    tenancy: DslValue[str] | None = None


@dataclass
class TargetGroup(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class TargetGroupsConfig(PropertyType):
    target_groups: list[DslValue[TargetGroup]] = field(default_factory=list)


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class VCpuCountRangeRequest(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None
