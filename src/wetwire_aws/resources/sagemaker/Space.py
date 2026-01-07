"""PropertyTypes for AWS::SageMaker::Space."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CodeRepository(PropertyType):
    repository_url: DslValue[str] | None = None


@dataclass
class CustomFileSystem(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_file_system": "EFSFileSystem",
    }

    efs_file_system: DslValue[EFSFileSystem] | None = None
    f_sx_lustre_file_system: DslValue[FSxLustreFileSystem] | None = None
    s3_file_system: DslValue[S3FileSystem] | None = None


@dataclass
class CustomImage(PropertyType):
    app_image_config_name: DslValue[str] | None = None
    image_name: DslValue[str] | None = None
    image_version_number: DslValue[int] | None = None


@dataclass
class EFSFileSystem(PropertyType):
    file_system_id: DslValue[str] | None = None


@dataclass
class EbsStorageSettings(PropertyType):
    ebs_volume_size_in_gb: DslValue[int] | None = None


@dataclass
class FSxLustreFileSystem(PropertyType):
    file_system_id: DslValue[str] | None = None


@dataclass
class JupyterServerAppSettings(PropertyType):
    default_resource_spec: DslValue[ResourceSpec] | None = None
    lifecycle_config_arns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class KernelGatewayAppSettings(PropertyType):
    custom_images: list[DslValue[CustomImage]] = field(default_factory=list)
    default_resource_spec: DslValue[ResourceSpec] | None = None
    lifecycle_config_arns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class OwnershipSettings(PropertyType):
    owner_user_profile_name: DslValue[str] | None = None


@dataclass
class ResourceSpec(PropertyType):
    instance_type: DslValue[str] | None = None
    lifecycle_config_arn: DslValue[str] | None = None
    sage_maker_image_arn: DslValue[str] | None = None
    sage_maker_image_version_arn: DslValue[str] | None = None


@dataclass
class S3FileSystem(PropertyType):
    s3_uri: DslValue[str] | None = None


@dataclass
class SpaceAppLifecycleManagement(PropertyType):
    idle_settings: DslValue[SpaceIdleSettings] | None = None


@dataclass
class SpaceCodeEditorAppSettings(PropertyType):
    app_lifecycle_management: DslValue[SpaceAppLifecycleManagement] | None = None
    default_resource_spec: DslValue[ResourceSpec] | None = None


@dataclass
class SpaceIdleSettings(PropertyType):
    idle_timeout_in_minutes: DslValue[int] | None = None


@dataclass
class SpaceJupyterLabAppSettings(PropertyType):
    app_lifecycle_management: DslValue[SpaceAppLifecycleManagement] | None = None
    code_repositories: list[DslValue[CodeRepository]] = field(default_factory=list)
    default_resource_spec: DslValue[ResourceSpec] | None = None


@dataclass
class SpaceSettings(PropertyType):
    app_type: DslValue[str] | None = None
    code_editor_app_settings: DslValue[SpaceCodeEditorAppSettings] | None = None
    custom_file_systems: list[DslValue[CustomFileSystem]] = field(default_factory=list)
    jupyter_lab_app_settings: DslValue[SpaceJupyterLabAppSettings] | None = None
    jupyter_server_app_settings: DslValue[JupyterServerAppSettings] | None = None
    kernel_gateway_app_settings: DslValue[KernelGatewayAppSettings] | None = None
    remote_access: DslValue[str] | None = None
    space_managed_resources: DslValue[str] | None = None
    space_storage_settings: DslValue[SpaceStorageSettings] | None = None


@dataclass
class SpaceSharingSettings(PropertyType):
    sharing_type: DslValue[str] | None = None


@dataclass
class SpaceStorageSettings(PropertyType):
    ebs_storage_settings: DslValue[EbsStorageSettings] | None = None
