"""PropertyTypes for AWS::SageMaker::Space."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CodeRepository(PropertyType):
    repository_url: str | None = None


@dataclass
class CustomFileSystem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_file_system": "EFSFileSystem",
    }

    efs_file_system: EFSFileSystem | None = None
    f_sx_lustre_file_system: FSxLustreFileSystem | None = None
    s3_file_system: S3FileSystem | None = None


@dataclass
class CustomImage(PropertyType):
    app_image_config_name: str | None = None
    image_name: str | None = None
    image_version_number: int | None = None


@dataclass
class EFSFileSystem(PropertyType):
    file_system_id: str | None = None


@dataclass
class EbsStorageSettings(PropertyType):
    ebs_volume_size_in_gb: int | None = None


@dataclass
class FSxLustreFileSystem(PropertyType):
    file_system_id: str | None = None


@dataclass
class JupyterServerAppSettings(PropertyType):
    default_resource_spec: ResourceSpec | None = None
    lifecycle_config_arns: list[String] = field(default_factory=list)


@dataclass
class KernelGatewayAppSettings(PropertyType):
    custom_images: list[CustomImage] = field(default_factory=list)
    default_resource_spec: ResourceSpec | None = None
    lifecycle_config_arns: list[String] = field(default_factory=list)


@dataclass
class OwnershipSettings(PropertyType):
    owner_user_profile_name: str | None = None


@dataclass
class ResourceSpec(PropertyType):
    instance_type: str | None = None
    lifecycle_config_arn: str | None = None
    sage_maker_image_arn: str | None = None
    sage_maker_image_version_arn: str | None = None


@dataclass
class S3FileSystem(PropertyType):
    s3_uri: str | None = None


@dataclass
class SpaceAppLifecycleManagement(PropertyType):
    idle_settings: SpaceIdleSettings | None = None


@dataclass
class SpaceCodeEditorAppSettings(PropertyType):
    app_lifecycle_management: SpaceAppLifecycleManagement | None = None
    default_resource_spec: ResourceSpec | None = None


@dataclass
class SpaceIdleSettings(PropertyType):
    idle_timeout_in_minutes: int | None = None


@dataclass
class SpaceJupyterLabAppSettings(PropertyType):
    app_lifecycle_management: SpaceAppLifecycleManagement | None = None
    code_repositories: list[CodeRepository] = field(default_factory=list)
    default_resource_spec: ResourceSpec | None = None


@dataclass
class SpaceSettings(PropertyType):
    app_type: str | None = None
    code_editor_app_settings: SpaceCodeEditorAppSettings | None = None
    custom_file_systems: list[CustomFileSystem] = field(default_factory=list)
    jupyter_lab_app_settings: SpaceJupyterLabAppSettings | None = None
    jupyter_server_app_settings: JupyterServerAppSettings | None = None
    kernel_gateway_app_settings: KernelGatewayAppSettings | None = None
    remote_access: str | None = None
    space_managed_resources: str | None = None
    space_storage_settings: SpaceStorageSettings | None = None


@dataclass
class SpaceSharingSettings(PropertyType):
    sharing_type: str | None = None


@dataclass
class SpaceStorageSettings(PropertyType):
    ebs_storage_settings: EbsStorageSettings | None = None
