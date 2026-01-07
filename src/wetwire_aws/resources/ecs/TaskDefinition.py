"""PropertyTypes for AWS::ECS::TaskDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuthorizationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "IAM",
    }

    access_point_id: DslValue[str] | None = None
    iam: DslValue[str] | None = None


@dataclass
class ContainerDefinition(PropertyType):
    image: DslValue[str] | None = None
    name: DslValue[str] | None = None
    command: list[DslValue[str]] = field(default_factory=list)
    cpu: DslValue[int] | None = None
    credential_specs: list[DslValue[str]] = field(default_factory=list)
    depends_on: list[DslValue[ContainerDependency]] = field(default_factory=list)
    disable_networking: DslValue[bool] | None = None
    dns_search_domains: list[DslValue[str]] = field(default_factory=list)
    dns_servers: list[DslValue[str]] = field(default_factory=list)
    docker_labels: dict[str, DslValue[str]] = field(default_factory=dict)
    docker_security_options: list[DslValue[str]] = field(default_factory=list)
    entry_point: list[DslValue[str]] = field(default_factory=list)
    environment: list[DslValue[KeyValuePair]] = field(default_factory=list)
    environment_files: list[DslValue[EnvironmentFile]] = field(default_factory=list)
    essential: DslValue[bool] | None = None
    extra_hosts: list[DslValue[HostEntry]] = field(default_factory=list)
    firelens_configuration: DslValue[FirelensConfiguration] | None = None
    health_check: DslValue[HealthCheck] | None = None
    hostname: DslValue[str] | None = None
    interactive: DslValue[bool] | None = None
    links: list[DslValue[str]] = field(default_factory=list)
    linux_parameters: DslValue[LinuxParameters] | None = None
    log_configuration: DslValue[LogConfiguration] | None = None
    memory: DslValue[int] | None = None
    memory_reservation: DslValue[int] | None = None
    mount_points: list[DslValue[MountPoint]] = field(default_factory=list)
    port_mappings: list[DslValue[PortMapping]] = field(default_factory=list)
    privileged: DslValue[bool] | None = None
    pseudo_terminal: DslValue[bool] | None = None
    readonly_root_filesystem: DslValue[bool] | None = None
    repository_credentials: DslValue[RepositoryCredentials] | None = None
    resource_requirements: list[DslValue[ResourceRequirement]] = field(
        default_factory=list
    )
    restart_policy: DslValue[RestartPolicy] | None = None
    secrets: list[DslValue[Secret]] = field(default_factory=list)
    start_timeout: DslValue[int] | None = None
    stop_timeout: DslValue[int] | None = None
    system_controls: list[DslValue[SystemControl]] = field(default_factory=list)
    ulimits: list[DslValue[Ulimit]] = field(default_factory=list)
    user: DslValue[str] | None = None
    version_consistency: DslValue[str] | None = None
    volumes_from: list[DslValue[VolumeFrom]] = field(default_factory=list)
    working_directory: DslValue[str] | None = None


@dataclass
class ContainerDependency(PropertyType):
    condition: DslValue[str] | None = None
    container_name: DslValue[str] | None = None


@dataclass
class Device(PropertyType):
    container_path: DslValue[str] | None = None
    host_path: DslValue[str] | None = None
    permissions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DockerVolumeConfiguration(PropertyType):
    autoprovision: DslValue[bool] | None = None
    driver: DslValue[str] | None = None
    driver_opts: dict[str, DslValue[str]] = field(default_factory=dict)
    labels: dict[str, DslValue[str]] = field(default_factory=dict)
    scope: DslValue[str] | None = None


@dataclass
class EFSVolumeConfiguration(PropertyType):
    filesystem_id: DslValue[str] | None = None
    authorization_config: DslValue[AuthorizationConfig] | None = None
    root_directory: DslValue[str] | None = None
    transit_encryption: DslValue[str] | None = None
    transit_encryption_port: DslValue[int] | None = None


@dataclass
class EnvironmentFile(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class EphemeralStorage(PropertyType):
    size_in_gi_b: DslValue[int] | None = None


@dataclass
class FSxAuthorizationConfig(PropertyType):
    credentials_parameter: DslValue[str] | None = None
    domain: DslValue[str] | None = None


@dataclass
class FSxWindowsFileServerVolumeConfiguration(PropertyType):
    file_system_id: DslValue[str] | None = None
    root_directory: DslValue[str] | None = None
    authorization_config: DslValue[FSxAuthorizationConfig] | None = None


@dataclass
class FirelensConfiguration(PropertyType):
    options: dict[str, DslValue[str]] = field(default_factory=dict)
    type_: DslValue[str] | None = None


@dataclass
class HealthCheck(PropertyType):
    command: list[DslValue[str]] = field(default_factory=list)
    interval: DslValue[int] | None = None
    retries: DslValue[int] | None = None
    start_period: DslValue[int] | None = None
    timeout: DslValue[int] | None = None


@dataclass
class HostEntry(PropertyType):
    hostname: DslValue[str] | None = None
    ip_address: DslValue[str] | None = None


@dataclass
class HostVolumeProperties(PropertyType):
    source_path: DslValue[str] | None = None


@dataclass
class KernelCapabilities(PropertyType):
    add: list[DslValue[str]] = field(default_factory=list)
    drop: list[DslValue[str]] = field(default_factory=list)


@dataclass
class KeyValuePair(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class LinuxParameters(PropertyType):
    capabilities: DslValue[KernelCapabilities] | None = None
    devices: list[DslValue[Device]] = field(default_factory=list)
    init_process_enabled: DslValue[bool] | None = None
    max_swap: DslValue[int] | None = None
    shared_memory_size: DslValue[int] | None = None
    swappiness: DslValue[int] | None = None
    tmpfs: list[DslValue[Tmpfs]] = field(default_factory=list)


@dataclass
class LogConfiguration(PropertyType):
    log_driver: DslValue[str] | None = None
    options: dict[str, DslValue[str]] = field(default_factory=dict)
    secret_options: list[DslValue[Secret]] = field(default_factory=list)


@dataclass
class MountPoint(PropertyType):
    container_path: DslValue[str] | None = None
    read_only: DslValue[bool] | None = None
    source_volume: DslValue[str] | None = None


@dataclass
class PortMapping(PropertyType):
    app_protocol: DslValue[str] | None = None
    container_port: DslValue[int] | None = None
    container_port_range: DslValue[str] | None = None
    host_port: DslValue[int] | None = None
    name: DslValue[str] | None = None
    protocol: DslValue[str] | None = None


@dataclass
class ProxyConfiguration(PropertyType):
    container_name: DslValue[str] | None = None
    proxy_configuration_properties: list[DslValue[KeyValuePair]] = field(
        default_factory=list
    )
    type_: DslValue[str] | None = None


@dataclass
class RepositoryCredentials(PropertyType):
    credentials_parameter: DslValue[str] | None = None


@dataclass
class ResourceRequirement(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class RestartPolicy(PropertyType):
    enabled: DslValue[bool] | None = None
    ignored_exit_codes: list[DslValue[int]] = field(default_factory=list)
    restart_attempt_period: DslValue[int] | None = None


@dataclass
class RuntimePlatform(PropertyType):
    cpu_architecture: DslValue[str] | None = None
    operating_system_family: DslValue[str] | None = None


@dataclass
class Secret(PropertyType):
    name: DslValue[str] | None = None
    value_from: DslValue[str] | None = None


@dataclass
class SystemControl(PropertyType):
    namespace: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class TaskDefinitionPlacementConstraint(PropertyType):
    type_: DslValue[str] | None = None
    expression: DslValue[str] | None = None


@dataclass
class Tmpfs(PropertyType):
    size: DslValue[int] | None = None
    container_path: DslValue[str] | None = None
    mount_options: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Ulimit(PropertyType):
    hard_limit: DslValue[int] | None = None
    name: DslValue[str] | None = None
    soft_limit: DslValue[int] | None = None


@dataclass
class Volume(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_volume_configuration": "EFSVolumeConfiguration",
    }

    configured_at_launch: DslValue[bool] | None = None
    docker_volume_configuration: DslValue[DockerVolumeConfiguration] | None = None
    efs_volume_configuration: DslValue[EFSVolumeConfiguration] | None = None
    f_sx_windows_file_server_volume_configuration: (
        DslValue[FSxWindowsFileServerVolumeConfiguration] | None
    ) = None
    host: DslValue[HostVolumeProperties] | None = None
    name: DslValue[str] | None = None


@dataclass
class VolumeFrom(PropertyType):
    read_only: DslValue[bool] | None = None
    source_container: DslValue[str] | None = None
