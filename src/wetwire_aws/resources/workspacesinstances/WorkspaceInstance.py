"""PropertyTypes for AWS::WorkspacesInstances::WorkspaceInstance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: DslValue[str] | None = None
    ebs: DslValue[EbsBlockDevice] | None = None
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
class CpuOptionsRequest(PropertyType):
    core_count: DslValue[int] | None = None
    threads_per_core: DslValue[int] | None = None


@dataclass
class CreditSpecificationRequest(PropertyType):
    cpu_credits: DslValue[str] | None = None


@dataclass
class EC2ManagedInstance(PropertyType):
    instance_id: DslValue[str] | None = None


@dataclass
class EbsBlockDevice(PropertyType):
    encrypted: DslValue[bool] | None = None
    iops: DslValue[int] | None = None
    kms_key_id: DslValue[str] | None = None
    throughput: DslValue[int] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class EnclaveOptionsRequest(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class HibernationOptionsRequest(PropertyType):
    configured: DslValue[bool] | None = None


@dataclass
class IamInstanceProfileSpecification(PropertyType):
    arn: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class InstanceMaintenanceOptionsRequest(PropertyType):
    auto_recovery: DslValue[str] | None = None


@dataclass
class InstanceMarketOptionsRequest(PropertyType):
    market_type: DslValue[str] | None = None
    spot_options: DslValue[SpotMarketOptions] | None = None


@dataclass
class InstanceMetadataOptionsRequest(PropertyType):
    http_endpoint: DslValue[str] | None = None
    http_protocol_ipv6: DslValue[str] | None = None
    http_put_response_hop_limit: DslValue[int] | None = None
    http_tokens: DslValue[str] | None = None
    instance_metadata_tags: DslValue[str] | None = None


@dataclass
class InstanceNetworkInterfaceSpecification(PropertyType):
    description: DslValue[str] | None = None
    device_index: DslValue[int] | None = None
    groups: list[DslValue[str]] = field(default_factory=list)
    subnet_id: DslValue[str] | None = None


@dataclass
class InstanceNetworkPerformanceOptionsRequest(PropertyType):
    bandwidth_weighting: DslValue[str] | None = None


@dataclass
class LicenseConfigurationRequest(PropertyType):
    license_configuration_arn: DslValue[str] | None = None


@dataclass
class ManagedInstance(PropertyType):
    image_id: DslValue[str] | None = None
    instance_type: DslValue[str] | None = None
    block_device_mappings: list[DslValue[BlockDeviceMapping]] = field(
        default_factory=list
    )
    capacity_reservation_specification: (
        DslValue[CapacityReservationSpecification] | None
    ) = None
    cpu_options: DslValue[CpuOptionsRequest] | None = None
    credit_specification: DslValue[CreditSpecificationRequest] | None = None
    disable_api_stop: DslValue[bool] | None = None
    ebs_optimized: DslValue[bool] | None = None
    enable_primary_ipv6: DslValue[bool] | None = None
    enclave_options: DslValue[EnclaveOptionsRequest] | None = None
    hibernation_options: DslValue[HibernationOptionsRequest] | None = None
    iam_instance_profile: DslValue[IamInstanceProfileSpecification] | None = None
    instance_market_options: DslValue[InstanceMarketOptionsRequest] | None = None
    ipv6_address_count: DslValue[int] | None = None
    key_name: DslValue[str] | None = None
    license_specifications: list[DslValue[LicenseConfigurationRequest]] = field(
        default_factory=list
    )
    maintenance_options: DslValue[InstanceMaintenanceOptionsRequest] | None = None
    metadata_options: DslValue[InstanceMetadataOptionsRequest] | None = None
    monitoring: DslValue[RunInstancesMonitoringEnabled] | None = None
    network_interfaces: list[DslValue[InstanceNetworkInterfaceSpecification]] = field(
        default_factory=list
    )
    network_performance_options: (
        DslValue[InstanceNetworkPerformanceOptionsRequest] | None
    ) = None
    placement: DslValue[Placement] | None = None
    private_dns_name_options: DslValue[PrivateDnsNameOptionsRequest] | None = None
    subnet_id: DslValue[str] | None = None
    tag_specifications: list[DslValue[TagSpecification]] = field(default_factory=list)
    user_data: DslValue[str] | None = None


@dataclass
class Placement(PropertyType):
    availability_zone: DslValue[str] | None = None
    group_id: DslValue[str] | None = None
    group_name: DslValue[str] | None = None
    partition_number: DslValue[int] | None = None
    tenancy: DslValue[str] | None = None


@dataclass
class PrivateDnsNameOptionsRequest(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: DslValue[bool] | None = None
    enable_resource_name_dns_aaaa_record: DslValue[bool] | None = None
    hostname_type: DslValue[str] | None = None


@dataclass
class RunInstancesMonitoringEnabled(PropertyType):
    enabled: DslValue[bool] | None = None


@dataclass
class SpotMarketOptions(PropertyType):
    instance_interruption_behavior: DslValue[str] | None = None
    max_price: DslValue[str] | None = None
    spot_instance_type: DslValue[str] | None = None
    valid_until_utc: DslValue[str] | None = None


@dataclass
class TagSpecification(PropertyType):
    resource_type: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
