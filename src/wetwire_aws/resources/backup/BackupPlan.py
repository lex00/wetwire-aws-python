"""PropertyTypes for AWS::Backup::BackupPlan."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AdvancedBackupSettingResourceType(PropertyType):
    backup_options: DslValue[dict[str, Any]] | None = None
    resource_type: DslValue[str] | None = None


@dataclass
class BackupPlanResourceType(PropertyType):
    backup_plan_name: DslValue[str] | None = None
    backup_plan_rule: list[DslValue[BackupRuleResourceType]] = field(
        default_factory=list
    )
    advanced_backup_settings: list[DslValue[AdvancedBackupSettingResourceType]] = field(
        default_factory=list
    )


@dataclass
class BackupRuleResourceType(PropertyType):
    rule_name: DslValue[str] | None = None
    target_backup_vault: DslValue[str] | None = None
    completion_window_minutes: DslValue[float] | None = None
    copy_actions: list[DslValue[CopyActionResourceType]] = field(default_factory=list)
    enable_continuous_backup: DslValue[bool] | None = None
    index_actions: list[DslValue[IndexActionsResourceType]] = field(
        default_factory=list
    )
    lifecycle: DslValue[LifecycleResourceType] | None = None
    recovery_point_tags: dict[str, DslValue[str]] = field(default_factory=dict)
    schedule_expression: DslValue[str] | None = None
    schedule_expression_timezone: DslValue[str] | None = None
    start_window_minutes: DslValue[float] | None = None
    target_logically_air_gapped_backup_vault_arn: DslValue[str] | None = None


@dataclass
class CopyActionResourceType(PropertyType):
    destination_backup_vault_arn: DslValue[str] | None = None
    lifecycle: DslValue[LifecycleResourceType] | None = None


@dataclass
class IndexActionsResourceType(PropertyType):
    resource_types: list[DslValue[str]] = field(default_factory=list)


@dataclass
class LifecycleResourceType(PropertyType):
    delete_after_days: DslValue[float] | None = None
    move_to_cold_storage_after_days: DslValue[float] | None = None
    opt_in_to_archive_for_supported_resources: DslValue[bool] | None = None
