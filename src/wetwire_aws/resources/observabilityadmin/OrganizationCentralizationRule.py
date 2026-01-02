"""PropertyTypes for AWS::ObservabilityAdmin::OrganizationCentralizationRule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CentralizationRule(PropertyType):
    destination: CentralizationRuleDestination | None = None
    source: CentralizationRuleSource | None = None


@dataclass
class CentralizationRuleDestination(PropertyType):
    region: str | None = None
    account: str | None = None
    destination_logs_configuration: DestinationLogsConfiguration | None = None


@dataclass
class CentralizationRuleSource(PropertyType):
    regions: list[String] = field(default_factory=list)
    scope: str | None = None
    source_logs_configuration: SourceLogsConfiguration | None = None


@dataclass
class DestinationLogsConfiguration(PropertyType):
    backup_configuration: LogsBackupConfiguration | None = None
    logs_encryption_configuration: LogsEncryptionConfiguration | None = None


@dataclass
class LogsBackupConfiguration(PropertyType):
    region: str | None = None
    kms_key_arn: str | None = None


@dataclass
class LogsEncryptionConfiguration(PropertyType):
    encryption_strategy: str | None = None
    encryption_conflict_resolution_strategy: str | None = None
    kms_key_arn: str | None = None


@dataclass
class SourceLogsConfiguration(PropertyType):
    encrypted_log_group_strategy: str | None = None
    log_group_selection_criteria: str | None = None
