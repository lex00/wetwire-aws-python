"""PropertyTypes for AWS::GreengrassV2::ComponentVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ComponentDependencyRequirement(PropertyType):
    dependency_type: str | None = None
    version_requirement: str | None = None


@dataclass
class ComponentPlatform(PropertyType):
    attributes: dict[str, String] = field(default_factory=dict)
    name: str | None = None


@dataclass
class LambdaContainerParams(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "memory_size_in_kb": "MemorySizeInKB",
        "mount_ro_sysfs": "MountROSysfs",
    }

    devices: list[LambdaDeviceMount] = field(default_factory=list)
    memory_size_in_kb: int | None = None
    mount_ro_sysfs: bool | None = None
    volumes: list[LambdaVolumeMount] = field(default_factory=list)


@dataclass
class LambdaDeviceMount(PropertyType):
    add_group_owner: bool | None = None
    path: str | None = None
    permission: str | None = None


@dataclass
class LambdaEventSource(PropertyType):
    topic: str | None = None
    type_: str | None = None


@dataclass
class LambdaExecutionParameters(PropertyType):
    environment_variables: dict[str, String] = field(default_factory=dict)
    event_sources: list[LambdaEventSource] = field(default_factory=list)
    exec_args: list[String] = field(default_factory=list)
    input_payload_encoding_type: str | None = None
    linux_process_params: LambdaLinuxProcessParams | None = None
    max_idle_time_in_seconds: int | None = None
    max_instances_count: int | None = None
    max_queue_size: int | None = None
    pinned: bool | None = None
    status_timeout_in_seconds: int | None = None
    timeout_in_seconds: int | None = None


@dataclass
class LambdaFunctionRecipeSource(PropertyType):
    component_dependencies: dict[str, ComponentDependencyRequirement] = field(
        default_factory=dict
    )
    component_lambda_parameters: LambdaExecutionParameters | None = None
    component_name: str | None = None
    component_platforms: list[ComponentPlatform] = field(default_factory=list)
    component_version: str | None = None
    lambda_arn: str | None = None


@dataclass
class LambdaLinuxProcessParams(PropertyType):
    container_params: LambdaContainerParams | None = None
    isolation_mode: str | None = None


@dataclass
class LambdaVolumeMount(PropertyType):
    add_group_owner: bool | None = None
    destination_path: str | None = None
    permission: str | None = None
    source_path: str | None = None
