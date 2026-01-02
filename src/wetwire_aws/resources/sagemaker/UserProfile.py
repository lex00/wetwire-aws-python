"""PropertyTypes for AWS::SageMaker::UserProfile."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AppLifecycleManagement(PropertyType):
    idle_settings: IdleSettings | None = None


@dataclass
class CodeEditorAppSettings(PropertyType):
    app_lifecycle_management: AppLifecycleManagement | None = None
    built_in_lifecycle_config_arn: str | None = None
    custom_images: list[CustomImage] = field(default_factory=list)
    default_resource_spec: ResourceSpec | None = None
    lifecycle_config_arns: list[String] = field(default_factory=list)


@dataclass
class CodeRepository(PropertyType):
    repository_url: str | None = None


@dataclass
class CustomFileSystemConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_file_system_config": "EFSFileSystemConfig",
    }

    efs_file_system_config: EFSFileSystemConfig | None = None
    f_sx_lustre_file_system_config: FSxLustreFileSystemConfig | None = None
    s3_file_system_config: S3FileSystemConfig | None = None


@dataclass
class CustomImage(PropertyType):
    app_image_config_name: str | None = None
    image_name: str | None = None
    image_version_number: int | None = None


@dataclass
class CustomPosixUserConfig(PropertyType):
    gid: int | None = None
    uid: int | None = None


@dataclass
class DefaultEbsStorageSettings(PropertyType):
    default_ebs_volume_size_in_gb: int | None = None
    maximum_ebs_volume_size_in_gb: int | None = None


@dataclass
class DefaultSpaceStorageSettings(PropertyType):
    default_ebs_storage_settings: DefaultEbsStorageSettings | None = None


@dataclass
class EFSFileSystemConfig(PropertyType):
    file_system_id: str | None = None
    file_system_path: str | None = None


@dataclass
class FSxLustreFileSystemConfig(PropertyType):
    file_system_id: str | None = None
    file_system_path: str | None = None


@dataclass
class HiddenSageMakerImage(PropertyType):
    sage_maker_image_name: str | None = None
    version_aliases: list[String] = field(default_factory=list)


@dataclass
class IdleSettings(PropertyType):
    idle_timeout_in_minutes: int | None = None
    lifecycle_management: str | None = None
    max_idle_timeout_in_minutes: int | None = None
    min_idle_timeout_in_minutes: int | None = None


@dataclass
class JupyterLabAppSettings(PropertyType):
    app_lifecycle_management: AppLifecycleManagement | None = None
    built_in_lifecycle_config_arn: str | None = None
    code_repositories: list[CodeRepository] = field(default_factory=list)
    custom_images: list[CustomImage] = field(default_factory=list)
    default_resource_spec: ResourceSpec | None = None
    lifecycle_config_arns: list[String] = field(default_factory=list)


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
class RStudioServerProAppSettings(PropertyType):
    access_status: str | None = None
    user_group: str | None = None


@dataclass
class ResourceSpec(PropertyType):
    instance_type: str | None = None
    lifecycle_config_arn: str | None = None
    sage_maker_image_arn: str | None = None
    sage_maker_image_version_arn: str | None = None


@dataclass
class S3FileSystemConfig(PropertyType):
    mount_path: str | None = None
    s3_uri: str | None = None


@dataclass
class SharingSettings(PropertyType):
    notebook_output_option: str | None = None
    s3_kms_key_id: str | None = None
    s3_output_path: str | None = None


@dataclass
class StudioWebPortalSettings(PropertyType):
    hidden_app_types: list[String] = field(default_factory=list)
    hidden_instance_types: list[String] = field(default_factory=list)
    hidden_ml_tools: list[String] = field(default_factory=list)
    hidden_sage_maker_image_version_aliases: list[HiddenSageMakerImage] = field(
        default_factory=list
    )


@dataclass
class UserSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_mount_home_efs": "AutoMountHomeEFS",
    }

    auto_mount_home_efs: str | None = None
    code_editor_app_settings: CodeEditorAppSettings | None = None
    custom_file_system_configs: list[CustomFileSystemConfig] = field(
        default_factory=list
    )
    custom_posix_user_config: CustomPosixUserConfig | None = None
    default_landing_uri: str | None = None
    execution_role: str | None = None
    jupyter_lab_app_settings: JupyterLabAppSettings | None = None
    jupyter_server_app_settings: JupyterServerAppSettings | None = None
    kernel_gateway_app_settings: KernelGatewayAppSettings | None = None
    r_studio_server_pro_app_settings: RStudioServerProAppSettings | None = None
    security_groups: list[String] = field(default_factory=list)
    sharing_settings: SharingSettings | None = None
    space_storage_settings: DefaultSpaceStorageSettings | None = None
    studio_web_portal: str | None = None
    studio_web_portal_settings: StudioWebPortalSettings | None = None
