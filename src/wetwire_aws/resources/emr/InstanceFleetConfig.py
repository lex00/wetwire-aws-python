"""PropertyTypes for AWS::EMR::InstanceFleetConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Configuration(PropertyType):
    classification: str | None = None
    configuration_properties: dict[str, String] = field(default_factory=dict)
    configurations: list[Configuration] = field(default_factory=list)


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    volume_specification: VolumeSpecification | None = None
    volumes_per_instance: int | None = None


@dataclass
class EbsConfiguration(PropertyType):
    ebs_block_device_configs: list[EbsBlockDeviceConfig] = field(default_factory=list)
    ebs_optimized: bool | None = None


@dataclass
class InstanceFleetProvisioningSpecifications(PropertyType):
    on_demand_specification: OnDemandProvisioningSpecification | None = None
    spot_specification: SpotProvisioningSpecification | None = None


@dataclass
class InstanceFleetResizingSpecifications(PropertyType):
    on_demand_resize_specification: OnDemandResizingSpecification | None = None
    spot_resize_specification: SpotResizingSpecification | None = None


@dataclass
class InstanceTypeConfig(PropertyType):
    instance_type: str | None = None
    bid_price: str | None = None
    bid_price_as_percentage_of_on_demand_price: float | None = None
    configurations: list[Configuration] = field(default_factory=list)
    custom_ami_id: str | None = None
    ebs_configuration: EbsConfiguration | None = None
    priority: float | None = None
    weighted_capacity: int | None = None


@dataclass
class OnDemandCapacityReservationOptions(PropertyType):
    capacity_reservation_preference: str | None = None
    capacity_reservation_resource_group_arn: str | None = None
    usage_strategy: str | None = None


@dataclass
class OnDemandProvisioningSpecification(PropertyType):
    allocation_strategy: str | None = None
    capacity_reservation_options: OnDemandCapacityReservationOptions | None = None


@dataclass
class OnDemandResizingSpecification(PropertyType):
    allocation_strategy: str | None = None
    capacity_reservation_options: OnDemandCapacityReservationOptions | None = None
    timeout_duration_minutes: int | None = None


@dataclass
class SpotProvisioningSpecification(PropertyType):
    timeout_action: str | None = None
    timeout_duration_minutes: int | None = None
    allocation_strategy: str | None = None
    block_duration_minutes: int | None = None


@dataclass
class SpotResizingSpecification(PropertyType):
    allocation_strategy: str | None = None
    timeout_duration_minutes: int | None = None


@dataclass
class VolumeSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gb": "SizeInGB",
    }

    size_in_gb: int | None = None
    volume_type: str | None = None
    iops: int | None = None
    throughput: int | None = None
