"""PropertyTypes for AWS::Glue::TableOptimizer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IcebergConfiguration(PropertyType):
    location: DslValue[str] | None = None
    orphan_file_retention_period_in_days: DslValue[int] | None = None


@dataclass
class IcebergRetentionConfiguration(PropertyType):
    clean_expired_files: DslValue[bool] | None = None
    number_of_snapshots_to_retain: DslValue[int] | None = None
    snapshot_retention_period_in_days: DslValue[int] | None = None


@dataclass
class OrphanFileDeletionConfiguration(PropertyType):
    iceberg_configuration: DslValue[IcebergConfiguration] | None = None


@dataclass
class RetentionConfiguration(PropertyType):
    iceberg_configuration: DslValue[IcebergRetentionConfiguration] | None = None


@dataclass
class TableOptimizerConfiguration(PropertyType):
    enabled: DslValue[bool] | None = None
    role_arn: DslValue[str] | None = None
    orphan_file_deletion_configuration: (
        DslValue[OrphanFileDeletionConfiguration] | None
    ) = None
    retention_configuration: DslValue[RetentionConfiguration] | None = None
    vpc_configuration: DslValue[VpcConfiguration] | None = None


@dataclass
class VpcConfiguration(PropertyType):
    glue_connection_name: DslValue[str] | None = None
