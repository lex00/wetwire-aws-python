"""PropertyTypes for AWS::ImageBuilder::ContainerRecipe."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComponentConfiguration(PropertyType):
    component_arn: DslValue[str] | None = None
    parameters: list[DslValue[ComponentParameter]] = field(default_factory=list)


@dataclass
class ComponentParameter(PropertyType):
    name: DslValue[str] | None = None
    value: list[DslValue[str]] = field(default_factory=list)


@dataclass
class EbsInstanceBlockDeviceSpecification(PropertyType):
    delete_on_termination: DslValue[bool] | None = None
    encrypted: DslValue[bool] | None = None
    iops: DslValue[int] | None = None
    kms_key_id: DslValue[str] | None = None
    snapshot_id: DslValue[str] | None = None
    throughput: DslValue[int] | None = None
    volume_size: DslValue[int] | None = None
    volume_type: DslValue[str] | None = None


@dataclass
class InstanceBlockDeviceMapping(PropertyType):
    device_name: DslValue[str] | None = None
    ebs: DslValue[EbsInstanceBlockDeviceSpecification] | None = None
    no_device: DslValue[str] | None = None
    virtual_name: DslValue[str] | None = None


@dataclass
class InstanceConfiguration(PropertyType):
    block_device_mappings: list[DslValue[InstanceBlockDeviceMapping]] = field(
        default_factory=list
    )
    image: DslValue[str] | None = None


@dataclass
class LatestVersion(PropertyType):
    arn: DslValue[str] | None = None
    major: DslValue[str] | None = None
    minor: DslValue[str] | None = None
    patch: DslValue[str] | None = None


@dataclass
class TargetContainerRepository(PropertyType):
    repository_name: DslValue[str] | None = None
    service: DslValue[str] | None = None
