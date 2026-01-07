"""PropertyTypes for AWS::Greengrass::ResourceDefinitionVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class GroupOwnerSetting(PropertyType):
    auto_add_group_owner: DslValue[bool] | None = None
    group_owner: DslValue[str] | None = None


@dataclass
class LocalDeviceResourceData(PropertyType):
    source_path: DslValue[str] | None = None
    group_owner_setting: DslValue[GroupOwnerSetting] | None = None


@dataclass
class LocalVolumeResourceData(PropertyType):
    destination_path: DslValue[str] | None = None
    source_path: DslValue[str] | None = None
    group_owner_setting: DslValue[GroupOwnerSetting] | None = None


@dataclass
class ResourceDataContainer(PropertyType):
    local_device_resource_data: DslValue[LocalDeviceResourceData] | None = None
    local_volume_resource_data: DslValue[LocalVolumeResourceData] | None = None
    s3_machine_learning_model_resource_data: (
        DslValue[S3MachineLearningModelResourceData] | None
    ) = None
    sage_maker_machine_learning_model_resource_data: (
        DslValue[SageMakerMachineLearningModelResourceData] | None
    ) = None
    secrets_manager_secret_resource_data: (
        DslValue[SecretsManagerSecretResourceData] | None
    ) = None


@dataclass
class ResourceDownloadOwnerSetting(PropertyType):
    group_owner: DslValue[str] | None = None
    group_permission: DslValue[str] | None = None


@dataclass
class ResourceInstance(PropertyType):
    id: DslValue[str] | None = None
    name: DslValue[str] | None = None
    resource_data_container: DslValue[ResourceDataContainer] | None = None


@dataclass
class S3MachineLearningModelResourceData(PropertyType):
    destination_path: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None
    owner_setting: DslValue[ResourceDownloadOwnerSetting] | None = None


@dataclass
class SageMakerMachineLearningModelResourceData(PropertyType):
    destination_path: DslValue[str] | None = None
    sage_maker_job_arn: DslValue[str] | None = None
    owner_setting: DslValue[ResourceDownloadOwnerSetting] | None = None


@dataclass
class SecretsManagerSecretResourceData(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "arn": "ARN",
    }

    arn: DslValue[str] | None = None
    additional_staging_labels_to_download: list[DslValue[str]] = field(
        default_factory=list
    )
