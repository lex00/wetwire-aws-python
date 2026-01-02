"""PropertyTypes for AWS::Deadline::Fleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AcceleratorCapabilities(PropertyType):
    selections: list[AcceleratorSelection] = field(default_factory=list)
    count: AcceleratorCountRange | None = None


@dataclass
class AcceleratorCountRange(PropertyType):
    min: int | None = None
    max: int | None = None


@dataclass
class AcceleratorSelection(PropertyType):
    name: str | None = None
    runtime: str | None = None


@dataclass
class AcceleratorTotalMemoryMiBRange(PropertyType):
    min: int | None = None
    max: int | None = None


@dataclass
class CustomerManagedFleetConfiguration(PropertyType):
    mode: str | None = None
    worker_capabilities: CustomerManagedWorkerCapabilities | None = None
    storage_profile_id: str | None = None
    tag_propagation_mode: str | None = None


@dataclass
class CustomerManagedWorkerCapabilities(PropertyType):
    cpu_architecture_type: str | None = None
    memory_mi_b: MemoryMiBRange | None = None
    os_family: str | None = None
    v_cpu_count: VCpuCountRange | None = None
    accelerator_count: AcceleratorCountRange | None = None
    accelerator_total_memory_mi_b: AcceleratorTotalMemoryMiBRange | None = None
    accelerator_types: list[String] = field(default_factory=list)
    custom_amounts: list[FleetAmountCapability] = field(default_factory=list)
    custom_attributes: list[FleetAttributeCapability] = field(default_factory=list)


@dataclass
class Ec2EbsVolume(PropertyType):
    iops: int | None = None
    size_gi_b: int | None = None
    throughput_mi_b: int | None = None


@dataclass
class FleetAmountCapability(PropertyType):
    min: float | None = None
    name: str | None = None
    max: float | None = None


@dataclass
class FleetAttributeCapability(PropertyType):
    name: str | None = None
    values: list[String] = field(default_factory=list)


@dataclass
class FleetCapabilities(PropertyType):
    amounts: list[FleetAmountCapability] = field(default_factory=list)
    attributes: list[FleetAttributeCapability] = field(default_factory=list)


@dataclass
class FleetConfiguration(PropertyType):
    customer_managed: CustomerManagedFleetConfiguration | None = None
    service_managed_ec2: ServiceManagedEc2FleetConfiguration | None = None


@dataclass
class HostConfiguration(PropertyType):
    script_body: str | None = None
    script_timeout_seconds: int | None = None


@dataclass
class MemoryMiBRange(PropertyType):
    min: int | None = None
    max: int | None = None


@dataclass
class ServiceManagedEc2FleetConfiguration(PropertyType):
    instance_capabilities: ServiceManagedEc2InstanceCapabilities | None = None
    instance_market_options: ServiceManagedEc2InstanceMarketOptions | None = None
    storage_profile_id: str | None = None
    vpc_configuration: VpcConfiguration | None = None


@dataclass
class ServiceManagedEc2InstanceCapabilities(PropertyType):
    cpu_architecture_type: str | None = None
    memory_mi_b: MemoryMiBRange | None = None
    os_family: str | None = None
    v_cpu_count: VCpuCountRange | None = None
    accelerator_capabilities: AcceleratorCapabilities | None = None
    allowed_instance_types: list[String] = field(default_factory=list)
    custom_amounts: list[FleetAmountCapability] = field(default_factory=list)
    custom_attributes: list[FleetAttributeCapability] = field(default_factory=list)
    excluded_instance_types: list[String] = field(default_factory=list)
    root_ebs_volume: Ec2EbsVolume | None = None


@dataclass
class ServiceManagedEc2InstanceMarketOptions(PropertyType):
    type_: str | None = None


@dataclass
class VCpuCountRange(PropertyType):
    min: int | None = None
    max: int | None = None


@dataclass
class VpcConfiguration(PropertyType):
    resource_configuration_arns: list[String] = field(default_factory=list)
