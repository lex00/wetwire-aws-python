"""PropertyTypes for AWS::SageMaker::Domain."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AppLifecycleManagement(PropertyType):
    idle_settings: DslValue[IdleSettings] | None = None


@dataclass
class CodeEditorAppSettings(PropertyType):
    app_lifecycle_management: DslValue[AppLifecycleManagement] | None = None
    built_in_lifecycle_config_arn: DslValue[str] | None = None
    custom_images: list[DslValue[CustomImage]] = field(default_factory=list)
    default_resource_spec: DslValue[ResourceSpec] | None = None
    lifecycle_config_arns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CodeRepository(PropertyType):
    repository_url: DslValue[str] | None = None


@dataclass
class CustomFileSystemConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_file_system_config": "EFSFileSystemConfig",
    }

    efs_file_system_config: DslValue[EFSFileSystemConfig] | None = None
    f_sx_lustre_file_system_config: DslValue[FSxLustreFileSystemConfig] | None = None
    s3_file_system_config: DslValue[S3FileSystemConfig] | None = None


@dataclass
class CustomImage(PropertyType):
    app_image_config_name: DslValue[str] | None = None
    image_name: DslValue[str] | None = None
    image_version_number: DslValue[int] | None = None


@dataclass
class CustomPosixUserConfig(PropertyType):
    gid: DslValue[int] | None = None
    uid: DslValue[int] | None = None


@dataclass
class DefaultEbsStorageSettings(PropertyType):
    default_ebs_volume_size_in_gb: DslValue[int] | None = None
    maximum_ebs_volume_size_in_gb: DslValue[int] | None = None


@dataclass
class DefaultSpaceSettings(PropertyType):
    execution_role: DslValue[str] | None = None
    custom_file_system_configs: list[DslValue[CustomFileSystemConfig]] = field(
        default_factory=list
    )
    custom_posix_user_config: DslValue[CustomPosixUserConfig] | None = None
    jupyter_lab_app_settings: DslValue[JupyterLabAppSettings] | None = None
    jupyter_server_app_settings: DslValue[JupyterServerAppSettings] | None = None
    kernel_gateway_app_settings: DslValue[KernelGatewayAppSettings] | None = None
    security_groups: list[DslValue[str]] = field(default_factory=list)
    space_storage_settings: DslValue[DefaultSpaceStorageSettings] | None = None


@dataclass
class DefaultSpaceStorageSettings(PropertyType):
    default_ebs_storage_settings: DslValue[DefaultEbsStorageSettings] | None = None


@dataclass
class DockerSettings(PropertyType):
    enable_docker_access: DslValue[str] | None = None
    vpc_only_trusted_accounts: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DomainSettings(PropertyType):
    docker_settings: DslValue[DockerSettings] | None = None
    execution_role_identity_config: DslValue[str] | None = None
    ip_address_type: DslValue[str] | None = None
    r_studio_server_pro_domain_settings: (
        DslValue[RStudioServerProDomainSettings] | None
    ) = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    unified_studio_settings: DslValue[UnifiedStudioSettings] | None = None


@dataclass
class EFSFileSystemConfig(PropertyType):
    file_system_id: DslValue[str] | None = None
    file_system_path: DslValue[str] | None = None


@dataclass
class FSxLustreFileSystemConfig(PropertyType):
    file_system_id: DslValue[str] | None = None
    file_system_path: DslValue[str] | None = None


@dataclass
class HiddenSageMakerImage(PropertyType):
    sage_maker_image_name: DslValue[str] | None = None
    version_aliases: list[DslValue[str]] = field(default_factory=list)


@dataclass
class IdleSettings(PropertyType):
    idle_timeout_in_minutes: DslValue[int] | None = None
    lifecycle_management: DslValue[str] | None = None
    max_idle_timeout_in_minutes: DslValue[int] | None = None
    min_idle_timeout_in_minutes: DslValue[int] | None = None


@dataclass
class JupyterLabAppSettings(PropertyType):
    app_lifecycle_management: DslValue[AppLifecycleManagement] | None = None
    built_in_lifecycle_config_arn: DslValue[str] | None = None
    code_repositories: list[DslValue[CodeRepository]] = field(default_factory=list)
    custom_images: list[DslValue[CustomImage]] = field(default_factory=list)
    default_resource_spec: DslValue[ResourceSpec] | None = None
    lifecycle_config_arns: list[DslValue[str]] = field(default_factory=list)


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
class RSessionAppSettings(PropertyType):
    custom_images: list[DslValue[CustomImage]] = field(default_factory=list)
    default_resource_spec: DslValue[ResourceSpec] | None = None


@dataclass
class RStudioServerProAppSettings(PropertyType):
    access_status: DslValue[str] | None = None
    user_group: DslValue[str] | None = None


@dataclass
class RStudioServerProDomainSettings(PropertyType):
    domain_execution_role_arn: DslValue[str] | None = None
    default_resource_spec: DslValue[ResourceSpec] | None = None
    r_studio_connect_url: DslValue[str] | None = None
    r_studio_package_manager_url: DslValue[str] | None = None


@dataclass
class ResourceSpec(PropertyType):
    instance_type: DslValue[str] | None = None
    lifecycle_config_arn: DslValue[str] | None = None
    sage_maker_image_arn: DslValue[str] | None = None
    sage_maker_image_version_arn: DslValue[str] | None = None


@dataclass
class S3FileSystemConfig(PropertyType):
    mount_path: DslValue[str] | None = None
    s3_uri: DslValue[str] | None = None


@dataclass
class SharingSettings(PropertyType):
    notebook_output_option: DslValue[str] | None = None
    s3_kms_key_id: DslValue[str] | None = None
    s3_output_path: DslValue[str] | None = None


@dataclass
class StudioWebPortalSettings(PropertyType):
    hidden_app_types: list[DslValue[str]] = field(default_factory=list)
    hidden_instance_types: list[DslValue[str]] = field(default_factory=list)
    hidden_ml_tools: list[DslValue[str]] = field(default_factory=list)
    hidden_sage_maker_image_version_aliases: list[DslValue[HiddenSageMakerImage]] = (
        field(default_factory=list)
    )


@dataclass
class UnifiedStudioSettings(PropertyType):
    domain_account_id: DslValue[str] | None = None
    domain_id: DslValue[str] | None = None
    domain_region: DslValue[str] | None = None
    environment_id: DslValue[str] | None = None
    project_id: DslValue[str] | None = None
    project_s3_path: DslValue[str] | None = None
    studio_web_portal_access: DslValue[str] | None = None


@dataclass
class UserSettings(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "auto_mount_home_efs": "AutoMountHomeEFS",
    }

    execution_role: DslValue[str] | None = None
    auto_mount_home_efs: DslValue[str] | None = None
    code_editor_app_settings: DslValue[CodeEditorAppSettings] | None = None
    custom_file_system_configs: list[DslValue[CustomFileSystemConfig]] = field(
        default_factory=list
    )
    custom_posix_user_config: DslValue[CustomPosixUserConfig] | None = None
    default_landing_uri: DslValue[str] | None = None
    jupyter_lab_app_settings: DslValue[JupyterLabAppSettings] | None = None
    jupyter_server_app_settings: DslValue[JupyterServerAppSettings] | None = None
    kernel_gateway_app_settings: DslValue[KernelGatewayAppSettings] | None = None
    r_session_app_settings: DslValue[RSessionAppSettings] | None = None
    r_studio_server_pro_app_settings: DslValue[RStudioServerProAppSettings] | None = (
        None
    )
    security_groups: list[DslValue[str]] = field(default_factory=list)
    sharing_settings: DslValue[SharingSettings] | None = None
    space_storage_settings: DslValue[DefaultSpaceStorageSettings] | None = None
    studio_web_portal: DslValue[str] | None = None
    studio_web_portal_settings: DslValue[StudioWebPortalSettings] | None = None
