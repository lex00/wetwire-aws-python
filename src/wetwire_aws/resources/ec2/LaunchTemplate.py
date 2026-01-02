"""PropertyTypes for AWS::EC2::LaunchTemplate."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AcceleratorCount(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class AcceleratorTotalMemoryMiB(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class BaselineEbsBandwidthMbps(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class BaselinePerformanceFactors(PropertyType):
    cpu: Cpu | None = None


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: str | None = None
    ebs: Ebs | None = None
    no_device: str | None = None
    virtual_name: str | None = None


@dataclass
class CapacityReservationSpecification(PropertyType):
    capacity_reservation_preference: str | None = None
    capacity_reservation_target: CapacityReservationTarget | None = None


@dataclass
class CapacityReservationTarget(PropertyType):
    capacity_reservation_id: str | None = None
    capacity_reservation_resource_group_arn: str | None = None


@dataclass
class ConnectionTrackingSpecification(PropertyType):
    tcp_established_timeout: int | None = None
    udp_stream_timeout: int | None = None
    udp_timeout: int | None = None


@dataclass
class Cpu(PropertyType):
    references: list[Reference] = field(default_factory=list)


@dataclass
class CpuOptions(PropertyType):
    amd_sev_snp: str | None = None
    core_count: int | None = None
    threads_per_core: int | None = None


@dataclass
class CreditSpecification(PropertyType):
    cpu_credits: str | None = None


@dataclass
class Ebs(PropertyType):
    delete_on_termination: bool | None = None
    encrypted: bool | None = None
    iops: int | None = None
    kms_key_id: str | None = None
    snapshot_id: str | None = None
    throughput: int | None = None
    volume_initialization_rate: int | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class EnaSrdSpecification(PropertyType):
    ena_srd_enabled: bool | None = None
    ena_srd_udp_specification: EnaSrdUdpSpecification | None = None


@dataclass
class EnaSrdUdpSpecification(PropertyType):
    ena_srd_udp_enabled: bool | None = None


@dataclass
class EnclaveOptions(PropertyType):
    enabled: bool | None = None


@dataclass
class HibernationOptions(PropertyType):
    configured: bool | None = None


@dataclass
class IamInstanceProfile(PropertyType):
    arn: str | None = None
    name: str | None = None


@dataclass
class InstanceMarketOptions(PropertyType):
    market_type: str | None = None
    spot_options: SpotOptions | None = None


@dataclass
class InstanceRequirements(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "total_local_storage_gb": "TotalLocalStorageGB",
    }

    accelerator_count: AcceleratorCount | None = None
    accelerator_manufacturers: list[String] = field(default_factory=list)
    accelerator_names: list[String] = field(default_factory=list)
    accelerator_total_memory_mi_b: AcceleratorTotalMemoryMiB | None = None
    accelerator_types: list[String] = field(default_factory=list)
    allowed_instance_types: list[String] = field(default_factory=list)
    bare_metal: str | None = None
    baseline_ebs_bandwidth_mbps: BaselineEbsBandwidthMbps | None = None
    baseline_performance_factors: BaselinePerformanceFactors | None = None
    burstable_performance: str | None = None
    cpu_manufacturers: list[String] = field(default_factory=list)
    excluded_instance_types: list[String] = field(default_factory=list)
    instance_generations: list[String] = field(default_factory=list)
    local_storage: str | None = None
    local_storage_types: list[String] = field(default_factory=list)
    max_spot_price_as_percentage_of_optimal_on_demand_price: int | None = None
    memory_gi_b_per_v_cpu: MemoryGiBPerVCpu | None = None
    memory_mi_b: MemoryMiB | None = None
    network_bandwidth_gbps: NetworkBandwidthGbps | None = None
    network_interface_count: NetworkInterfaceCount | None = None
    on_demand_max_price_percentage_over_lowest_price: int | None = None
    require_hibernate_support: bool | None = None
    spot_max_price_percentage_over_lowest_price: int | None = None
    total_local_storage_gb: TotalLocalStorageGB | None = None
    v_cpu_count: VCpuCount | None = None


@dataclass
class Ipv4PrefixSpecification(PropertyType):
    ipv4_prefix: str | None = None


@dataclass
class Ipv6Add(PropertyType):
    ipv6_address: str | None = None


@dataclass
class Ipv6PrefixSpecification(PropertyType):
    ipv6_prefix: str | None = None


@dataclass
class LaunchTemplateData(PropertyType):
    block_device_mappings: list[BlockDeviceMapping] = field(default_factory=list)
    capacity_reservation_specification: CapacityReservationSpecification | None = None
    cpu_options: CpuOptions | None = None
    credit_specification: CreditSpecification | None = None
    disable_api_stop: bool | None = None
    disable_api_termination: bool | None = None
    ebs_optimized: bool | None = None
    enclave_options: EnclaveOptions | None = None
    hibernation_options: HibernationOptions | None = None
    iam_instance_profile: IamInstanceProfile | None = None
    image_id: str | None = None
    instance_initiated_shutdown_behavior: str | None = None
    instance_market_options: InstanceMarketOptions | None = None
    instance_requirements: InstanceRequirements | None = None
    instance_type: str | None = None
    kernel_id: str | None = None
    key_name: str | None = None
    license_specifications: list[LicenseSpecification] = field(default_factory=list)
    maintenance_options: MaintenanceOptions | None = None
    metadata_options: MetadataOptions | None = None
    monitoring: Monitoring | None = None
    network_interfaces: list[NetworkInterface] = field(default_factory=list)
    network_performance_options: NetworkPerformanceOptions | None = None
    placement: Placement | None = None
    private_dns_name_options: PrivateDnsNameOptions | None = None
    ram_disk_id: str | None = None
    security_group_ids: list[String] = field(default_factory=list)
    security_groups: list[String] = field(default_factory=list)
    tag_specifications: list[TagSpecification] = field(default_factory=list)
    user_data: str | None = None


@dataclass
class LaunchTemplateTagSpecification(PropertyType):
    resource_type: str | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class LicenseSpecification(PropertyType):
    license_configuration_arn: str | None = None


@dataclass
class MaintenanceOptions(PropertyType):
    auto_recovery: str | None = None


@dataclass
class MemoryGiBPerVCpu(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class MemoryMiB(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class MetadataOptions(PropertyType):
    http_endpoint: str | None = None
    http_protocol_ipv6: str | None = None
    http_put_response_hop_limit: int | None = None
    http_tokens: str | None = None
    instance_metadata_tags: str | None = None


@dataclass
class Monitoring(PropertyType):
    enabled: bool | None = None


@dataclass
class NetworkBandwidthGbps(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class NetworkInterface(PropertyType):
    associate_carrier_ip_address: bool | None = None
    associate_public_ip_address: bool | None = None
    connection_tracking_specification: ConnectionTrackingSpecification | None = None
    delete_on_termination: bool | None = None
    description: str | None = None
    device_index: int | None = None
    ena_queue_count: int | None = None
    ena_srd_specification: EnaSrdSpecification | None = None
    groups: list[String] = field(default_factory=list)
    interface_type: str | None = None
    ipv4_prefix_count: int | None = None
    ipv4_prefixes: list[Ipv4PrefixSpecification] = field(default_factory=list)
    ipv6_address_count: int | None = None
    ipv6_addresses: list[Ipv6Add] = field(default_factory=list)
    ipv6_prefix_count: int | None = None
    ipv6_prefixes: list[Ipv6PrefixSpecification] = field(default_factory=list)
    network_card_index: int | None = None
    network_interface_id: str | None = None
    primary_ipv6: bool | None = None
    private_ip_address: str | None = None
    private_ip_addresses: list[PrivateIpAdd] = field(default_factory=list)
    secondary_private_ip_address_count: int | None = None
    subnet_id: str | None = None


@dataclass
class NetworkInterfaceCount(PropertyType):
    max: int | None = None
    min: int | None = None


@dataclass
class NetworkPerformanceOptions(PropertyType):
    bandwidth_weighting: str | None = None


@dataclass
class Placement(PropertyType):
    affinity: str | None = None
    availability_zone: str | None = None
    group_id: str | None = None
    group_name: str | None = None
    host_id: str | None = None
    host_resource_group_arn: str | None = None
    partition_number: int | None = None
    spread_domain: str | None = None
    tenancy: str | None = None


@dataclass
class PrivateDnsNameOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: bool | None = None
    enable_resource_name_dns_aaaa_record: bool | None = None
    hostname_type: str | None = None


@dataclass
class PrivateIpAdd(PropertyType):
    primary: bool | None = None
    private_ip_address: str | None = None


@dataclass
class Reference(PropertyType):
    instance_family: str | None = None


@dataclass
class SpotOptions(PropertyType):
    block_duration_minutes: int | None = None
    instance_interruption_behavior: str | None = None
    max_price: str | None = None
    spot_instance_type: str | None = None
    valid_until: str | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: str | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class TotalLocalStorageGB(PropertyType):
    max: float | None = None
    min: float | None = None


@dataclass
class VCpuCount(PropertyType):
    max: int | None = None
    min: int | None = None
