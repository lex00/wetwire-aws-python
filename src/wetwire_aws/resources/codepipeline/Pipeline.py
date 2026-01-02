"""PropertyTypes for AWS::CodePipeline::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ActionDeclaration(PropertyType):
    action_type_id: ActionTypeId | None = None
    name: str | None = None
    commands: list[String] = field(default_factory=list)
    configuration: dict[str, Any] | None = None
    environment_variables: list[EnvironmentVariable] = field(default_factory=list)
    input_artifacts: list[InputArtifact] = field(default_factory=list)
    namespace: str | None = None
    output_artifacts: list[OutputArtifact] = field(default_factory=list)
    output_variables: list[String] = field(default_factory=list)
    region: str | None = None
    role_arn: str | None = None
    run_order: int | None = None
    timeout_in_minutes: int | None = None


@dataclass
class ActionTypeId(PropertyType):
    category: str | None = None
    owner: str | None = None
    provider: str | None = None
    version: str | None = None


@dataclass
class ArtifactStore(PropertyType):
    location: str | None = None
    type_: str | None = None
    encryption_key: EncryptionKey | None = None


@dataclass
class ArtifactStoreMap(PropertyType):
    artifact_store: ArtifactStore | None = None
    region: str | None = None


@dataclass
class BeforeEntryConditions(PropertyType):
    conditions: list[Condition] = field(default_factory=list)


@dataclass
class BlockerDeclaration(PropertyType):
    name: str | None = None
    type_: str | None = None


@dataclass
class Condition(PropertyType):
    result: str | None = None
    rules: list[RuleDeclaration] = field(default_factory=list)


@dataclass
class EncryptionKey(PropertyType):
    id: str | None = None
    type_: str | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    name: str | None = None
    value: str | None = None
    type_: str | None = None


@dataclass
class FailureConditions(PropertyType):
    conditions: list[Condition] = field(default_factory=list)
    result: str | None = None
    retry_configuration: RetryConfiguration | None = None


@dataclass
class GitBranchFilterCriteria(PropertyType):
    excludes: list[String] = field(default_factory=list)
    includes: list[String] = field(default_factory=list)


@dataclass
class GitConfiguration(PropertyType):
    source_action_name: str | None = None
    pull_request: list[GitPullRequestFilter] = field(default_factory=list)
    push: list[GitPushFilter] = field(default_factory=list)


@dataclass
class GitFilePathFilterCriteria(PropertyType):
    excludes: list[String] = field(default_factory=list)
    includes: list[String] = field(default_factory=list)


@dataclass
class GitPullRequestFilter(PropertyType):
    branches: GitBranchFilterCriteria | None = None
    events: list[String] = field(default_factory=list)
    file_paths: GitFilePathFilterCriteria | None = None


@dataclass
class GitPushFilter(PropertyType):
    branches: GitBranchFilterCriteria | None = None
    file_paths: GitFilePathFilterCriteria | None = None
    tags: GitTagFilterCriteria | None = None


@dataclass
class GitTagFilterCriteria(PropertyType):
    excludes: list[String] = field(default_factory=list)
    includes: list[String] = field(default_factory=list)


@dataclass
class InputArtifact(PropertyType):
    name: str | None = None


@dataclass
class OutputArtifact(PropertyType):
    name: str | None = None
    files: list[String] = field(default_factory=list)


@dataclass
class PipelineTriggerDeclaration(PropertyType):
    provider_type: str | None = None
    git_configuration: GitConfiguration | None = None


@dataclass
class RetryConfiguration(PropertyType):
    retry_mode: str | None = None


@dataclass
class RuleDeclaration(PropertyType):
    commands: list[String] = field(default_factory=list)
    configuration: dict[str, Any] | None = None
    input_artifacts: list[InputArtifact] = field(default_factory=list)
    name: str | None = None
    region: str | None = None
    role_arn: str | None = None
    rule_type_id: RuleTypeId | None = None


@dataclass
class RuleTypeId(PropertyType):
    category: str | None = None
    owner: str | None = None
    provider: str | None = None
    version: str | None = None


@dataclass
class StageDeclaration(PropertyType):
    actions: list[ActionDeclaration] = field(default_factory=list)
    name: str | None = None
    before_entry: BeforeEntryConditions | None = None
    blockers: list[BlockerDeclaration] = field(default_factory=list)
    on_failure: FailureConditions | None = None
    on_success: SuccessConditions | None = None


@dataclass
class StageTransition(PropertyType):
    reason: str | None = None
    stage_name: str | None = None


@dataclass
class SuccessConditions(PropertyType):
    conditions: list[Condition] = field(default_factory=list)


@dataclass
class VariableDeclaration(PropertyType):
    name: str | None = None
    default_value: str | None = None
    description: str | None = None
