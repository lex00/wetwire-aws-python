"""PropertyTypes for AWS::Glue::TableOptimizer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IcebergConfiguration(PropertyType):
    location: str | None = None
    orphan_file_retention_period_in_days: int | None = None


@dataclass
class IcebergRetentionConfiguration(PropertyType):
    clean_expired_files: bool | None = None
    number_of_snapshots_to_retain: int | None = None
    snapshot_retention_period_in_days: int | None = None


@dataclass
class OrphanFileDeletionConfiguration(PropertyType):
    iceberg_configuration: IcebergConfiguration | None = None


@dataclass
class RetentionConfiguration(PropertyType):
    iceberg_configuration: IcebergRetentionConfiguration | None = None


@dataclass
class TableOptimizerConfiguration(PropertyType):
    enabled: bool | None = None
    role_arn: str | None = None
    orphan_file_deletion_configuration: OrphanFileDeletionConfiguration | None = None
    retention_configuration: RetentionConfiguration | None = None
    vpc_configuration: VpcConfiguration | None = None


@dataclass
class VpcConfiguration(PropertyType):
    glue_connection_name: str | None = None
