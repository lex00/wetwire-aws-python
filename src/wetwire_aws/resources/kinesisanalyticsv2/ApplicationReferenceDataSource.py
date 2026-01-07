"""PropertyTypes for AWS::KinesisAnalyticsV2::ApplicationReferenceDataSource."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CSVMappingParameters(PropertyType):
    record_column_delimiter: DslValue[str] | None = None
    record_row_delimiter: DslValue[str] | None = None


@dataclass
class JSONMappingParameters(PropertyType):
    record_row_path: DslValue[str] | None = None


@dataclass
class MappingParameters(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "csv_mapping_parameters": "CSVMappingParameters",
        "json_mapping_parameters": "JSONMappingParameters",
    }

    csv_mapping_parameters: DslValue[CSVMappingParameters] | None = None
    json_mapping_parameters: DslValue[JSONMappingParameters] | None = None


@dataclass
class RecordColumn(PropertyType):
    name: DslValue[str] | None = None
    sql_type: DslValue[str] | None = None
    mapping: DslValue[str] | None = None


@dataclass
class RecordFormat(PropertyType):
    record_format_type: DslValue[str] | None = None
    mapping_parameters: DslValue[MappingParameters] | None = None


@dataclass
class ReferenceDataSource(PropertyType):
    reference_schema: DslValue[ReferenceSchema] | None = None
    s3_reference_data_source: DslValue[S3ReferenceDataSource] | None = None
    table_name: DslValue[str] | None = None


@dataclass
class ReferenceSchema(PropertyType):
    record_columns: list[DslValue[RecordColumn]] = field(default_factory=list)
    record_format: DslValue[RecordFormat] | None = None
    record_encoding: DslValue[str] | None = None


@dataclass
class S3ReferenceDataSource(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "bucket_arn": "BucketARN",
    }

    bucket_arn: DslValue[str] | None = None
    file_key: DslValue[str] | None = None
