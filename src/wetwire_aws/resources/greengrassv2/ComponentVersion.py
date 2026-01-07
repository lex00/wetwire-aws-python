"""PropertyTypes for AWS::GreengrassV2::ComponentVersion."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ComponentDependencyRequirement(PropertyType):
    dependency_type: DslValue[str] | None = None
    version_requirement: DslValue[str] | None = None


@dataclass
class ComponentPlatform(PropertyType):
    attributes: dict[str, DslValue[str]] = field(default_factory=dict)
    name: DslValue[str] | None = None


@dataclass
class LambdaContainerParams(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "memory_size_in_kb": "MemorySizeInKB",
        "mount_ro_sysfs": "MountROSysfs",
    }

    devices: list[DslValue[LambdaDeviceMount]] = field(default_factory=list)
    memory_size_in_kb: DslValue[int] | None = None
    mount_ro_sysfs: DslValue[bool] | None = None
    volumes: list[DslValue[LambdaVolumeMount]] = field(default_factory=list)


@dataclass
class LambdaDeviceMount(PropertyType):
    add_group_owner: DslValue[bool] | None = None
    path: DslValue[str] | None = None
    permission: DslValue[str] | None = None


@dataclass
class LambdaEventSource(PropertyType):
    topic: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class LambdaExecutionParameters(PropertyType):
    environment_variables: dict[str, DslValue[str]] = field(default_factory=dict)
    event_sources: list[DslValue[LambdaEventSource]] = field(default_factory=list)
    exec_args: list[DslValue[str]] = field(default_factory=list)
    input_payload_encoding_type: DslValue[str] | None = None
    linux_process_params: DslValue[LambdaLinuxProcessParams] | None = None
    max_idle_time_in_seconds: DslValue[int] | None = None
    max_instances_count: DslValue[int] | None = None
    max_queue_size: DslValue[int] | None = None
    pinned: DslValue[bool] | None = None
    status_timeout_in_seconds: DslValue[int] | None = None
    timeout_in_seconds: DslValue[int] | None = None


@dataclass
class LambdaFunctionRecipeSource(PropertyType):
    component_dependencies: dict[str, DslValue[ComponentDependencyRequirement]] = field(
        default_factory=dict
    )
    component_lambda_parameters: DslValue[LambdaExecutionParameters] | None = None
    component_name: DslValue[str] | None = None
    component_platforms: list[DslValue[ComponentPlatform]] = field(default_factory=list)
    component_version: DslValue[str] | None = None
    lambda_arn: DslValue[str] | None = None


@dataclass
class LambdaLinuxProcessParams(PropertyType):
    container_params: DslValue[LambdaContainerParams] | None = None
    isolation_mode: DslValue[str] | None = None


@dataclass
class LambdaVolumeMount(PropertyType):
    add_group_owner: DslValue[bool] | None = None
    destination_path: DslValue[str] | None = None
    permission: DslValue[str] | None = None
    source_path: DslValue[str] | None = None
