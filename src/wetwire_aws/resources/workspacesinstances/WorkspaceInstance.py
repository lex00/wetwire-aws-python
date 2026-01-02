"""PropertyTypes for AWS::WorkspacesInstances::WorkspaceInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: str | None = None
    ebs: EbsBlockDevice | None = None
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
class CpuOptionsRequest(PropertyType):
    core_count: int | None = None
    threads_per_core: int | None = None


@dataclass
class CreditSpecificationRequest(PropertyType):
    cpu_credits: str | None = None


@dataclass
class EC2ManagedInstance(PropertyType):
    instance_id: str | None = None


@dataclass
class EbsBlockDevice(PropertyType):
    encrypted: bool | None = None
    iops: int | None = None
    kms_key_id: str | None = None
    throughput: int | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class EnclaveOptionsRequest(PropertyType):
    enabled: bool | None = None


@dataclass
class HibernationOptionsRequest(PropertyType):
    configured: bool | None = None


@dataclass
class IamInstanceProfileSpecification(PropertyType):
    arn: str | None = None
    name: str | None = None


@dataclass
class InstanceMaintenanceOptionsRequest(PropertyType):
    auto_recovery: str | None = None


@dataclass
class InstanceMarketOptionsRequest(PropertyType):
    market_type: str | None = None
    spot_options: SpotMarketOptions | None = None


@dataclass
class InstanceMetadataOptionsRequest(PropertyType):
    http_endpoint: str | None = None
    http_protocol_ipv6: str | None = None
    http_put_response_hop_limit: int | None = None
    http_tokens: str | None = None
    instance_metadata_tags: str | None = None


@dataclass
class InstanceNetworkInterfaceSpecification(PropertyType):
    description: str | None = None
    device_index: int | None = None
    groups: list[String] = field(default_factory=list)
    subnet_id: str | None = None


@dataclass
class InstanceNetworkPerformanceOptionsRequest(PropertyType):
    bandwidth_weighting: str | None = None


@dataclass
class LicenseConfigurationRequest(PropertyType):
    license_configuration_arn: str | None = None


@dataclass
class ManagedInstance(PropertyType):
    image_id: str | None = None
    instance_type: str | None = None
    block_device_mappings: list[BlockDeviceMapping] = field(default_factory=list)
    capacity_reservation_specification: CapacityReservationSpecification | None = None
    cpu_options: CpuOptionsRequest | None = None
    credit_specification: CreditSpecificationRequest | None = None
    disable_api_stop: bool | None = None
    ebs_optimized: bool | None = None
    enable_primary_ipv6: bool | None = None
    enclave_options: EnclaveOptionsRequest | None = None
    hibernation_options: HibernationOptionsRequest | None = None
    iam_instance_profile: IamInstanceProfileSpecification | None = None
    instance_market_options: InstanceMarketOptionsRequest | None = None
    ipv6_address_count: int | None = None
    key_name: str | None = None
    license_specifications: list[LicenseConfigurationRequest] = field(
        default_factory=list
    )
    maintenance_options: InstanceMaintenanceOptionsRequest | None = None
    metadata_options: InstanceMetadataOptionsRequest | None = None
    monitoring: RunInstancesMonitoringEnabled | None = None
    network_interfaces: list[InstanceNetworkInterfaceSpecification] = field(
        default_factory=list
    )
    network_performance_options: InstanceNetworkPerformanceOptionsRequest | None = None
    placement: Placement | None = None
    private_dns_name_options: PrivateDnsNameOptionsRequest | None = None
    subnet_id: str | None = None
    tag_specifications: list[TagSpecification] = field(default_factory=list)
    user_data: str | None = None


@dataclass
class Placement(PropertyType):
    availability_zone: str | None = None
    group_id: str | None = None
    group_name: str | None = None
    partition_number: int | None = None
    tenancy: str | None = None


@dataclass
class PrivateDnsNameOptionsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: bool | None = None
    enable_resource_name_dns_aaaa_record: bool | None = None
    hostname_type: str | None = None


@dataclass
class RunInstancesMonitoringEnabled(PropertyType):
    enabled: bool | None = None


@dataclass
class SpotMarketOptions(PropertyType):
    instance_interruption_behavior: str | None = None
    max_price: str | None = None
    spot_instance_type: str | None = None
    valid_until_utc: str | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: str | None = None
    tags: list[Tag] = field(default_factory=list)
