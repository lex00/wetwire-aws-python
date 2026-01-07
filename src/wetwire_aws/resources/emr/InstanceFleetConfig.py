"""PropertyTypes for AWS::EMR::InstanceFleetConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Configuration(PropertyType):
    classification: DslValue[str] | None = None
    configuration_properties: dict[str, DslValue[str]] = field(default_factory=dict)
    configurations: list[DslValue[Configuration]] = field(default_factory=list)


@dataclass
class EbsBlockDeviceConfig(PropertyType):
    volume_specification: DslValue[VolumeSpecification] | None = None
    volumes_per_instance: DslValue[int] | None = None


@dataclass
class EbsConfiguration(PropertyType):
    ebs_block_device_configs: list[DslValue[EbsBlockDeviceConfig]] = field(
        default_factory=list
    )
    ebs_optimized: DslValue[bool] | None = None


@dataclass
class InstanceFleetProvisioningSpecifications(PropertyType):
    on_demand_specification: DslValue[OnDemandProvisioningSpecification] | None = None
    spot_specification: DslValue[SpotProvisioningSpecification] | None = None


@dataclass
class InstanceFleetResizingSpecifications(PropertyType):
    on_demand_resize_specification: DslValue[OnDemandResizingSpecification] | None = (
        None
    )
    spot_resize_specification: DslValue[SpotResizingSpecification] | None = None


@dataclass
class InstanceTypeConfig(PropertyType):
    instance_type: DslValue[str] | None = None
    bid_price: DslValue[str] | None = None
    bid_price_as_percentage_of_on_demand_price: DslValue[float] | None = None
    configurations: list[DslValue[Configuration]] = field(default_factory=list)
    custom_ami_id: DslValue[str] | None = None
    ebs_configuration: DslValue[EbsConfiguration] | None = None
    priority: DslValue[float] | None = None
    weighted_capacity: DslValue[int] | None = None


@dataclass
class OnDemandCapacityReservationOptions(PropertyType):
    capacity_reservation_preference: DslValue[str] | None = None
    capacity_reservation_resource_group_arn: DslValue[str] | None = None
    usage_strategy: DslValue[str] | None = None


@dataclass
class OnDemandProvisioningSpecification(PropertyType):
    allocation_strategy: DslValue[str] | None = None
    capacity_reservation_options: (
        DslValue[OnDemandCapacityReservationOptions] | None
    ) = None


@dataclass
class OnDemandResizingSpecification(PropertyType):
    allocation_strategy: DslValue[str] | None = None
    capacity_reservation_options: (
        DslValue[OnDemandCapacityReservationOptions] | None
    ) = None
    timeout_duration_minutes: DslValue[int] | None = None


@dataclass
class SpotProvisioningSpecification(PropertyType):
    timeout_action: DslValue[str] | None = None
    timeout_duration_minutes: DslValue[int] | None = None
    allocation_strategy: DslValue[str] | None = None
    block_duration_minutes: DslValue[int] | None = None


@dataclass
class SpotResizingSpecification(PropertyType):
    allocation_strategy: DslValue[str] | None = None
    timeout_duration_minutes: DslValue[int] | None = None


@dataclass
class VolumeSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "size_in_gb": "SizeInGB",
    }

    size_in_gb: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None
    iops: DslValue[int] | None = None
    throughput: DslValue[int] | None = None
