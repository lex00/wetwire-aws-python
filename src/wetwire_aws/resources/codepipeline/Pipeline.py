"""PropertyTypes for AWS::CodePipeline::Pipeline."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ActionDeclaration(PropertyType):
    action_type_id: DslValue[ActionTypeId] | None = None
    name: DslValue[str] | None = None
    commands: list[DslValue[str]] = field(default_factory=list)
    configuration: DslValue[dict[str, Any]] | None = None
    environment_variables: list[DslValue[EnvironmentVariable]] = field(
        default_factory=list
    )
    input_artifacts: list[DslValue[InputArtifact]] = field(default_factory=list)
    namespace: DslValue[str] | None = None
    output_artifacts: list[DslValue[OutputArtifact]] = field(default_factory=list)
    output_variables: list[DslValue[str]] = field(default_factory=list)
    region: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    run_order: DslValue[int] | None = None
    timeout_in_minutes: DslValue[int] | None = None


@dataclass
class ActionTypeId(PropertyType):
    category: DslValue[str] | None = None
    owner: DslValue[str] | None = None
    provider: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class ArtifactStore(PropertyType):
    location: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    encryption_key: DslValue[EncryptionKey] | None = None


@dataclass
class ArtifactStoreMap(PropertyType):
    artifact_store: DslValue[ArtifactStore] | None = None
    region: DslValue[str] | None = None


@dataclass
class BeforeEntryConditions(PropertyType):
    conditions: list[DslValue[Condition]] = field(default_factory=list)


@dataclass
class BlockerDeclaration(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class Condition(PropertyType):
    result: DslValue[str] | None = None
    rules: list[DslValue[RuleDeclaration]] = field(default_factory=list)


@dataclass
class EncryptionKey(PropertyType):
    id: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class EnvironmentVariable(PropertyType):
    name: DslValue[str] | None = None
    value: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class FailureConditions(PropertyType):
    conditions: list[DslValue[Condition]] = field(default_factory=list)
    result: DslValue[str] | None = None
    retry_configuration: DslValue[RetryConfiguration] | None = None


@dataclass
class GitBranchFilterCriteria(PropertyType):
    excludes: list[DslValue[str]] = field(default_factory=list)
    includes: list[DslValue[str]] = field(default_factory=list)


@dataclass
class GitConfiguration(PropertyType):
    source_action_name: DslValue[str] | None = None
    pull_request: list[DslValue[GitPullRequestFilter]] = field(default_factory=list)
    push: list[DslValue[GitPushFilter]] = field(default_factory=list)


@dataclass
class GitFilePathFilterCriteria(PropertyType):
    excludes: list[DslValue[str]] = field(default_factory=list)
    includes: list[DslValue[str]] = field(default_factory=list)


@dataclass
class GitPullRequestFilter(PropertyType):
    branches: DslValue[GitBranchFilterCriteria] | None = None
    events: list[DslValue[str]] = field(default_factory=list)
    file_paths: DslValue[GitFilePathFilterCriteria] | None = None


@dataclass
class GitPushFilter(PropertyType):
    branches: DslValue[GitBranchFilterCriteria] | None = None
    file_paths: DslValue[GitFilePathFilterCriteria] | None = None
    tags: DslValue[GitTagFilterCriteria] | None = None


@dataclass
class GitTagFilterCriteria(PropertyType):
    excludes: list[DslValue[str]] = field(default_factory=list)
    includes: list[DslValue[str]] = field(default_factory=list)


@dataclass
class InputArtifact(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class OutputArtifact(PropertyType):
    name: DslValue[str] | None = None
    files: list[DslValue[str]] = field(default_factory=list)


@dataclass
class PipelineTriggerDeclaration(PropertyType):
    provider_type: DslValue[str] | None = None
    git_configuration: DslValue[GitConfiguration] | None = None


@dataclass
class RetryConfiguration(PropertyType):
    retry_mode: DslValue[str] | None = None


@dataclass
class RuleDeclaration(PropertyType):
    commands: list[DslValue[str]] = field(default_factory=list)
    configuration: DslValue[dict[str, Any]] | None = None
    input_artifacts: list[DslValue[InputArtifact]] = field(default_factory=list)
    name: DslValue[str] | None = None
    region: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    rule_type_id: DslValue[RuleTypeId] | None = None


@dataclass
class RuleTypeId(PropertyType):
    category: DslValue[str] | None = None
    owner: DslValue[str] | None = None
    provider: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class StageDeclaration(PropertyType):
    actions: list[DslValue[ActionDeclaration]] = field(default_factory=list)
    name: DslValue[str] | None = None
    before_entry: DslValue[BeforeEntryConditions] | None = None
    blockers: list[DslValue[BlockerDeclaration]] = field(default_factory=list)
    on_failure: DslValue[FailureConditions] | None = None
    on_success: DslValue[SuccessConditions] | None = None


@dataclass
class StageTransition(PropertyType):
    reason: DslValue[str] | None = None
    stage_name: DslValue[str] | None = None


@dataclass
class SuccessConditions(PropertyType):
    conditions: list[DslValue[Condition]] = field(default_factory=list)


@dataclass
class VariableDeclaration(PropertyType):
    name: DslValue[str] | None = None
    default_value: DslValue[str] | None = None
    description: DslValue[str] | None = None
