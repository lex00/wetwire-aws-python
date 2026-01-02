"""PropertyTypes for AWS::Batch::JobDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ConsumableResourceProperties(PropertyType):
    consumable_resource_list: list[ConsumableResourceRequirement] = field(
        default_factory=list
    )


@dataclass
class ConsumableResourceRequirement(PropertyType):
    consumable_resource: str | None = None
    quantity: int | None = None


@dataclass
class ContainerProperties(PropertyType):
    image: str | None = None
    command: list[String] = field(default_factory=list)
    enable_execute_command: bool | None = None
    environment: list[Environment] = field(default_factory=list)
    ephemeral_storage: EphemeralStorage | None = None
    execution_role_arn: str | None = None
    fargate_platform_configuration: FargatePlatformConfiguration | None = None
    job_role_arn: str | None = None
    linux_parameters: LinuxParameters | None = None
    log_configuration: LogConfiguration | None = None
    memory: int | None = None
    mount_points: list[MountPoint] = field(default_factory=list)
    network_configuration: NetworkConfiguration | None = None
    privileged: bool | None = None
    readonly_root_filesystem: bool | None = None
    repository_credentials: RepositoryCredentials | None = None
    resource_requirements: list[ResourceRequirement] = field(default_factory=list)
    runtime_platform: RuntimePlatform | None = None
    secrets: list[Secret] = field(default_factory=list)
    ulimits: list[Ulimit] = field(default_factory=list)
    user: str | None = None
    vcpus: int | None = None
    volumes: list[Volume] = field(default_factory=list)


@dataclass
class Device(PropertyType):
    container_path: str | None = None
    host_path: str | None = None
    permissions: list[String] = field(default_factory=list)


@dataclass
class EFSAuthorizationConfig(PropertyType):
    access_point_id: str | None = None
    iam: str | None = None


@dataclass
class EFSVolumeConfiguration(PropertyType):
    file_system_id: str | None = None
    authorization_config: EFSAuthorizationConfig | None = None
    root_directory: str | None = None
    transit_encryption: str | None = None
    transit_encryption_port: int | None = None


@dataclass
class EcsProperties(PropertyType):
    task_properties: list[EcsTaskProperties] = field(default_factory=list)


@dataclass
class EcsTaskProperties(PropertyType):
    containers: list[TaskContainerProperties] = field(default_factory=list)
    enable_execute_command: bool | None = None
    ephemeral_storage: EphemeralStorage | None = None
    execution_role_arn: str | None = None
    ipc_mode: str | None = None
    network_configuration: NetworkConfiguration | None = None
    pid_mode: str | None = None
    platform_version: str | None = None
    runtime_platform: RuntimePlatform | None = None
    task_role_arn: str | None = None
    volumes: list[Volume] = field(default_factory=list)


@dataclass
class EksContainer(PropertyType):
    image: str | None = None
    args: list[String] = field(default_factory=list)
    command: list[String] = field(default_factory=list)
    env: list[EksContainerEnvironmentVariable] = field(default_factory=list)
    image_pull_policy: str | None = None
    name: str | None = None
    resources: EksContainerResourceRequirements | None = None
    security_context: EksContainerSecurityContext | None = None
    volume_mounts: list[EksContainerVolumeMount] = field(default_factory=list)


@dataclass
class EksContainerEnvironmentVariable(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class EksContainerResourceRequirements(PropertyType):
    limits: dict[str, String] = field(default_factory=dict)
    requests: dict[str, String] = field(default_factory=dict)


@dataclass
class EksContainerSecurityContext(PropertyType):
    allow_privilege_escalation: bool | None = None
    privileged: bool | None = None
    read_only_root_filesystem: bool | None = None
    run_as_group: int | None = None
    run_as_non_root: bool | None = None
    run_as_user: int | None = None


@dataclass
class EksContainerVolumeMount(PropertyType):
    mount_path: str | None = None
    name: str | None = None
    read_only: bool | None = None
    sub_path: str | None = None


@dataclass
class EksEmptyDir(PropertyType):
    medium: str | None = None
    size_limit: str | None = None


@dataclass
class EksHostPath(PropertyType):
    path: str | None = None


@dataclass
class EksMetadata(PropertyType):
    annotations: dict[str, String] = field(default_factory=dict)
    labels: dict[str, String] = field(default_factory=dict)
    namespace: str | None = None


@dataclass
class EksPersistentVolumeClaim(PropertyType):
    claim_name: str | None = None
    read_only: bool | None = None


@dataclass
class EksPodProperties(PropertyType):
    containers: list[EksContainer] = field(default_factory=list)
    dns_policy: str | None = None
    host_network: bool | None = None
    image_pull_secrets: list[ImagePullSecret] = field(default_factory=list)
    init_containers: list[EksContainer] = field(default_factory=list)
    metadata: EksMetadata | None = None
    service_account_name: str | None = None
    share_process_namespace: bool | None = None
    volumes: list[EksVolume] = field(default_factory=list)


@dataclass
class EksProperties(PropertyType):
    pod_properties: EksPodProperties | None = None


@dataclass
class EksSecret(PropertyType):
    secret_name: str | None = None
    optional: bool | None = None


@dataclass
class EksVolume(PropertyType):
    name: str | None = None
    empty_dir: EksEmptyDir | None = None
    host_path: EksHostPath | None = None
    persistent_volume_claim: EksPersistentVolumeClaim | None = None
    secret: EksSecret | None = None


@dataclass
class Environment(PropertyType):
    name: str | None = None
    value: str | None = None


@dataclass
class EphemeralStorage(PropertyType):
    size_in_gi_b: int | None = None


@dataclass
class EvaluateOnExit(PropertyType):
    action: str | None = None
    on_exit_code: str | None = None
    on_reason: str | None = None
    on_status_reason: str | None = None


@dataclass
class FargatePlatformConfiguration(PropertyType):
    platform_version: str | None = None


@dataclass
class FirelensConfiguration(PropertyType):
    type_: str | None = None
    options: dict[str, String] = field(default_factory=dict)


@dataclass
class Host(PropertyType):
    source_path: str | None = None


@dataclass
class ImagePullSecret(PropertyType):
    name: str | None = None


@dataclass
class JobTimeout(PropertyType):
    attempt_duration_seconds: int | None = None


@dataclass
class LinuxParameters(PropertyType):
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
class MultiNodeContainerProperties(PropertyType):
    image: str | None = None
    command: list[String] = field(default_factory=list)
    enable_execute_command: bool | None = None
    environment: list[Environment] = field(default_factory=list)
    ephemeral_storage: EphemeralStorage | None = None
    execution_role_arn: str | None = None
    instance_type: str | None = None
    job_role_arn: str | None = None
    linux_parameters: LinuxParameters | None = None
    log_configuration: LogConfiguration | None = None
    memory: int | None = None
    mount_points: list[MountPoint] = field(default_factory=list)
    privileged: bool | None = None
    readonly_root_filesystem: bool | None = None
    repository_credentials: RepositoryCredentials | None = None
    resource_requirements: list[ResourceRequirement] = field(default_factory=list)
    runtime_platform: RuntimePlatform | None = None
    secrets: list[Secret] = field(default_factory=list)
    ulimits: list[Ulimit] = field(default_factory=list)
    user: str | None = None
    vcpus: int | None = None
    volumes: list[Volume] = field(default_factory=list)


@dataclass
class MultiNodeEcsProperties(PropertyType):
    task_properties: list[MultiNodeEcsTaskProperties] = field(default_factory=list)


@dataclass
class MultiNodeEcsTaskProperties(PropertyType):
    containers: list[TaskContainerProperties] = field(default_factory=list)
    enable_execute_command: bool | None = None
    execution_role_arn: str | None = None
    ipc_mode: str | None = None
    pid_mode: str | None = None
    task_role_arn: str | None = None
    volumes: list[Volume] = field(default_factory=list)


@dataclass
class NetworkConfiguration(PropertyType):
    assign_public_ip: str | None = None


@dataclass
class NodeProperties(PropertyType):
    main_node: int | None = None
    node_range_properties: list[NodeRangeProperty] = field(default_factory=list)
    num_nodes: int | None = None


@dataclass
class NodeRangeProperty(PropertyType):
    target_nodes: str | None = None
    consumable_resource_properties: ConsumableResourceProperties | None = None
    container: MultiNodeContainerProperties | None = None
    ecs_properties: MultiNodeEcsProperties | None = None
    eks_properties: EksProperties | None = None
    instance_types: list[String] = field(default_factory=list)


@dataclass
class RepositoryCredentials(PropertyType):
    credentials_parameter: str | None = None


@dataclass
class ResourceRequirement(PropertyType):
    type_: str | None = None
    value: str | None = None


@dataclass
class ResourceRetentionPolicy(PropertyType):
    skip_deregister_on_update: bool | None = None


@dataclass
class RetryStrategy(PropertyType):
    attempts: int | None = None
    evaluate_on_exit: list[EvaluateOnExit] = field(default_factory=list)


@dataclass
class RuntimePlatform(PropertyType):
    cpu_architecture: str | None = None
    operating_system_family: str | None = None


@dataclass
class Secret(PropertyType):
    name: str | None = None
    value_from: str | None = None


@dataclass
class TaskContainerDependency(PropertyType):
    condition: str | None = None
    container_name: str | None = None


@dataclass
class TaskContainerProperties(PropertyType):
    image: str | None = None
    command: list[String] = field(default_factory=list)
    depends_on: list[TaskContainerDependency] = field(default_factory=list)
    environment: list[Environment] = field(default_factory=list)
    essential: bool | None = None
    firelens_configuration: FirelensConfiguration | None = None
    linux_parameters: LinuxParameters | None = None
    log_configuration: LogConfiguration | None = None
    mount_points: list[MountPoint] = field(default_factory=list)
    name: str | None = None
    privileged: bool | None = None
    readonly_root_filesystem: bool | None = None
    repository_credentials: RepositoryCredentials | None = None
    resource_requirements: list[ResourceRequirement] = field(default_factory=list)
    secrets: list[Secret] = field(default_factory=list)
    ulimits: list[Ulimit] = field(default_factory=list)
    user: str | None = None


@dataclass
class Tmpfs(PropertyType):
    container_path: str | None = None
    size: int | None = None
    mount_options: list[String] = field(default_factory=list)


@dataclass
class Ulimit(PropertyType):
    hard_limit: int | None = None
    name: str | None = None
    soft_limit: int | None = None


@dataclass
class Volume(PropertyType):
    efs_volume_configuration: EFSVolumeConfiguration | None = None
    host: Host | None = None
    name: str | None = None
