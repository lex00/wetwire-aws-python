"""PropertyTypes for AWS::ECS::TaskDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthorizationConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "iam": "IAM",
    }

    access_point_id: str | None = None
    iam: str | None = None


@dataclass
class ContainerDefinition(PropertyType):
    image: str | None = None
    name: str | None = None
    command: list[String] = field(default_factory=list)
    cpu: int | None = None
    credential_specs: list[String] = field(default_factory=list)
    depends_on: list[ContainerDependency] = field(default_factory=list)
    disable_networking: bool | None = None
    dns_search_domains: list[String] = field(default_factory=list)
    dns_servers: list[String] = field(default_factory=list)
    docker_labels: dict[str, String] = field(default_factory=dict)
    docker_security_options: list[String] = field(default_factory=list)
    entry_point: list[String] = field(default_factory=list)
    environment: list[KeyValuePair] = field(default_factory=list)
    environment_files: list[EnvironmentFile] = field(default_factory=list)
    essential: bool | None = None
    extra_hosts: list[HostEntry] = field(default_factory=list)
    firelens_configuration: FirelensConfiguration | None = None
    health_check: HealthCheck | None = None
    hostname: str | None = None
    interactive: bool | None = None
    links: list[String] = field(default_factory=list)
    linux_parameters: LinuxParameters | None = None
    log_configuration: LogConfiguration | None = None
    memory: int | None = None
    memory_reservation: int | None = None
    mount_points: list[MountPoint] = field(default_factory=list)
    port_mappings: list[PortMapping] = field(default_factory=list)
    privileged: bool | None = None
    pseudo_terminal: bool | None = None
    readonly_root_filesystem: bool | None = None
    repository_credentials: RepositoryCredentials | None = None
    resource_requirements: list[ResourceRequirement] = field(default_factory=list)
    restart_policy: RestartPolicy | None = None
    secrets: list[Secret] = field(default_factory=list)
    start_timeout: int | None = None
    stop_timeout: int | None = None
    system_controls: list[SystemControl] = field(default_factory=list)
    ulimits: list[Ulimit] = field(default_factory=list)
    user: str | None = None
    version_consistency: str | None = None
    volumes_from: list[VolumeFrom] = field(default_factory=list)
    working_directory: str | None = None


@dataclass
class ContainerDependency(PropertyType):
    condition: str | None = None
    container_name: str | None = None


@dataclass
class Device(PropertyType):
    container_path: str | None = None
    host_path: str | None = None
    permissions: list[String] = field(default_factory=list)


@dataclass
class DockerVolumeConfiguration(PropertyType):
    autoprovision: bool | None = None
    driver: str | None = None
    driver_opts: dict[str, String] = field(default_factory=dict)
    labels: dict[str, String] = field(default_factory=dict)
    scope: str | None = None


@dataclass
class EFSVolumeConfiguration(PropertyType):
    filesystem_id: str | None = None
    authorization_config: AuthorizationConfig | None = None
    root_directory: str | None = None
    transit_encryption: str | None = None
    transit_encryption_port: int | None = None


@dataclass
class EnvironmentFile(PropertyType):
    type_: str | None = None
    value: str | None = None


@dataclass
class EphemeralStorage(PropertyType):
    size_in_gi_b: int | None = None


@dataclass
class FSxAuthorizationConfig(PropertyType):
    credentials_parameter: str | None = None
    domain: str | None = None


@dataclass
class FSxWindowsFileServerVolumeConfiguration(PropertyType):
    file_system_id: str | None = None
    root_directory: str | None = None
    authorization_config: FSxAuthorizationConfig | None = None


@dataclass
class FirelensConfiguration(PropertyType):
    options: dict[str, String] = field(default_factory=dict)
    type_: str | None = None


@dataclass
class HealthCheck(PropertyType):
    command: list[String] = field(default_factory=list)
    interval: int | None = None
    retries: int | None = None
    start_period: int | None = None
    timeout: int | None = None


@dataclass
class HostEntry(PropertyType):
    hostname: str | None = None
    ip_address: str | None = None


@dataclass
class HostVolumeProperties(PropertyType):
    source_path: str | None = None


@dataclass
class KernelCapabilities(PropertyType):
    add: list[String] = field(default_factory=list)
    drop: list[String] = field(default_factory=list)


@dataclass
class KeyValuePair(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class LinuxParameters(PropertyType):
    capabilities: KernelCapabilities | None = None
    devices: list[Device] = field(default_factory=list)
    init_process_enabled: bool | None = None
    max_swap: int | None = None
    shared_memory_size: int | None = None
    swappiness: int | None = None
    tmpfs: list[Tmpfs] = field(default_factory=list)


@dataclass
class LogConfiguration(PropertyType):
    log_driver: str | None = None
    options: dict[str, String] = field(default_factory=dict)
    secret_options: list[Secret] = field(default_factory=list)


@dataclass
class MountPoint(PropertyType):
    container_path: str | None = None
    read_only: bool | None = None
    source_volume: str | None = None


@dataclass
class PortMapping(PropertyType):
    app_protocol: str | None = None
    container_port: int | None = None
    container_port_range: str | None = None
    host_port: int | None = None
    name: str | None = None
    protocol: str | None = None


@dataclass
class ProxyConfiguration(PropertyType):
    container_name: str | None = None
    proxy_configuration_properties: list[KeyValuePair] = field(default_factory=list)
    type_: str | None = None


@dataclass
class RepositoryCredentials(PropertyType):
    credentials_parameter: str | None = None


@dataclass
class ResourceRequirement(PropertyType):
    type_: str | None = None
    value: str | None = None


@dataclass
class RestartPolicy(PropertyType):
    enabled: bool | None = None
    ignored_exit_codes: list[Integer] = field(default_factory=list)
    restart_attempt_period: int | None = None


@dataclass
class RuntimePlatform(PropertyType):
    cpu_architecture: str | None = None
    operating_system_family: str | None = None


@dataclass
class Secret(PropertyType):
    name: str | None = None
    value_from: str | None = None


@dataclass
class SystemControl(PropertyType):
    namespace: str | None = None
    value: str | None = None


@dataclass
class TaskDefinitionPlacementConstraint(PropertyType):
    type_: str | None = None
    expression: str | None = None


@dataclass
class Tmpfs(PropertyType):
    size: int | None = None
    container_path: str | None = None
    mount_options: list[String] = field(default_factory=list)


@dataclass
class Ulimit(PropertyType):
    hard_limit: int | None = None
    name: str | None = None
    soft_limit: int | None = None


@dataclass
class Volume(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "efs_volume_configuration": "EFSVolumeConfiguration",
    }

    configured_at_launch: bool | None = None
    docker_volume_configuration: DockerVolumeConfiguration | None = None
    efs_volume_configuration: EFSVolumeConfiguration | None = None
    f_sx_windows_file_server_volume_configuration: (
        FSxWindowsFileServerVolumeConfiguration | None
    ) = None
    host: HostVolumeProperties | None = None
    name: str | None = None


@dataclass
class VolumeFrom(PropertyType):
    read_only: bool | None = None
    source_container: str | None = None
