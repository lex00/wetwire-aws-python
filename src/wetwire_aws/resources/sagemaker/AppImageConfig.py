"""PropertyTypes for AWS::SageMaker::AppImageConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CodeEditorAppImageConfig(PropertyType):
    container_config: ContainerConfig | None = None


@dataclass
class ContainerConfig(PropertyType):
    container_arguments: list[String] = field(default_factory=list)
    container_entrypoint: list[String] = field(default_factory=list)
    container_environment_variables: list[CustomImageContainerEnvironmentVariable] = (
        field(default_factory=list)
    )


@dataclass
class CustomImageContainerEnvironmentVariable(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class FileSystemConfig(PropertyType):
    default_gid: int | None = None
    default_uid: int | None = None
    mount_path: str | None = None


@dataclass
class JupyterLabAppImageConfig(PropertyType):
    container_config: ContainerConfig | None = None


@dataclass
class KernelGatewayImageConfig(PropertyType):
    kernel_specs: list[KernelSpec] = field(default_factory=list)
    file_system_config: FileSystemConfig | None = None


@dataclass
class KernelSpec(PropertyType):
    name: str | None = None
    display_name: str | None = None
