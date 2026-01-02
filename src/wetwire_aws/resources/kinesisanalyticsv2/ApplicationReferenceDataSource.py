"""PropertyTypes for AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CSVMappingParameters(PropertyType):
    record_column_delimiter: str | None = None
    record_row_delimiter: str | None = None


@dataclass
class JSONMappingParameters(PropertyType):
    record_row_path: str | None = None


@dataclass
class MappingParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "csv_mapping_parameters": "CSVMappingParameters",
        "json_mapping_parameters": "JSONMappingParameters",
    }

    csv_mapping_parameters: CSVMappingParameters | None = None
    json_mapping_parameters: JSONMappingParameters | None = None


@dataclass
class RecordColumn(PropertyType):
    name: str | None = None
    sql_type: str | None = None
    mapping: str | None = None


@dataclass
class RecordFormat(PropertyType):
    record_format_type: str | None = None
    mapping_parameters: MappingParameters | None = None


@dataclass
class ReferenceDataSource(PropertyType):
    reference_schema: ReferenceSchema | None = None
    s3_reference_data_source: S3ReferenceDataSource | None = None
    table_name: str | None = None


@dataclass
class ReferenceSchema(PropertyType):
    record_columns: list[RecordColumn] = field(default_factory=list)
    record_format: RecordFormat | None = None
    record_encoding: str | None = None


@dataclass
class S3ReferenceDataSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
    }

    bucket_arn: str | None = None
    file_key: str | None = None
