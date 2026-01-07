"""PropertyTypes for AWS::S3Tables::Table."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Compaction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_file_size_mb": "TargetFileSizeMB",
    }

    status: DslValue[str] | None = None
    target_file_size_mb: DslValue[int] | None = None


@dataclass
class IcebergMetadata(PropertyType):
    iceberg_schema: DslValue[IcebergSchema] | None = None


@dataclass
class IcebergSchema(PropertyType):
    schema_field_list: list[DslValue[SchemaField]] = field(default_factory=list)


@dataclass
class SchemaField(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    required: DslValue[bool] | None = None


@dataclass
class SnapshotManagement(PropertyType):
    max_snapshot_age_hours: DslValue[int] | None = None
    min_snapshots_to_keep: DslValue[int] | None = None
    status: DslValue[str] | None = None


@dataclass
class StorageClassConfiguration(PropertyType):
    storage_class: DslValue[str] | None = None
