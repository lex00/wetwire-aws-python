"""PropertyTypes for AWS::Glue::Table."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Column(PropertyType):
    name: str | None = None
    comment: str | None = None
    type_: str | None = None


@dataclass
class IcebergInput(PropertyType):
    metadata_operation: MetadataOperation | None = None
    version: str | None = None


@dataclass
class MetadataOperation(PropertyType):
    pass


@dataclass
class OpenTableFormatInput(PropertyType):
    iceberg_input: IcebergInput | None = None


@dataclass
class Order(PropertyType):
    column: str | None = None
    sort_order: int | None = None


@dataclass
class SchemaId(PropertyType):
    registry_name: str | None = None
    schema_arn: str | None = None
    schema_name: str | None = None


@dataclass
class SchemaReference(PropertyType):
    schema_id: SchemaId | None = None
    schema_version_id: str | None = None
    schema_version_number: int | None = None


@dataclass
class SerdeInfo(PropertyType):
    name: str | None = None
    parameters: dict[str, Any] | None = None
    serialization_library: str | None = None


@dataclass
class SkewedInfo(PropertyType):
    skewed_column_names: list[String] = field(default_factory=list)
    skewed_column_value_location_maps: dict[str, Any] | None = None
    skewed_column_values: list[String] = field(default_factory=list)


@dataclass
class StorageDescriptor(PropertyType):
    bucket_columns: list[String] = field(default_factory=list)
    columns: list[Column] = field(default_factory=list)
    compressed: bool | None = None
    input_format: str | None = None
    location: str | None = None
    number_of_buckets: int | None = None
    output_format: str | None = None
    parameters: dict[str, Any] | None = None
    schema_reference: SchemaReference | None = None
    serde_info: SerdeInfo | None = None
    skewed_info: SkewedInfo | None = None
    sort_columns: list[Order] = field(default_factory=list)
    stored_as_sub_directories: bool | None = None


@dataclass
class TableIdentifier(PropertyType):
    catalog_id: str | None = None
    database_name: str | None = None
    name: str | None = None
    region: str | None = None


@dataclass
class TableInput(PropertyType):
    description: str | None = None
    name: str | None = None
    owner: str | None = None
    parameters: dict[str, Any] | None = None
    partition_keys: list[Column] = field(default_factory=list)
    retention: int | None = None
    storage_descriptor: StorageDescriptor | None = None
    table_type: str | None = None
    target_table: TableIdentifier | None = None
    view_expanded_text: str | None = None
    view_original_text: str | None = None
