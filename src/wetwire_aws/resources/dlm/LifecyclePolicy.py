"""PropertyTypes for AWS::DLM::LifecyclePolicy."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Action(PropertyType):
    cross_region_copy: list[CrossRegionCopyAction] = field(default_factory=list)
    name: str | None = None


@dataclass
class ArchiveRetainRule(PropertyType):
    retention_archive_tier: RetentionArchiveTier | None = None


@dataclass
class ArchiveRule(PropertyType):
    retain_rule: ArchiveRetainRule | None = None


@dataclass
class CreateRule(PropertyType):
    cron_expression: str | None = None
    interval: int | None = None
    interval_unit: str | None = None
    location: str | None = None
    scripts: list[Script] = field(default_factory=list)
    times: list[String] = field(default_factory=list)


@dataclass
class CrossRegionCopyAction(PropertyType):
    encryption_configuration: EncryptionConfiguration | None = None
    target: str | None = None
    retain_rule: CrossRegionCopyRetainRule | None = None


@dataclass
class CrossRegionCopyDeprecateRule(PropertyType):
    interval: int | None = None
    interval_unit: str | None = None


@dataclass
class CrossRegionCopyRetainRule(PropertyType):
    interval: int | None = None
    interval_unit: str | None = None


@dataclass
class CrossRegionCopyRule(PropertyType):
    encrypted: bool | None = None
    cmk_arn: str | None = None
    copy_tags: bool | None = None
    deprecate_rule: CrossRegionCopyDeprecateRule | None = None
    retain_rule: CrossRegionCopyRetainRule | None = None
    target: str | None = None
    target_region: str | None = None


@dataclass
class CrossRegionCopyTarget(PropertyType):
    target_region: str | None = None


@dataclass
class CrossRegionCopyTargets(PropertyType):
    pass


@dataclass
class DeprecateRule(PropertyType):
    count: int | None = None
    interval: int | None = None
    interval_unit: str | None = None


@dataclass
class EncryptionConfiguration(PropertyType):
    encrypted: bool | None = None
    cmk_arn: str | None = None


@dataclass
class EventParameters(PropertyType):
    event_type: str | None = None
    snapshot_owner: list[String] = field(default_factory=list)
    description_regex: str | None = None


@dataclass
class EventSource(PropertyType):
    type_: str | None = None
    parameters: EventParameters | None = None


@dataclass
class ExcludeTags(PropertyType):
    pass


@dataclass
class ExcludeVolumeTypesList(PropertyType):
    pass


@dataclass
class Exclusions(PropertyType):
    exclude_boot_volumes: bool | None = None
    exclude_tags: ExcludeTags | None = None
    exclude_volume_types: ExcludeVolumeTypesList | None = None


@dataclass
class FastRestoreRule(PropertyType):
    availability_zones: list[String] = field(default_factory=list)
    count: int | None = None
    interval: int | None = None
    interval_unit: str | None = None


@dataclass
class Parameters(PropertyType):
    exclude_boot_volume: bool | None = None
    exclude_data_volume_tags: list[Tag] = field(default_factory=list)
    no_reboot: bool | None = None


@dataclass
class PolicyDetails(PropertyType):
    actions: list[Action] = field(default_factory=list)
    copy_tags: bool | None = None
    create_interval: int | None = None
    cross_region_copy_targets: CrossRegionCopyTargets | None = None
    event_source: EventSource | None = None
    exclusions: Exclusions | None = None
    extend_deletion: bool | None = None
    parameters: Parameters | None = None
    policy_language: str | None = None
    policy_type: str | None = None
    resource_locations: list[String] = field(default_factory=list)
    resource_type: str | None = None
    resource_types: list[String] = field(default_factory=list)
    retain_interval: int | None = None
    schedules: list[Schedule] = field(default_factory=list)
    target_tags: list[Tag] = field(default_factory=list)


@dataclass
class RetainRule(PropertyType):
    count: int | None = None
    interval: int | None = None
    interval_unit: str | None = None


@dataclass
class RetentionArchiveTier(PropertyType):
    count: int | None = None
    interval: int | None = None
    interval_unit: str | None = None


@dataclass
class Schedule(PropertyType):
    archive_rule: ArchiveRule | None = None
    copy_tags: bool | None = None
    create_rule: CreateRule | None = None
    cross_region_copy_rules: list[CrossRegionCopyRule] = field(default_factory=list)
    deprecate_rule: DeprecateRule | None = None
    fast_restore_rule: FastRestoreRule | None = None
    name: str | None = None
    retain_rule: RetainRule | None = None
    share_rules: list[ShareRule] = field(default_factory=list)
    tags_to_add: list[Tag] = field(default_factory=list)
    variable_tags: list[Tag] = field(default_factory=list)


@dataclass
class Script(PropertyType):
    execute_operation_on_script_failure: bool | None = None
    execution_handler: str | None = None
    execution_handler_service: str | None = None
    execution_timeout: int | None = None
    maximum_retry_count: int | None = None
    stages: list[String] = field(default_factory=list)


@dataclass
class ShareRule(PropertyType):
    target_accounts: list[String] = field(default_factory=list)
    unshare_interval: int | None = None
    unshare_interval_unit: str | None = None


@dataclass
class VolumeTypeValues(PropertyType):
    pass
