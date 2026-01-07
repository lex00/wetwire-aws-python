"""PropertyTypes for AWS::SageMaker::AppImageConfig."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CodeEditorAppImageConfig(PropertyType):
    container_config: DslValue[ContainerConfig] | None = None


@dataclass
class ContainerConfig(PropertyType):
    container_arguments: list[DslValue[str]] = field(default_factory=list)
    container_entrypoint: list[DslValue[str]] = field(default_factory=list)
    container_environment_variables: list[
        DslValue[CustomImageContainerEnvironmentVariable]
    ] = field(default_factory=list)


@dataclass
class CustomImageContainerEnvironmentVariable(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class FileSystemConfig(PropertyType):
    default_gid: DslValue[int] | None = None
    default_uid: DslValue[int] | None = None
    mount_path: DslValue[str] | None = None


@dataclass
class JupyterLabAppImageConfig(PropertyType):
    container_config: DslValue[ContainerConfig] | None = None


@dataclass
class KernelGatewayImageConfig(PropertyType):
    kernel_specs: list[DslValue[KernelSpec]] = field(default_factory=list)
    file_system_config: DslValue[FileSystemConfig] | None = None


@dataclass
class KernelSpec(PropertyType):
    name: DslValue[str] | None = None
    display_name: DslValue[str] | None = None
