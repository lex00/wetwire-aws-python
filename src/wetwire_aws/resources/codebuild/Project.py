"""PropertyTypes for AWS::CodeBuild::Project."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Artifacts(PropertyType):
    type_: DslValue[str] | None = None
    artifact_identifier: DslValue[str] | None = None
    encryption_disabled: DslValue[bool] | None = None
    location: DslValue[str] | None = None
    name: DslValue[str] | None = None
    namespace_type: DslValue[str] | None = None
    override_artifact_name: DslValue[bool] | None = None
    packaging: DslValue[str] | None = None
    path: DslValue[str] | None = None


@dataclass
class BatchRestrictions(PropertyType):
    compute_types_allowed: list[DslValue[str]] = field(default_factory=list)
    maximum_builds_allowed: DslValue[int] | None = None


@dataclass
class BuildStatusConfig(PropertyType):
    context: DslValue[str] | None = None
    target_url: DslValue[str] | None = None


@dataclass
class CloudWatchLogsConfig(PropertyType):
    status: DslValue[str] | None = None
    group_name: DslValue[str] | None = None
    stream_name: DslValue[str] | None = None


@dataclass
class DockerServer(PropertyType):
    compute_type: DslValue[str] | None = None
    security_group_ids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class Environment(PropertyType):
    compute_type: DslValue[str] | None = None
    image: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    certificate: DslValue[str] | None = None
    docker_server: DslValue[DockerServer] | None = None
    environment_variables: list[DslValue[EnvironmentVariable]] = field(
        default_factory=list
    )
    fleet: DslValue[ProjectFleet] | None = None
    image_pull_credentials_type: DslValue[str] | None = None
    privileged_mode: DslValue[bool] | None = None
    registry_credential: DslValue[RegistryCredential] | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FilterGroup(PropertyType):
    pass


@dataclass
class GitSubmodulesConfig(PropertyType):
    fetch_submodules: DslValue[bool] | None = None


@dataclass
class LogsConfig(PropertyType):
    cloud_watch_logs: DslValue[CloudWatchLogsConfig] | None = None
    s3_logs: DslValue[S3LogsConfig] | None = None


@dataclass
class ProjectBuildBatchConfig(PropertyType):
    batch_report_mode: DslValue[str] | None = None
    combine_artifacts: DslValue[bool] | None = None
    restrictions: DslValue[BatchRestrictions] | None = None
    service_role: DslValue[str] | None = None
    timeout_in_mins: DslValue[int] | None = None


@dataclass
class ProjectCache(PropertyType):
    type_: DslValue[str] | None = None
    cache_namespace: DslValue[str] | None = None
    location: DslValue[str] | None = None
    modes: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ProjectFileSystemLocation(PropertyType):
    identifier: DslValue[str] | None = None
    location: DslValue[str] | None = None
    mount_point: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    mount_options: DslValue[str] | None = None


@dataclass
class ProjectFleet(PropertyType):
    fleet_arn: DslValue[str] | None = None


@dataclass
class ProjectSourceVersion(PropertyType):
    source_identifier: DslValue[str] | None = None
    source_version: DslValue[str] | None = None


@dataclass
class ProjectTriggers(PropertyType):
    build_type: DslValue[str] | None = None
    filter_groups: list[DslValue[FilterGroup]] = field(default_factory=list)
    pull_request_build_policy: DslValue[PullRequestBuildPolicy] | None = None
    scope_configuration: DslValue[ScopeConfiguration] | None = None
    webhook: DslValue[bool] | None = None


@dataclass
class PullRequestBuildPolicy(PropertyType):
    requires_comment_approval: DslValue[str] | None = None
    approver_roles: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RegistryCredential(PropertyType):
    credential: DslValue[str] | None = None
    credential_provider: DslValue[str] | None = None


@dataclass
class S3LogsConfig(PropertyType):
    status: DslValue[str] | None = None
    encryption_disabled: DslValue[bool] | None = None
    location: DslValue[str] | None = None


@dataclass
class ScopeConfiguration(PropertyType):
    name: DslValue[str] | None = None
    domain: DslValue[str] | None = None
    scope: DslValue[str] | None = None


@dataclass
class Source(PropertyType):
    type_: DslValue[str] | None = None
    auth: DslValue[SourceAuth] | None = None
    build_spec: DslValue[str] | None = None
    build_status_config: DslValue[BuildStatusConfig] | None = None
    git_clone_depth: DslValue[int] | None = None
    git_submodules_config: DslValue[GitSubmodulesConfig] | None = None
    insecure_ssl: DslValue[bool] | None = None
    location: DslValue[str] | None = None
    report_build_status: DslValue[bool] | None = None
    source_identifier: DslValue[str] | None = None


@dataclass
class SourceAuth(PropertyType):
    type_: DslValue[str] | None = None
    resource: DslValue[str] | None = None


@dataclass
class VpcConfig(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    subnets: list[DslValue[str]] = field(default_factory=list)
    vpc_id: DslValue[str] | None = None


@dataclass
class WebhookFilter(PropertyType):
    pattern: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    exclude_matched_pattern: DslValue[bool] | None = None
