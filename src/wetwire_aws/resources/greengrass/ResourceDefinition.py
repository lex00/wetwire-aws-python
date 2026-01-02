"""PropertyTypes for AWS::Greengrass::ResourceDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class GroupOwnerSetting(PropertyType):
    auto_add_group_owner: bool | None = None
    group_owner: str | None = None


@dataclass
class LocalDeviceResourceData(PropertyType):
    source_path: str | None = None
    group_owner_setting: GroupOwnerSetting | None = None


@dataclass
class LocalVolumeResourceData(PropertyType):
    destination_path: str | None = None
    source_path: str | None = None
    group_owner_setting: GroupOwnerSetting | None = None


@dataclass
class ResourceDataContainer(PropertyType):
    local_device_resource_data: LocalDeviceResourceData | None = None
    local_volume_resource_data: LocalVolumeResourceData | None = None
    s3_machine_learning_model_resource_data: (
        S3MachineLearningModelResourceData | None
    ) = None
    sage_maker_machine_learning_model_resource_data: (
        SageMakerMachineLearningModelResourceData | None
    ) = None
    secrets_manager_secret_resource_data: SecretsManagerSecretResourceData | None = None


@dataclass
class ResourceDefinitionVersion(PropertyType):
    resources: list[ResourceInstance] = field(default_factory=list)


@dataclass
class ResourceDownloadOwnerSetting(PropertyType):
    group_owner: str | None = None
    group_permission: str | None = None


@dataclass
class ResourceInstance(PropertyType):
    id: str | None = None
    name: str | None = None
    resource_data_container: ResourceDataContainer | None = None


@dataclass
class S3MachineLearningModelResourceData(PropertyType):
    destination_path: str | None = None
    s3_uri: str | None = None
    owner_setting: ResourceDownloadOwnerSetting | None = None


@dataclass
class SageMakerMachineLearningModelResourceData(PropertyType):
    destination_path: str | None = None
    sage_maker_job_arn: str | None = None
    owner_setting: ResourceDownloadOwnerSetting | None = None


@dataclass
class SecretsManagerSecretResourceData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "ARN",
    }

    arn: str | None = None
    additional_staging_labels_to_download: list[String] = field(default_factory=list)
