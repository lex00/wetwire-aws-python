"""PropertyTypes for AWS::EC2::Instance."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AssociationParameter(PropertyType):
    key: DslValue[str] | None = None
    value: list[DslValue[str]] = field(default_factory=list)


@dataclass
class BlockDeviceMapping(PropertyType):
    device_name: DslValue[str] | None = None
    ebs: DslValue[Ebs] | None = None
    no_device: DslValue[dict[str, Any]] | None = None
    virtual_name: DslValue[str] | None = None


@dataclass
class CpuOptions(PropertyType):
    core_count: DslValue[int] | None = None
    threads_per_core: DslValue[int] | None = None


@dataclass
class CreditSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "cpu_credits": "CPUCredits",
    }

    cpu_credits: DslValue[str] | None = None


@dataclass
class Ebs(PropertyType):
    delete_on_termination: DslValue[bool] | None = None
    encrypted: DslValue[bool] | None = None
    iops: DslValue[int] | None = None
    kms_key_id: DslValue[str] | None = None
    snapshot_id: DslValue[str] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class ElasticGpuSpecification(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class ElasticInferenceAccelerator(PropertyType):
    type_: DslValue[str] | None = None
    count: DslValue[int] | None = None


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
class InstanceIpv6Address(PropertyType):
    ipv6_address: DslValue[str] | None = None


@dataclass
class LaunchTemplateSpecification(PropertyType):
    version: DslValue[str] | None = None
    launch_template_id: DslValue[str] | None = None
    launch_template_name: DslValue[str] | None = None


@dataclass
class LicenseSpecification(PropertyType):
    license_configuration_arn: DslValue[str] | None = None


@dataclass
class MetadataOptions(PropertyType):
    http_endpoint: DslValue[str] | None = None
    http_protocol_ipv6: DslValue[str] | None = None
    http_put_response_hop_limit: DslValue[int] | None = None
    http_tokens: DslValue[str] | None = None
    instance_metadata_tags: DslValue[str] | None = None


@dataclass
class NetworkInterface(PropertyType):
    device_index: DslValue[str] | None = None
    associate_carrier_ip_address: DslValue[bool] | None = None
    associate_public_ip_address: DslValue[bool] | None = None
    delete_on_termination: DslValue[bool] | None = None
    description: DslValue[str] | None = None
    ena_srd_specification: DslValue[EnaSrdSpecification] | None = None
    group_set: list[DslValue[str]] = field(default_factory=list)
    ipv6_address_count: DslValue[int] | None = None
    ipv6_addresses: list[DslValue[InstanceIpv6Address]] = field(default_factory=list)
    network_interface_id: DslValue[str] | None = None
    private_ip_address: DslValue[str] | None = None
    private_ip_addresses: list[DslValue[PrivateIpAddressSpecification]] = field(
        default_factory=list
    )
    secondary_private_ip_address_count: DslValue[int] | None = None
    subnet_id: DslValue[str] | None = None


@dataclass
class PrivateDnsNameOptions(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enable_resource_name_dns_aaaa_record": "EnableResourceNameDnsAAAARecord",
    }

    enable_resource_name_dns_a_record: DslValue[bool] | None = None
    enable_resource_name_dns_aaaa_record: DslValue[bool] | None = None
    hostname_type: DslValue[str] | None = None


@dataclass
class PrivateIpAddressSpecification(PropertyType):
    primary: DslValue[bool] | None = None
    private_ip_address: DslValue[str] | None = None


@dataclass
class SsmAssociation(PropertyType):
    document_name: DslValue[str] | None = None
    association_parameters: list[DslValue[AssociationParameter]] = field(
        default_factory=list
    )


@dataclass
class State(PropertyType):
    code: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class Volume(PropertyType):
    device: DslValue[str] | None = None
    volume_id: DslValue[str] | None = None
