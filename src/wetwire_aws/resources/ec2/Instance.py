"""PropertyTypes for AWS::EC2::Instance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AssociationParameter(PropertyType):
    key: str | None = None
    value: list[String] = field(default_factory=list)


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: str | None = None
    ebs: Ebs | None = None
    no_device: dict[str, Any] | None = None
    virtual_name: str | None = None


@dataclass
class CpuOptions(PropertyType):
    core_count: int | None = None
    threads_per_core: int | None = None


@dataclass
class CreditSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_credits": "CPUCredits",
    }

    cpu_credits: str | None = None


@dataclass
class Ebs(PropertyType):
    delete_on_termination: bool | None = None
    encrypted: bool | None = None
    iops: int | None = None
    kms_key_id: str | None = None
    snapshot_id: str | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class ElasticGpuSpecification(PropertyType):
    type_: str | None = None


@dataclass
class ElasticInferenceAccelerator(PropertyType):
    type_: str | None = None
    count: int | None = None


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
class InstanceIpv6Address(PropertyType):
    ipv6_address: str | None = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
    version: str | None = None
    launch_template_id: str | None = None
    launch_template_name: str | None = None


@dataclass
class LicenseSpecification(PropertyType):
    license_configuration_arn: str | None = None


@dataclass
class MetadataOptions(PropertyType):
    http_endpoint: str | None = None
    http_protocol_ipv6: str | None = None
    http_put_response_hop_limit: int | None = None
    http_tokens: str | None = None
    instance_metadata_tags: str | None = None


@dataclass
class NetworkInterface(PropertyType):
    device_index: str | None = None
    associate_carrier_ip_address: bool | None = None
    associate_public_ip_address: bool | None = None
    delete_on_termination: bool | None = None
    description: str | None = None
    ena_srd_specification: EnaSrdSpecification | None = None
    group_set: list[String] = field(default_factory=list)
    ipv6_address_count: int | None = None
    ipv6_addresses: list[InstanceIpv6Address] = field(default_factory=list)
    network_interface_id: str | None = None
    private_ip_address: str | None = None
    private_ip_addresses: list[PrivateIpAddressSpecification] = field(
        default_factory=list
    )
    secondary_private_ip_address_count: int | None = None
    subnet_id: str | None = None


@dataclass
class PrivateDnsNameOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: bool | None = None
    enable_resource_name_dns_aaaa_record: bool | None = None
    hostname_type: str | None = None


@dataclass
class PrivateIpAddressSpecification(PropertyType):
    primary: bool | None = None
    private_ip_address: str | None = None


@dataclass
class SsmAssociation(PropertyType):
    document_name: str | None = None
    association_parameters: list[AssociationParameter] = field(default_factory=list)


@dataclass
class State(PropertyType):
    code: str | None = None
    name: str | None = None


@dataclass
class Volume(PropertyType):
    device: str | None = None
    volume_id: str | None = None
