"""PropertyTypes for AWS::GameLift::ContainerGroupDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ContainerDependency(PropertyType):
    condition: str | None = None
    container_name: str | None = None


@dataclass
class ContainerEnvironment(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class ContainerHealthCheck(PropertyType):
    command: list[String] = field(default_factory=list)
    interval: int | None = None
    retries: int | None = None
    start_period: int | None = None
    timeout: int | None = None


@dataclass
class ContainerMountPoint(PropertyType):
    instance_path: str | None = None
    access_level: str | None = None
    container_path: str | None = None


@dataclass
class ContainerPortRange(PropertyType):
    from_port: int | None = None
    protocol: str | None = None
    to_port: int | None = None


@dataclass
class GameServerContainerDefinition(PropertyType):
    container_name: str | None = None
    image_uri: str | None = None
    server_sdk_version: str | None = None
    depends_on: list[ContainerDependency] = field(default_factory=list)
    environment_override: list[ContainerEnvironment] = field(default_factory=list)
    mount_points: list[ContainerMountPoint] = field(default_factory=list)
    port_configuration: PortConfiguration | None = None
    resolved_image_digest: str | None = None


@dataclass
class PortConfiguration(PropertyType):
    container_port_ranges: list[ContainerPortRange] = field(default_factory=list)


@dataclass
class SupportContainerDefinition(PropertyType):
    container_name: str | None = None
    image_uri: str | None = None
    depends_on: list[ContainerDependency] = field(default_factory=list)
    environment_override: list[ContainerEnvironment] = field(default_factory=list)
    essential: bool | None = None
    health_check: ContainerHealthCheck | None = None
    memory_hard_limit_mebibytes: int | None = None
    mount_points: list[ContainerMountPoint] = field(default_factory=list)
    port_configuration: PortConfiguration | None = None
    resolved_image_digest: str | None = None
    vcpu: float | None = None
