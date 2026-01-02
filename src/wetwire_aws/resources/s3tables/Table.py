"""PropertyTypes for AWS::S3Tables::Table."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Compaction(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "target_file_size_mb": "TargetFileSizeMB",
    }

    status: str | None = None
    target_file_size_mb: int | None = None


@dataclass
class IcebergMetadata(PropertyType):
    iceberg_schema: IcebergSchema | None = None


@dataclass
class IcebergSchema(PropertyType):
    schema_field_list: list[SchemaField] = field(default_factory=list)


@dataclass
class SchemaField(PropertyType):
    name: str | None = None
    type_: str | None = None
    required: bool | None = None


@dataclass
class SnapshotManagement(PropertyType):
    max_snapshot_age_hours: int | None = None
    min_snapshots_to_keep: int | None = None
    status: str | None = None


@dataclass
class StorageClassConfiguration(PropertyType):
    storage_class: str | None = None
