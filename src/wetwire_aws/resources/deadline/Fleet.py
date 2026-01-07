"""PropertyTypes for AWS::Deadline::Fleet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AcceleratorCapabilities(PropertyType):
    selections: list[DslValue[AcceleratorSelection]] = field(default_factory=list)
    count: DslValue[AcceleratorCountRange] | None = None


@dataclass
class AcceleratorCountRange(PropertyType):
    min: DslValue[int] | None = None
    max: DslValue[int] | None = None


@dataclass
class AcceleratorSelection(PropertyType):
    name: DslValue[str] | None = None
    runtime: DslValue[str] | None = None


@dataclass
class AcceleratorTotalMemoryMiBRange(PropertyType):
    min: DslValue[int] | None = None
    max: DslValue[int] | None = None


@dataclass
class CustomerManagedFleetConfiguration(PropertyType):
    mode: DslValue[str] | None = None
    worker_capabilities: DslValue[CustomerManagedWorkerCapabilities] | None = None
    storage_profile_id: DslValue[str] | None = None
    tag_propagation_mode: DslValue[str] | None = None


@dataclass
class CustomerManagedWorkerCapabilities(PropertyType):
    cpu_architecture_type: DslValue[str] | None = None
    memory_mi_b: DslValue[MemoryMiBRange] | None = None
    os_family: DslValue[str] | None = None
    v_cpu_count: DslValue[VCpuCountRange] | None = None
    accelerator_count: DslValue[AcceleratorCountRange] | None = None
    accelerator_total_memory_mi_b: DslValue[AcceleratorTotalMemoryMiBRange] | None = (
        None
    )
    accelerator_types: list[DslValue[str]] = field(default_factory=list)
    custom_amounts: list[DslValue[FleetAmountCapability]] = field(default_factory=list)
    custom_attributes: list[DslValue[FleetAttributeCapability]] = field(
        default_factory=list
    )


@dataclass
class Ec2EbsVolume(PropertyType):
    iops: DslValue[int] | None = None
    size_gi_b: DslValue[int] | None = None
    throughput_mi_b: DslValue[int] | None = None


@dataclass
class FleetAmountCapability(PropertyType):
    min: DslValue[float] | None = None
    name: DslValue[str] | None = None
    max: DslValue[float] | None = None


@dataclass
class FleetAttributeCapability(PropertyType):
    name: DslValue[str] | None = None
    values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class FleetCapabilities(PropertyType):
    amounts: list[DslValue[FleetAmountCapability]] = field(default_factory=list)
    attributes: list[DslValue[FleetAttributeCapability]] = field(default_factory=list)


@dataclass
class FleetConfiguration(PropertyType):
    customer_managed: DslValue[CustomerManagedFleetConfiguration] | None = None
    service_managed_ec2: DslValue[ServiceManagedEc2FleetConfiguration] | None = None


@dataclass
class HostConfiguration(PropertyType):
    script_body: DslValue[str] | None = None
    script_timeout_seconds: DslValue[int] | None = None


@dataclass
class MemoryMiBRange(PropertyType):
    min: DslValue[int] | None = None
    max: DslValue[int] | None = None


@dataclass
class ServiceManagedEc2FleetConfiguration(PropertyType):
    instance_capabilities: DslValue[ServiceManagedEc2InstanceCapabilities] | None = None
    instance_market_options: DslValue[ServiceManagedEc2InstanceMarketOptions] | None = (
        None
    )
    storage_profile_id: DslValue[str] | None = None
    vpc_configuration: DslValue[VpcConfiguration] | None = None


@dataclass
class ServiceManagedEc2InstanceCapabilities(PropertyType):
    cpu_architecture_type: DslValue[str] | None = None
    memory_mi_b: DslValue[MemoryMiBRange] | None = None
    os_family: DslValue[str] | None = None
    v_cpu_count: DslValue[VCpuCountRange] | None = None
    accelerator_capabilities: DslValue[AcceleratorCapabilities] | None = None
    allowed_instance_types: list[DslValue[str]] = field(default_factory=list)
    custom_amounts: list[DslValue[FleetAmountCapability]] = field(default_factory=list)
    custom_attributes: list[DslValue[FleetAttributeCapability]] = field(
        default_factory=list
    )
    excluded_instance_types: list[DslValue[str]] = field(default_factory=list)
    root_ebs_volume: DslValue[Ec2EbsVolume] | None = None


@dataclass
class ServiceManagedEc2InstanceMarketOptions(PropertyType):
    type_: DslValue[str] | None = None


@dataclass
class VCpuCountRange(PropertyType):
    min: DslValue[int] | None = None
    max: DslValue[int] | None = None


@dataclass
class VpcConfiguration(PropertyType):
    resource_configuration_arns: list[DslValue[str]] = field(default_factory=list)
