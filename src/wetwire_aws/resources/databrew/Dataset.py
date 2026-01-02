"""PropertyTypes for AWS::DataBrew::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CsvOptions(PropertyType):
    delimiter: str | None = None
    header_row: bool | None = None


@dataclass
class DataCatalogInputDefinition(PropertyType):
    catalog_id: str | None = None
    database_name: str | None = None
    table_name: str | None = None
    temp_directory: S3Location | None = None


@dataclass
class DatabaseInputDefinition(PropertyType):
    glue_connection_name: str | None = None
    database_table_name: str | None = None
    query_string: str | None = None
    temp_directory: S3Location | None = None


@dataclass
class DatasetParameter(PropertyType):
    name: str | None = None
    type_: str | None = None
    create_column: bool | None = None
    datetime_options: DatetimeOptions | None = None
    filter: FilterExpression | None = None


@dataclass
class DatetimeOptions(PropertyType):
    format: str | None = None
    locale_code: str | None = None
    timezone_offset: str | None = None


@dataclass
class ExcelOptions(PropertyType):
    header_row: bool | None = None
    sheet_indexes: list[Integer] = field(default_factory=list)
    sheet_names: list[String] = field(default_factory=list)


@dataclass
class FilesLimit(PropertyType):
    max_files: int | None = None
    order: str | None = None
    ordered_by: str | None = None


@dataclass
class FilterExpression(PropertyType):
    expression: str | None = None
    values_map: list[FilterValue] = field(default_factory=list)


@dataclass
class FilterValue(PropertyType):
    value: str | None = None
    value_reference: str | None = None


@dataclass
class FormatOptions(PropertyType):
    csv: CsvOptions | None = None
    excel: ExcelOptions | None = None
    json: JsonOptions | None = None


@dataclass
class Input(PropertyType):
    data_catalog_input_definition: DataCatalogInputDefinition | None = None
    database_input_definition: DatabaseInputDefinition | None = None
    metadata: Metadata | None = None
    s3_input_definition: S3Location | None = None


@dataclass
class JsonOptions(PropertyType):
    multi_line: bool | None = None


@dataclass
class Metadata(PropertyType):
    source_arn: str | None = None


@dataclass
class PathOptions(PropertyType):
    files_limit: FilesLimit | None = None
    last_modified_date_condition: FilterExpression | None = None
    parameters: list[PathParameter] = field(default_factory=list)


@dataclass
class PathParameter(PropertyType):
    dataset_parameter: DatasetParameter | None = None
    path_parameter_name: str | None = None


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    bucket_owner: str | None = None
    key: str | None = None
