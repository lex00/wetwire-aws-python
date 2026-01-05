"""PropertyTypes for AWS::EC2::SpotFleet."""

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
class ClassicLoadBalancer(PropertyType):
    name: str | None = None


@dataclass
class ClassicLoadBalancersConfig(PropertyType):
    classic_load_balancers: list[ClassicLoadBalancer] = field(default_factory=list)


@dataclass
class CpuPerformanceFactorRequest(PropertyType):
    references: list[PerformanceFactorReferenceRequest] = field(default_factory=list)


@dataclass
class EbsBlockDevice(PropertyType):
    delete_on_termination: bool | None = None
    encrypted: bool | None = None
    iops: int | None = None
    snapshot_id: str | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class FleetLaunchTemplateSpecification(PropertyType):
    version: str | None = None
    launch_template_id: str | None = None
    launch_template_name: str | None = None


@dataclass
class GroupIdentifier(PropertyType):
    group_id: str | None = None


@dataclass
class IamInstanceProfileSpecification(PropertyType):
    arn: str | None = None


@dataclass
class InstanceIpv6Address(PropertyType):
    ipv6_address: str | None = None


@dataclass
class InstanceNetworkInterfaceSpecification(PropertyType):
    associate_public_ip_address: bool | None = None
    delete_on_termination: bool | None = None
    description: str | None = None
    device_index: int | None = None
    groups: list[String] = field(default_factory=list)
    ipv6_address_count: int | None = None
    ipv6_addresses: list[InstanceIpv6Address] = field(default_factory=list)
    network_interface_id: str | None = None
    private_ip_addresses: list[PrivateIpAddressSpecification] = field(
        default_factory=list
    )
    secondary_private_ip_address_count: int | None = None
    subnet_id: str | None = None


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
class LaunchTemplateConfig(PropertyType):
    launch_template_specification: FleetLaunchTemplateSpecification | None = None
    overrides: list[LaunchTemplateOverrides] = field(default_factory=list)


@dataclass
class LaunchTemplateOverrides(PropertyType):
    availability_zone: str | None = None
    availability_zone_id: str | None = None
    instance_requirements: InstanceRequirementsRequest | None = None
    instance_type: str | None = None
    priority: float | None = None
    spot_price: str | None = None
    subnet_id: str | None = None
    weighted_capacity: float | None = None


@dataclass
class LoadBalancersConfig(PropertyType):
    classic_load_balancers_config: ClassicLoadBalancersConfig | None = None
    target_groups_config: TargetGroupsConfig | None = None


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
class PerformanceFactorReferenceRequest(PropertyType):
    instance_family: str | None = None


@dataclass
class PrivateIpAddressSpecification(PropertyType):
    private_ip_address: str | None = None
    primary: bool | None = None


@dataclass
class SpotCapacityRebalance(PropertyType):
    replacement_strategy: str | None = None
    termination_delay: int | None = None


@dataclass
class SpotFleetLaunchSpecification(PropertyType):
    image_id: str | None = None
    block_device_mappings: list[BlockDeviceMapping] = field(default_factory=list)
    ebs_optimized: bool | None = None
    iam_instance_profile: IamInstanceProfileSpecification | None = None
    instance_requirements: InstanceRequirementsRequest | None = None
    instance_type: str | None = None
    kernel_id: str | None = None
    key_name: str | None = None
    monitoring: SpotFleetMonitoring | None = None
    network_interfaces: list[InstanceNetworkInterfaceSpecification] = field(
        default_factory=list
    )
    placement: SpotPlacement | None = None
    ramdisk_id: str | None = None
    security_groups: list[GroupIdentifier] = field(default_factory=list)
    spot_price: str | None = None
    subnet_id: str | None = None
    tag_specifications: list[SpotFleetTagSpecification] = field(default_factory=list)
    user_data: str | None = None
    weighted_capacity: float | None = None


@dataclass
class SpotFleetMonitoring(PropertyType):
    enabled: bool | None = None


@dataclass
class SpotFleetRequestConfigData(PropertyType):
    iam_fleet_role: str | None = None
    target_capacity: int | None = None
    allocation_strategy: str | None = None
    context: str | None = None
    excess_capacity_termination_policy: str | None = None
    instance_interruption_behavior: str | None = None
    instance_pools_to_use_count: int | None = None
    launch_specifications: list[SpotFleetLaunchSpecification] = field(
        default_factory=list
    )
    launch_template_configs: list[LaunchTemplateConfig] = field(default_factory=list)
    load_balancers_config: LoadBalancersConfig | None = None
    on_demand_allocation_strategy: str | None = None
    on_demand_max_total_price: str | None = None
    on_demand_target_capacity: int | None = None
    replace_unhealthy_instances: bool | None = None
    spot_maintenance_strategies: SpotMaintenanceStrategies | None = None
    spot_max_total_price: str | None = None
    spot_price: str | None = None
    tag_specifications: list[SpotFleetTagSpecification] = field(default_factory=list)
    target_capacity_unit_type: str | None = None
    terminate_instances_with_expiration: bool | None = None
    type_: str | None = None
    valid_from: str | None = None
    valid_until: str | None = None


@dataclass
class SpotFleetTagSpecification(PropertyType):
    resource_type: str | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class SpotMaintenanceStrategies(PropertyType):
    capacity_rebalance: SpotCapacityRebalance | None = None


@dataclass
class SpotPlacement(PropertyType):
    availability_zone: str | None = None
    availability_zone_id: str | None = None
    group_name: str | None = None
    tenancy: str | None = None


@dataclass
class TargetGroup(PropertyType):
    arn: str | None = None


@dataclass
class TargetGroupsConfig(PropertyType):
    target_groups: list[TargetGroup] = field(default_factory=list)


@dataclass
class TotalLocalStorageGBRequest(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class VCpuCountRangeRequest(PropertyType):
    max: int | None = None
    min: int | None = None
