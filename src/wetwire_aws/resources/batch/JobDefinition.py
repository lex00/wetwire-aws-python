"""PropertyTypes for AWS::Batch::JobDefinition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ConsumableResourceProperties(PropertyType):
    consumable_resource_list: list[DslValue[ConsumableResourceRequirement]] = field(
        default_factory=list
    )


@dataclass
class ConsumableResourceRequirement(PropertyType):
    consumable_resource: DslValue[str] | None = None
    quantity: DslValue[int] | None = None


@dataclass
class ContainerProperties(PropertyType):
    image: DslValue[str] | None = None
    command: list[DslValue[str]] = field(default_factory=list)
    enable_execute_command: DslValue[bool] | None = None
    environment: list[DslValue[Environment]] = field(default_factory=list)
    ephemeral_storage: DslValue[EphemeralStorage] | None = None
    execution_role_arn: DslValue[str] | None = None
    fargate_platform_configuration: DslValue[FargatePlatformConfiguration] | None = None
    job_role_arn: DslValue[str] | None = None
    linux_parameters: DslValue[LinuxParameters] | None = None
    log_configuration: DslValue[LogConfiguration] | None = None
    memory: DslValue[int] | None = None
    mount_points: list[DslValue[MountPoint]] = field(default_factory=list)
    network_configuration: DslValue[NetworkConfiguration] | None = None
    privileged: DslValue[bool] | None = None
    readonly_root_filesystem: DslValue[bool] | None = None
    repository_credentials: DslValue[RepositoryCredentials] | None = None
    resource_requirements: list[DslValue[ResourceRequirement]] = field(
        default_factory=list
    )
    runtime_platform: DslValue[RuntimePlatform] | None = None
    secrets: list[DslValue[Secret]] = field(default_factory=list)
    ulimits: list[DslValue[Ulimit]] = field(default_factory=list)
    user: DslValue[str] | None = None
    vcpus: DslValue[int] | None = None
    volumes: list[DslValue[Volume]] = field(default_factory=list)


@dataclass
class Device(PropertyType):
    container_path: DslValue[str] | None = None
    host_path: DslValue[str] | None = None
    permissions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class EFSAuthorizationConfig(PropertyType):
    access_point_id: DslValue[str] | None = None
    iam: DslValue[str] | None = None


@dataclass
class EFSVolumeConfiguration(PropertyType):
    file_system_id: DslValue[str] | None = None
    authorization_config: DslValue[EFSAuthorizationConfig] | None = None
    root_directory: DslValue[str] | None = None
    transit_encryption: DslValue[str] | None = None
    transit_encryption_port: DslValue[int] | None = None


@dataclass
class EcsProperties(PropertyType):
    task_properties: list[DslValue[EcsTaskProperties]] = field(default_factory=list)


@dataclass
class EcsTaskProperties(PropertyType):
    containers: list[DslValue[TaskContainerProperties]] = field(default_factory=list)
    enable_execute_command: DslValue[bool] | None = None
    ephemeral_storage: DslValue[EphemeralStorage] | None = None
    execution_role_arn: DslValue[str] | None = None
    ipc_mode: DslValue[str] | None = None
    network_configuration: DslValue[NetworkConfiguration] | None = None
    pid_mode: DslValue[str] | None = None
    platform_version: DslValue[str] | None = None
    runtime_platform: DslValue[RuntimePlatform] | None = None
    task_role_arn: DslValue[str] | None = None
    volumes: list[DslValue[Volume]] = field(default_factory=list)


@dataclass
class EksContainer(PropertyType):
    image: DslValue[str] | None = None
    args: list[DslValue[str]] = field(default_factory=list)
    command: list[DslValue[str]] = field(default_factory=list)
    env: list[DslValue[EksContainerEnvironmentVariable]] = field(default_factory=list)
    image_pull_policy: DslValue[str] | None = None
    name: DslValue[str] | None = None
    resources: DslValue[EksContainerResourceRequirements] | None = None
    security_context: DslValue[EksContainerSecurityContext] | None = None
    volume_mounts: list[DslValue[EksContainerVolumeMount]] = field(default_factory=list)


@dataclass
class EksContainerEnvironmentVariable(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class EksContainerResourceRequirements(PropertyType):
    limits: dict[str, DslValue[str]] = field(default_factory=dict)
    requests: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class EksContainerSecurityContext(PropertyType):
    allow_privilege_escalation: DslValue[bool] | None = None
    privileged: DslValue[bool] | None = None
    read_only_root_filesystem: DslValue[bool] | None = None
    run_as_group: DslValue[int] | None = None
    run_as_non_root: DslValue[bool] | None = None
    run_as_user: DslValue[int] | None = None


@dataclass
class EksContainerVolumeMount(PropertyType):
    mount_path: DslValue[str] | None = None
    name: DslValue[str] | None = None
    read_only: DslValue[bool] | None = None
    sub_path: DslValue[str] | None = None


@dataclass
class EksEmptyDir(PropertyType):
    medium: DslValue[str] | None = None
    size_limit: DslValue[str] | None = None


@dataclass
class EksHostPath(PropertyType):
    path: DslValue[str] | None = None


@dataclass
class EksMetadata(PropertyType):
    annotations: dict[str, DslValue[str]] = field(default_factory=dict)
    labels: dict[str, DslValue[str]] = field(default_factory=dict)
    namespace: DslValue[str] | None = None


@dataclass
class EksPersistentVolumeClaim(PropertyType):
    claim_name: DslValue[str] | None = None
    read_only: DslValue[bool] | None = None


@dataclass
class EksPodProperties(PropertyType):
    containers: list[DslValue[EksContainer]] = field(default_factory=list)
    dns_policy: DslValue[str] | None = None
    host_network: DslValue[bool] | None = None
    image_pull_secrets: list[DslValue[ImagePullSecret]] = field(default_factory=list)
    init_containers: list[DslValue[EksContainer]] = field(default_factory=list)
    metadata: DslValue[EksMetadata] | None = None
    service_account_name: DslValue[str] | None = None
    share_process_namespace: DslValue[bool] | None = None
    volumes: list[DslValue[EksVolume]] = field(default_factory=list)


@dataclass
class EksProperties(PropertyType):
    pod_properties: DslValue[EksPodProperties] | None = None


@dataclass
class EksSecret(PropertyType):
    secret_name: DslValue[str] | None = None
    optional: DslValue[bool] | None = None


@dataclass
class EksVolume(PropertyType):
    name: DslValue[str] | None = None
    empty_dir: DslValue[EksEmptyDir] | None = None
    host_path: DslValue[EksHostPath] | None = None
    persistent_volume_claim: DslValue[EksPersistentVolumeClaim] | None = None
    secret: DslValue[EksSecret] | None = None


@dataclass
class Environment(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class EphemeralStorage(PropertyType):
    size_in_gi_b: DslValue[int] | None = None


@dataclass
class EvaluateOnExit(PropertyType):
    action: DslValue[str] | None = None
    on_exit_code: DslValue[str] | None = None
    on_reason: DslValue[str] | None = None
    on_status_reason: DslValue[str] | None = None


@dataclass
class FargatePlatformConfiguration(PropertyType):
    platform_version: DslValue[str] | None = None


@dataclass
class FirelensConfiguration(PropertyType):
    type_: DslValue[str] | None = None
    options: dict[str, DslValue[str]] = field(default_factory=dict)


@dataclass
class Host(PropertyType):
    source_path: DslValue[str] | None = None


@dataclass
class ImagePullSecret(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class JobTimeout(PropertyType):
    attempt_duration_seconds: DslValue[int] | None = None


@dataclass
class LinuxParameters(PropertyType):
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
class MultiNodeContainerProperties(PropertyType):
    image: DslValue[str] | None = None
    command: list[DslValue[str]] = field(default_factory=list)
    enable_execute_command: DslValue[bool] | None = None
    environment: list[DslValue[Environment]] = field(default_factory=list)
    ephemeral_storage: DslValue[EphemeralStorage] | None = None
    execution_role_arn: DslValue[str] | None = None
    instance_type: DslValue[str] | None = None
    job_role_arn: DslValue[str] | None = None
    linux_parameters: DslValue[LinuxParameters] | None = None
    log_configuration: DslValue[LogConfiguration] | None = None
    memory: DslValue[int] | None = None
    mount_points: list[DslValue[MountPoint]] = field(default_factory=list)
    privileged: DslValue[bool] | None = None
    readonly_root_filesystem: DslValue[bool] | None = None
    repository_credentials: DslValue[RepositoryCredentials] | None = None
    resource_requirements: list[DslValue[ResourceRequirement]] = field(
        default_factory=list
    )
    runtime_platform: DslValue[RuntimePlatform] | None = None
    secrets: list[DslValue[Secret]] = field(default_factory=list)
    ulimits: list[DslValue[Ulimit]] = field(default_factory=list)
    user: DslValue[str] | None = None
    vcpus: DslValue[int] | None = None
    volumes: list[DslValue[Volume]] = field(default_factory=list)


@dataclass
class MultiNodeEcsProperties(PropertyType):
    task_properties: list[DslValue[MultiNodeEcsTaskProperties]] = field(
        default_factory=list
    )


@dataclass
class MultiNodeEcsTaskProperties(PropertyType):
    containers: list[DslValue[TaskContainerProperties]] = field(default_factory=list)
    enable_execute_command: DslValue[bool] | None = None
    execution_role_arn: DslValue[str] | None = None
    ipc_mode: DslValue[str] | None = None
    pid_mode: DslValue[str] | None = None
    task_role_arn: DslValue[str] | None = None
    volumes: list[DslValue[Volume]] = field(default_factory=list)


@dataclass
class NetworkConfiguration(PropertyType):
    assign_public_ip: DslValue[str] | None = None


@dataclass
class NodeProperties(PropertyType):
    main_node: DslValue[int] | None = None
    node_range_properties: list[DslValue[NodeRangeProperty]] = field(
        default_factory=list
    )
    num_nodes: DslValue[int] | None = None


@dataclass
class NodeRangeProperty(PropertyType):
    target_nodes: DslValue[str] | None = None
    consumable_resource_properties: DslValue[ConsumableResourceProperties] | None = None
    container: DslValue[MultiNodeContainerProperties] | None = None
    ecs_properties: DslValue[MultiNodeEcsProperties] | None = None
    eks_properties: DslValue[EksProperties] | None = None
    instance_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RepositoryCredentials(PropertyType):
    credentials_parameter: DslValue[str] | None = None


@dataclass
class ResourceRequirement(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class ResourceRetentionPolicy(PropertyType):
    skip_deregister_on_update: DslValue[bool] | None = None


@dataclass
class RetryStrategy(PropertyType):
    attempts: DslValue[int] | None = None
    evaluate_on_exit: list[DslValue[EvaluateOnExit]] = field(default_factory=list)


@dataclass
class RuntimePlatform(PropertyType):
    cpu_architecture: DslValue[str] | None = None
    operating_system_family: DslValue[str] | None = None


@dataclass
class Secret(PropertyType):
    name: DslValue[str] | None = None
    value_from: DslValue[str] | None = None


@dataclass
class TaskContainerDependency(PropertyType):
    condition: DslValue[str] | None = None
    container_name: DslValue[str] | None = None


@dataclass
class TaskContainerProperties(PropertyType):
    image: DslValue[str] | None = None
    command: list[DslValue[str]] = field(default_factory=list)
    depends_on: list[DslValue[TaskContainerDependency]] = field(default_factory=list)
    environment: list[DslValue[Environment]] = field(default_factory=list)
    essential: DslValue[bool] | None = None
    firelens_configuration: DslValue[FirelensConfiguration] | None = None
    linux_parameters: DslValue[LinuxParameters] | None = None
    log_configuration: DslValue[LogConfiguration] | None = None
    mount_points: list[DslValue[MountPoint]] = field(default_factory=list)
    name: DslValue[str] | None = None
    privileged: DslValue[bool] | None = None
    readonly_root_filesystem: DslValue[bool] | None = None
    repository_credentials: DslValue[RepositoryCredentials] | None = None
    resource_requirements: list[DslValue[ResourceRequirement]] = field(
        default_factory=list
    )
    secrets: list[DslValue[Secret]] = field(default_factory=list)
    ulimits: list[DslValue[Ulimit]] = field(default_factory=list)
    user: DslValue[str] | None = None


@dataclass
class Tmpfs(PropertyType):
    container_path: DslValue[str] | None = None
    size: DslValue[int] | None = None
    mount_options: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Ulimit(PropertyType):
    hard_limit: DslValue[int] | None = None
    name: DslValue[str] | None = None
    soft_limit: DslValue[int] | None = None


@dataclass
class Volume(PropertyType):
    efs_volume_configuration: DslValue[EFSVolumeConfiguration] | None = None
    host: DslValue[Host] | None = None
    name: DslValue[str] | None = None
