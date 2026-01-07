"""PropertyTypes for AWS::ObservabilityAdmin::OrganizationCentralizationRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CentralizationRule(PropertyType):
    destination: DslValue[CentralizationRuleDestination] | None = None
    source: DslValue[CentralizationRuleSource] | None = None


@dataclass
class CentralizationRuleDestination(PropertyType):
    region: DslValue[str] | None = None
    account: DslValue[str] | None = None
    destination_logs_configuration: DslValue[DestinationLogsConfiguration] | None = None


@dataclass
class CentralizationRuleSource(PropertyType):
    regions: list[DslValue[str]] = field(default_factory=list)
    scope: DslValue[str] | None = None
    source_logs_configuration: DslValue[SourceLogsConfiguration] | None = None


@dataclass
class DestinationLogsConfiguration(PropertyType):
    backup_configuration: DslValue[LogsBackupConfiguration] | None = None
    logs_encryption_configuration: DslValue[LogsEncryptionConfiguration] | None = None


@dataclass
class LogsBackupConfiguration(PropertyType):
    region: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class LogsEncryptionConfiguration(PropertyType):
    encryption_strategy: DslValue[str] | None = None
    encryption_conflict_resolution_strategy: DslValue[str] | None = None
    kms_key_arn: DslValue[str] | None = None


@dataclass
class SourceLogsConfiguration(PropertyType):
    encrypted_log_group_strategy: DslValue[str] | None = None
    log_group_selection_criteria: DslValue[str] | None = None
