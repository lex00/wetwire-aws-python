"""PropertyTypes for AWS::CodeBuild::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Artifacts(PropertyType):
    type_: str | None = None
    artifact_identifier: str | None = None
    encryption_disabled: bool | None = None
    location: str | None = None
    name: str | None = None
    namespace_type: str | None = None
    override_artifact_name: bool | None = None
    packaging: str | None = None
    path: str | None = None


@dataclass
class BatchRestrictions(PropertyType):
    compute_types_allowed: list[String] = field(default_factory=list)
    maximum_builds_allowed: int | None = None


@dataclass
class BuildStatusConfig(PropertyType):
    context: str | None = None
    target_url: str | None = None


@dataclass
class CloudWatchLogsConfig(PropertyType):
    status: str | None = None
    group_name: str | None = None
    stream_name: str | None = None


@dataclass
class DockerServer(PropertyType):
    compute_type: str | None = None
    security_group_ids: list[String] = field(default_factory=list)


@dataclass
class Environment(PropertyType):
    compute_type: str | None = None
    image: str | None = None
    type_: str | None = None
    certificate: str | None = None
    docker_server: DockerServer | None = None
    environment_variables: list[EnvironmentVariable] = field(default_factory=list)
    fleet: ProjectFleet | None = None
    image_pull_credentials_type: str | None = None
    privileged_mode: bool | None = None
    registry_credential: RegistryCredential | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    name: str | None = None
    value: str | None = None
    type_: str | None = None


@dataclass
class FilterGroup(PropertyType):
    pass


@dataclass
class GitSubmodulesConfig(PropertyType):
    fetch_submodules: bool | None = None


@dataclass
class LogsConfig(PropertyType):
    cloud_watch_logs: CloudWatchLogsConfig | None = None
    s3_logs: S3LogsConfig | None = None


@dataclass
class ProjectBuildBatchConfig(PropertyType):
    batch_report_mode: str | None = None
    combine_artifacts: bool | None = None
    restrictions: BatchRestrictions | None = None
    service_role: str | None = None
    timeout_in_mins: int | None = None


@dataclass
class ProjectCache(PropertyType):
    type_: str | None = None
    cache_namespace: str | None = None
    location: str | None = None
    modes: list[String] = field(default_factory=list)


@dataclass
class ProjectFileSystemLocation(PropertyType):
    identifier: str | None = None
    location: str | None = None
    mount_point: str | None = None
    type_: str | None = None
    mount_options: str | None = None


@dataclass
class ProjectFleet(PropertyType):
    fleet_arn: str | None = None


@dataclass
class ProjectSourceVersion(PropertyType):
    source_identifier: str | None = None
    source_version: str | None = None


@dataclass
class ProjectTriggers(PropertyType):
    build_type: str | None = None
    filter_groups: list[FilterGroup] = field(default_factory=list)
    pull_request_build_policy: PullRequestBuildPolicy | None = None
    scope_configuration: ScopeConfiguration | None = None
    webhook: bool | None = None


@dataclass
class PullRequestBuildPolicy(PropertyType):
    requires_comment_approval: str | None = None
    approver_roles: list[String] = field(default_factory=list)


@dataclass
class RegistryCredential(PropertyType):
    credential: str | None = None
    credential_provider: str | None = None


@dataclass
class S3LogsConfig(PropertyType):
    status: str | None = None
    encryption_disabled: bool | None = None
    location: str | None = None


@dataclass
class ScopeConfiguration(PropertyType):
    name: str | None = None
    domain: str | None = None
    scope: str | None = None


@dataclass
class Source(PropertyType):
    type_: str | None = None
    auth: SourceAuth | None = None
    build_spec: str | None = None
    build_status_config: BuildStatusConfig | None = None
    git_clone_depth: int | None = None
    git_submodules_config: GitSubmodulesConfig | None = None
    insecure_ssl: bool | None = None
    location: str | None = None
    report_build_status: bool | None = None
    source_identifier: str | None = None


@dataclass
class SourceAuth(PropertyType):
    type_: str | None = None
    resource: str | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    subnets: list[String] = field(default_factory=list)
    vpc_id: str | None = None


@dataclass
class WebhookFilter(PropertyType):
    pattern: str | None = None
    type_: str | None = None
    exclude_matched_pattern: bool | None = None
