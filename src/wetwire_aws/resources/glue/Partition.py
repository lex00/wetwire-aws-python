"""PropertyTypes for AWS::Glue::Partition."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Column(PropertyType):
    name: DslValue[str] | None = None
    comment: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class Order(PropertyType):
    column: DslValue[str] | None = None
    sort_order: DslValue[int] | None = None


@dataclass
class PartitionInput(PropertyType):
    values: list[DslValue[str]] = field(default_factory=list)
    parameters: DslValue[dict[str, Any]] | None = None
    storage_descriptor: DslValue[StorageDescriptor] | None = None


@dataclass
class SchemaId(PropertyType):
    registry_name: DslValue[str] | None = None
    schema_arn: DslValue[str] | None = None
    schema_name: DslValue[str] | None = None


@dataclass
class SchemaReference(PropertyType):
    schema_id: DslValue[SchemaId] | None = None
    schema_version_id: DslValue[str] | None = None
    schema_version_number: DslValue[int] | None = None


@dataclass
class SerdeInfo(PropertyType):
    name: DslValue[str] | None = None
    parameters: DslValue[dict[str, Any]] | None = None
    serialization_library: DslValue[str] | None = None


@dataclass
class SkewedInfo(PropertyType):
    skewed_column_names: list[DslValue[str]] = field(default_factory=list)
    skewed_column_value_location_maps: DslValue[dict[str, Any]] | None = None
    skewed_column_values: list[DslValue[str]] = field(default_factory=list)


@dataclass
class StorageDescriptor(PropertyType):
    bucket_columns: list[DslValue[str]] = field(default_factory=list)
    columns: list[DslValue[Column]] = field(default_factory=list)
    compressed: DslValue[bool] | None = None
    input_format: DslValue[str] | None = None
    location: DslValue[str] | None = None
    number_of_buckets: DslValue[int] | None = None
    output_format: DslValue[str] | None = None
    parameters: DslValue[dict[str, Any]] | None = None
    schema_reference: DslValue[SchemaReference] | None = None
    serde_info: DslValue[SerdeInfo] | None = None
    skewed_info: DslValue[SkewedInfo] | None = None
    sort_columns: list[DslValue[Order]] = field(default_factory=list)
    stored_as_sub_directories: DslValue[bool] | None = None
