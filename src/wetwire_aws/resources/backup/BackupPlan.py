"""PropertyTypes for AWS::Backup::BackupPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AdvancedBackupSettingResourceType(PropertyType):
    backup_options: dict[str, Any] | None = None
    resource_type: str | None = None


@dataclass
class BackupPlanResourceType(PropertyType):
    backup_plan_name: str | None = None
    backup_plan_rule: list[BackupRuleResourceType] = field(default_factory=list)
    advanced_backup_settings: list[AdvancedBackupSettingResourceType] = field(
        default_factory=list
    )


@dataclass
class BackupRuleResourceType(PropertyType):
    rule_name: str | None = None
    target_backup_vault: str | None = None
    completion_window_minutes: float | None = None
    copy_actions: list[CopyActionResourceType] = field(default_factory=list)
    enable_continuous_backup: bool | None = None
    index_actions: list[IndexActionsResourceType] = field(default_factory=list)
    lifecycle: LifecycleResourceType | None = None
    recovery_point_tags: dict[str, String] = field(default_factory=dict)
    schedule_expression: str | None = None
    schedule_expression_timezone: str | None = None
    start_window_minutes: float | None = None
    target_logically_air_gapped_backup_vault_arn: str | None = None


@dataclass
class CopyActionResourceType(PropertyType):
    destination_backup_vault_arn: str | None = None
    lifecycle: LifecycleResourceType | None = None


@dataclass
class IndexActionsResourceType(PropertyType):
    resource_types: list[String] = field(default_factory=list)


@dataclass
class LifecycleResourceType(PropertyType):
    delete_after_days: float | None = None
    move_to_cold_storage_after_days: float | None = None
    opt_in_to_archive_for_supported_resources: bool | None = None
