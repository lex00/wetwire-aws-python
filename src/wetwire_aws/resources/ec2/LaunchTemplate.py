"""PropertyTypes for AWS::EC2::LaunchTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AcceleratorCount(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class AcceleratorTotalMemoryMiB(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class BaselineEbsBandwidthMbps(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class BaselinePerformanceFactors(PropertyType):
    cpu: DslValue[Cpu] | None = None


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: DslValue[str] | None = None
    ebs: DslValue[Ebs] | None = None
    no_device: DslValue[str] | None = None
    virtual_name: DslValue[str] | None = None


@dataclass
class CapacityReservationSpecification(PropertyType):
    capacity_reservation_preference: DslValue[str] | None = None
    capacity_reservation_target: DslValue[CapacityReservationTarget] | None = None


@dataclass
class CapacityReservationTarget(PropertyType):
    capacity_reservation_id: DslValue[str] | None = None
    capacity_reservation_resource_group_arn: DslValue[str] | None = None


@dataclass
class ConnectionTrackingSpecification(PropertyType):
    tcp_established_timeout: DslValue[int] | None = None
    udp_stream_timeout: DslValue[int] | None = None
    udp_timeout: DslValue[int] | None = None


@dataclass
class Cpu(PropertyType):
    references: list[DslValue[Reference]] = field(default_factory=list)


@dataclass
class CpuOptions(PropertyType):
    amd_sev_snp: DslValue[str] | None = None
    core_count: DslValue[int] | None = None
    threads_per_core: DslValue[int] | None = None


@dataclass
class CreditSpecification(PropertyType):
    cpu_credits: DslValue[str] | None = None


@dataclass
class Ebs(PropertyType):
    delete_on_termination: DslValue[bool] | None = None
    encrypted: DslValue[bool] | None = None
    iops: DslValue[int] | None = None
    kms_key_id: DslValue[str] | None = None
    snapshot_id: DslValue[str] | None = None
    throughput: DslValue[int] | None = None
    volume_initialization_rate: DslValue[int] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class EnaSrdSpecification(PropertyType):
    ena_srd_enabled: DslValue[bool] | None = None
    ena_srd_udp_specification: DslValue[EnaSrdUdpSpecification] | None = None


@dataclass
class EnaSrdUdpSpecification(PropertyType):
    ena_srd_udp_enabled: DslValue[bool] | None = None


@dataclass
class EnclaveOptions(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class HibernationOptions(PropertyType):
    configured: DslValue[bool] | None = None


@dataclass
class IamInstanceProfile(PropertyType):
    arn: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class InstanceMarketOptions(PropertyType):
    market_type: DslValue[str] | None = None
    spot_options: DslValue[SpotOptions] | None = None


@dataclass
class InstanceRequirements(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    accelerator_count: DslValue[AcceleratorCount] | None = None
    accelerator_manufacturers: list[DslValue[str]] = field(default_factory=list)
    accelerator_names: list[DslValue[str]] = field(default_factory=list)
    accelerator_total_memory_mi_b: DslValue[AcceleratorTotalMemoryMiB] | None = None
    accelerator_types: list[DslValue[str]] = field(default_factory=list)
    allowed_instance_types: list[DslValue[str]] = field(default_factory=list)
    bare_metal: DslValue[str] | None = None
    baseline_ebs_bandwidth_mbps: DslValue[BaselineEbsBandwidthMbps] | None = None
    baseline_performance_factors: DslValue[BaselinePerformanceFactors] | None = None
    burstable_performance: DslValue[str] | None = None
    cpu_manufacturers: list[DslValue[str]] = field(default_factory=list)
    excluded_instance_types: list[DslValue[str]] = field(default_factory=list)
    instance_generations: list[DslValue[str]] = field(default_factory=list)
    local_storage: DslValue[str] | None = None
    local_storage_types: list[DslValue[str]] = field(default_factory=list)
    max_spot_price_as_percentage_of_optimal_on_demand_price: DslValue[int] | None = None
    memory_gi_b_per_v_cpu: DslValue[MemoryGiBPerVCpu] | None = None
    memory_mi_b: DslValue[MemoryMiB] | None = None
    network_bandwidth_gbps: DslValue[NetworkBandwidthGbps] | None = None
    network_interface_count: DslValue[NetworkInterfaceCount] | None = None
    on_demand_max_price_percentage_over_lowest_price: DslValue[int] | None = None
    require_hibernate_support: DslValue[bool] | None = None
    spot_max_price_percentage_over_lowest_price: DslValue[int] | None = None
    total_local_storage_gb: DslValue[TotalLocalStorageGB] | None = None
    v_cpu_count: DslValue[VCpuCount] | None = None


@dataclass
class Ipv4PrefixSpecification(PropertyType):
    ipv4_prefix: DslValue[str] | None = None


@dataclass
class Ipv6Add(PropertyType):
    ipv6_address: DslValue[str] | None = None


@dataclass
class Ipv6PrefixSpecification(PropertyType):
    ipv6_prefix: DslValue[str] | None = None


@dataclass
class LaunchTemplateData(PropertyType):
    block_device_mappings: list[DslValue[BlockDeviceMapping]] = field(
        default_factory=list
    )
    capacity_reservation_specification: (
        DslValue[CapacityReservationSpecification] | None
    ) = None
    cpu_options: DslValue[CpuOptions] | None = None
    credit_specification: DslValue[CreditSpecification] | None = None
    disable_api_stop: DslValue[bool] | None = None
    disable_api_termination: DslValue[bool] | None = None
    ebs_optimized: DslValue[bool] | None = None
    enclave_options: DslValue[EnclaveOptions] | None = None
    hibernation_options: DslValue[HibernationOptions] | None = None
    iam_instance_profile: DslValue[IamInstanceProfile] | None = None
    image_id: DslValue[str] | None = None
    instance_initiated_shutdown_behavior: DslValue[str] | None = None
    instance_market_options: DslValue[InstanceMarketOptions] | None = None
    instance_requirements: DslValue[InstanceRequirements] | None = None
    instance_type: DslValue[str] | None = None
    kernel_id: DslValue[str] | None = None
    key_name: DslValue[str] | None = None
    license_specifications: list[DslValue[LicenseSpecification]] = field(
        default_factory=list
    )
    maintenance_options: DslValue[MaintenanceOptions] | None = None
    metadata_options: DslValue[MetadataOptions] | None = None
    monitoring: DslValue[Monitoring] | None = None
    network_interfaces: list[DslValue[NetworkInterface]] = field(default_factory=list)
    network_performance_options: DslValue[NetworkPerformanceOptions] | None = None
    placement: DslValue[Placement] | None = None
    private_dns_name_options: DslValue[PrivateDnsNameOptions] | None = None
    ram_disk_id: DslValue[str] | None = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    security_groups: list[DslValue[str]] = field(default_factory=list)
    tag_specifications: list[DslValue[TagSpecification]] = field(default_factory=list)
    user_data: DslValue[str] | None = None


@dataclass
class LaunchTemplateTagSpecification(PropertyType):
    resource_type: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class LicenseSpecification(PropertyType):
    license_configuration_arn: DslValue[str] | None = None


@dataclass
class MaintenanceOptions(PropertyType):
    auto_recovery: DslValue[str] | None = None


@dataclass
class MemoryGiBPerVCpu(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class MemoryMiB(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class MetadataOptions(PropertyType):
    http_endpoint: DslValue[str] | None = None
    http_protocol_ipv6: DslValue[str] | None = None
    http_put_response_hop_limit: DslValue[int] | None = None
    http_tokens: DslValue[str] | None = None
    instance_metadata_tags: DslValue[str] | None = None


@dataclass
class Monitoring(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class NetworkBandwidthGbps(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class NetworkInterface(PropertyType):
    associate_carrier_ip_address: DslValue[bool] | None = None
    associate_public_ip_address: DslValue[bool] | None = None
    connection_tracking_specification: (
        DslValue[ConnectionTrackingSpecification] | None
    ) = None
    delete_on_termination: DslValue[bool] | None = None
    description: DslValue[str] | None = None
    device_index: DslValue[int] | None = None
    ena_queue_count: DslValue[int] | None = None
    ena_srd_specification: DslValue[EnaSrdSpecification] | None = None
    groups: list[DslValue[str]] = field(default_factory=list)
    interface_type: DslValue[str] | None = None
    ipv4_prefix_count: DslValue[int] | None = None
    ipv4_prefixes: list[DslValue[Ipv4PrefixSpecification]] = field(default_factory=list)
    ipv6_address_count: DslValue[int] | None = None
    ipv6_addresses: list[DslValue[Ipv6Add]] = field(default_factory=list)
    ipv6_prefix_count: DslValue[int] | None = None
    ipv6_prefixes: list[DslValue[Ipv6PrefixSpecification]] = field(default_factory=list)
    network_card_index: DslValue[int] | None = None
    network_interface_id: DslValue[str] | None = None
    primary_ipv6: DslValue[bool] | None = None
    private_ip_address: DslValue[str] | None = None
    private_ip_addresses: list[DslValue[PrivateIpAdd]] = field(default_factory=list)
    secondary_private_ip_address_count: DslValue[int] | None = None
    subnet_id: DslValue[str] | None = None


@dataclass
class NetworkInterfaceCount(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None


@dataclass
class NetworkPerformanceOptions(PropertyType):
    bandwidth_weighting: DslValue[str] | None = None


@dataclass
class Placement(PropertyType):
    affinity: DslValue[str] | None = None
    availability_zone: DslValue[str] | None = None
    group_id: DslValue[str] | None = None
    group_name: DslValue[str] | None = None
    host_id: DslValue[str] | None = None
    host_resource_group_arn: DslValue[str] | None = None
    partition_number: DslValue[int] | None = None
    spread_domain: DslValue[str] | None = None
    tenancy: DslValue[str] | None = None


@dataclass
class PrivateDnsNameOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: DslValue[bool] | None = None
    enable_resource_name_dns_aaaa_record: DslValue[bool] | None = None
    hostname_type: DslValue[str] | None = None


@dataclass
class PrivateIpAdd(PropertyType):
    primary: DslValue[bool] | None = None
    private_ip_address: DslValue[str] | None = None


@dataclass
class Reference(PropertyType):
    instance_family: DslValue[str] | None = None


@dataclass
class SpotOptions(PropertyType):
    block_duration_minutes: DslValue[int] | None = None
    instance_interruption_behavior: DslValue[str] | None = None
    max_price: DslValue[str] | None = None
    spot_instance_type: DslValue[str] | None = None
    valid_until: DslValue[str] | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class TotalLocalStorageGB(PropertyType):
    max: DslValue[float] | None = None
    min: DslValue[float] | None = None


@dataclass
class VCpuCount(PropertyType):
    max: DslValue[int] | None = None
    min: DslValue[int] | None = None
