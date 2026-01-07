"""PropertyTypes for AWS::GameLift::ContainerGroupDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ContainerDependency(PropertyType):
    condition: DslValue[str] | None = None
    container_name: DslValue[str] | None = None


@dataclass
class ContainerEnvironment(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ContainerHealthCheck(PropertyType):
    command: list[DslValue[str]] = field(default_factory=list)
    interval: DslValue[int] | None = None
    retries: DslValue[int] | None = None
    start_period: DslValue[int] | None = None
    timeout: DslValue[int] | None = None


@dataclass
class ContainerMountPoint(PropertyType):
    instance_path: DslValue[str] | None = None
    access_level: DslValue[str] | None = None
    container_path: DslValue[str] | None = None


@dataclass
class ContainerPortRange(PropertyType):
    from_port: DslValue[int] | None = None
    protocol: DslValue[str] | None = None
    to_port: DslValue[int] | None = None


@dataclass
class GameServerContainerDefinition(PropertyType):
    container_name: DslValue[str] | None = None
    image_uri: DslValue[str] | None = None
    server_sdk_version: DslValue[str] | None = None
    depends_on: list[DslValue[ContainerDependency]] = field(default_factory=list)
    environment_override: list[DslValue[ContainerEnvironment]] = field(
        default_factory=list
    )
    mount_points: list[DslValue[ContainerMountPoint]] = field(default_factory=list)
    port_configuration: DslValue[PortConfiguration] | None = None
    resolved_image_digest: DslValue[str] | None = None


@dataclass
class PortConfiguration(PropertyType):
    container_port_ranges: list[DslValue[ContainerPortRange]] = field(
        default_factory=list
    )


@dataclass
class SupportContainerDefinition(PropertyType):
    container_name: DslValue[str] | None = None
    image_uri: DslValue[str] | None = None
    depends_on: list[DslValue[ContainerDependency]] = field(default_factory=list)
    environment_override: list[DslValue[ContainerEnvironment]] = field(
        default_factory=list
    )
    essential: DslValue[bool] | None = None
    health_check: DslValue[ContainerHealthCheck] | None = None
    memory_hard_limit_mebibytes: DslValue[int] | None = None
    mount_points: list[DslValue[ContainerMountPoint]] = field(default_factory=list)
    port_configuration: DslValue[PortConfiguration] | None = None
    resolved_image_digest: DslValue[str] | None = None
    vcpu: DslValue[float] | None = None
