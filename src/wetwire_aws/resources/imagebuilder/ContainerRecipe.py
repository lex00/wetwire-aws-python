"""PropertyTypes for AWS::ImageBuilder::ContainerRecipe."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComponentConfiguration(PropertyType):
    component_arn: str | None = None
    parameters: list[ComponentParameter] = field(default_factory=list)


@dataclass
class ComponentParameter(PropertyType):
    name: str | None = None
    value: list[String] = field(default_factory=list)


@dataclass
class EbsInstanceBlockDeviceSpecification(PropertyType):
    delete_on_termination: bool | None = None
    encrypted: bool | None = None
    iops: int | None = None
    kms_key_id: str | None = None
    snapshot_id: str | None = None
    throughput: int | None = None
    volume_size: int | None = None
    volume_type: str | None = None


@dataclass
class InstanceBlockDeviceMapping(PropertyType):
    device_name: str | None = None
    ebs: EbsInstanceBlockDeviceSpecification | None = None
    no_device: str | None = None
    virtual_name: str | None = None


@dataclass
class InstanceConfiguration(PropertyType):
    block_device_mappings: list[InstanceBlockDeviceMapping] = field(
        default_factory=list
    )
    image: str | None = None


@dataclass
class LatestVersion(PropertyType):
    arn: str | None = None
    major: str | None = None
    minor: str | None = None
    patch: str | None = None


@dataclass
class TargetContainerRepository(PropertyType):
    repository_name: str | None = None
    service: str | None = None
