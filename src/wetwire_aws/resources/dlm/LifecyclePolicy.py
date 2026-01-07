"""PropertyTypes for AWS::DLM::LifecyclePolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Action(PropertyType):
    cross_region_copy: list[DslValue[CrossRegionCopyAction]] = field(
        default_factory=list
    )
    name: DslValue[str] | None = None


@dataclass
class ArchiveRetainRule(PropertyType):
    retention_archive_tier: DslValue[RetentionArchiveTier] | None = None


@dataclass
class ArchiveRule(PropertyType):
    retain_rule: DslValue[ArchiveRetainRule] | None = None


@dataclass
class CreateRule(PropertyType):
    cron_expression: DslValue[str] | None = None
    interval: DslValue[int] | None = None
    interval_unit: DslValue[str] | None = None
    location: DslValue[str] | None = None
    scripts: list[DslValue[Script]] = field(default_factory=list)
    times: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CrossRegionCopyAction(PropertyType):
    encryption_configuration: DslValue[EncryptionConfiguration] | None = None
    target: DslValue[str] | None = None
    retain_rule: DslValue[CrossRegionCopyRetainRule] | None = None


@dataclass
class CrossRegionCopyDeprecateRule(PropertyType):
    interval: DslValue[int] | None = None
    interval_unit: DslValue[str] | None = None


@dataclass
class CrossRegionCopyRetainRule(PropertyType):
    interval: DslValue[int] | None = None
    interval_unit: DslValue[str] | None = None


@dataclass
class CrossRegionCopyRule(PropertyType):
    encrypted: DslValue[bool] | None = None
    cmk_arn: DslValue[str] | None = None
    copy_tags: DslValue[bool] | None = None
    deprecate_rule: DslValue[CrossRegionCopyDeprecateRule] | None = None
    retain_rule: DslValue[CrossRegionCopyRetainRule] | None = None
    target: DslValue[str] | None = None
    target_region: DslValue[str] | None = None


@dataclass
class CrossRegionCopyTarget(PropertyType):
    target_region: DslValue[str] | None = None


@dataclass
class CrossRegionCopyTargets(PropertyType):
    pass


@dataclass
class DeprecateRule(PropertyType):
    count: DslValue[int] | None = None
    interval: DslValue[int] | None = None
    interval_unit: DslValue[str] | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    encrypted: DslValue[bool] | None = None
    cmk_arn: DslValue[str] | None = None


@dataclass
class EventParameters(PropertyType):
    event_type: DslValue[str] | None = None
    snapshot_owner: list[DslValue[str]] = field(default_factory=list)
    description_regex: DslValue[str] | None = None


@dataclass
class EventSource(PropertyType):
    type_: DslValue[str] | None = None
    parameters: DslValue[EventParameters] | None = None


@dataclass
class ExcludeTags(PropertyType):
    pass


@dataclass
class ExcludeVolumeTypesList(PropertyType):
    pass


@dataclass
class Exclusions(PropertyType):
    exclude_boot_volumes: DslValue[bool] | None = None
    exclude_tags: DslValue[ExcludeTags] | None = None
    exclude_volume_types: DslValue[ExcludeVolumeTypesList] | None = None


@dataclass
class FastRestoreRule(PropertyType):
    availability_zones: list[DslValue[str]] = field(default_factory=list)
    count: DslValue[int] | None = None
    interval: DslValue[int] | None = None
    interval_unit: DslValue[str] | None = None


@dataclass
class Parameters(PropertyType):
    exclude_boot_volume: DslValue[bool] | None = None
    exclude_data_volume_tags: list[DslValue[Tag]] = field(default_factory=list)
    no_reboot: DslValue[bool] | None = None


@dataclass
class PolicyDetails(PropertyType):
    actions: list[DslValue[Action]] = field(default_factory=list)
    copy_tags: DslValue[bool] | None = None
    create_interval: DslValue[int] | None = None
    cross_region_copy_targets: DslValue[CrossRegionCopyTargets] | None = None
    event_source: DslValue[EventSource] | None = None
    exclusions: DslValue[Exclusions] | None = None
    extend_deletion: DslValue[bool] | None = None
    parameters: DslValue[Parameters] | None = None
    policy_language: DslValue[str] | None = None
    policy_type: DslValue[str] | None = None
    resource_locations: list[DslValue[str]] = field(default_factory=list)
    resource_type: DslValue[str] | None = None
    resource_types: list[DslValue[str]] = field(default_factory=list)
    retain_interval: DslValue[int] | None = None
    schedules: list[DslValue[Schedule]] = field(default_factory=list)
    target_tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class RetainRule(PropertyType):
    count: DslValue[int] | None = None
    interval: DslValue[int] | None = None
    interval_unit: DslValue[str] | None = None


@dataclass
class RetentionArchiveTier(PropertyType):
    count: DslValue[int] | None = None
    interval: DslValue[int] | None = None
    interval_unit: DslValue[str] | None = None


@dataclass
class Schedule(PropertyType):
    archive_rule: DslValue[ArchiveRule] | None = None
    copy_tags: DslValue[bool] | None = None
    create_rule: DslValue[CreateRule] | None = None
    cross_region_copy_rules: list[DslValue[CrossRegionCopyRule]] = field(
        default_factory=list
    )
    deprecate_rule: DslValue[DeprecateRule] | None = None
    fast_restore_rule: DslValue[FastRestoreRule] | None = None
    name: DslValue[str] | None = None
    retain_rule: DslValue[RetainRule] | None = None
    share_rules: list[DslValue[ShareRule]] = field(default_factory=list)
    tags_to_add: list[DslValue[Tag]] = field(default_factory=list)
    variable_tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class Script(PropertyType):
    execute_operation_on_script_failure: DslValue[bool] | None = None
    execution_handler: DslValue[str] | None = None
    execution_handler_service: DslValue[str] | None = None
    execution_timeout: DslValue[int] | None = None
    maximum_retry_count: DslValue[int] | None = None
    stages: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ShareRule(PropertyType):
    target_accounts: list[DslValue[str]] = field(default_factory=list)
    unshare_interval: DslValue[int] | None = None
    unshare_interval_unit: DslValue[str] | None = None


@dataclass
class VolumeTypeValues(PropertyType):
    pass
