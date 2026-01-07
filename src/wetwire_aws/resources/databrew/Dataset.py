"""PropertyTypes for AWS::DataBrew::Dataset."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CsvOptions(PropertyType):
    delimiter: DslValue[str] | None = None
    header_row: DslValue[bool] | None = None


@dataclass
class DataCatalogInputDefinition(PropertyType):
    catalog_id: DslValue[str] | None = None
    database_name: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    temp_directory: DslValue[S3Location] | None = None


@dataclass
class DatabaseInputDefinition(PropertyType):
    glue_connection_name: DslValue[str] | None = None
    database_table_name: DslValue[str] | None = None
    query_string: DslValue[str] | None = None
    temp_directory: DslValue[S3Location] | None = None


@dataclass
class DatasetParameter(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    create_column: DslValue[bool] | None = None
    datetime_options: DslValue[DatetimeOptions] | None = None
    filter: DslValue[FilterExpression] | None = None


@dataclass
class DatetimeOptions(PropertyType):
    format: DslValue[str] | None = None
    locale_code: DslValue[str] | None = None
    timezone_offset: DslValue[str] | None = None


@dataclass
class ExcelOptions(PropertyType):
    header_row: DslValue[bool] | None = None
    sheet_indexes: list[DslValue[int]] = field(default_factory=list)
    sheet_names: list[DslValue[str]] = field(default_factory=list)


@dataclass
class FilesLimit(PropertyType):
    max_files: DslValue[int] | None = None
    order: DslValue[str] | None = None
    ordered_by: DslValue[str] | None = None


@dataclass
class FilterExpression(PropertyType):
    expression: DslValue[str] | None = None
    values_map: list[DslValue[FilterValue]] = field(default_factory=list)


@dataclass
class FilterValue(PropertyType):
    value: DslValue[str] | None = None
    value_reference: DslValue[str] | None = None


@dataclass
class FormatOptions(PropertyType):
    csv: DslValue[CsvOptions] | None = None
    excel: DslValue[ExcelOptions] | None = None
    json: DslValue[JsonOptions] | None = None


@dataclass
class Input(PropertyType):
    data_catalog_input_definition: DslValue[DataCatalogInputDefinition] | None = None
    database_input_definition: DslValue[DatabaseInputDefinition] | None = None
    metadata: DslValue[Metadata] | None = None
    s3_input_definition: DslValue[S3Location] | None = None


@dataclass
class JsonOptions(PropertyType):
    multi_line: DslValue[bool] | None = None


@dataclass
class Metadata(PropertyType):
    source_arn: DslValue[str] | None = None


@dataclass
class PathOptions(PropertyType):
    files_limit: DslValue[FilesLimit] | None = None
    last_modified_date_condition: DslValue[FilterExpression] | None = None
    parameters: list[DslValue[PathParameter]] = field(default_factory=list)


@dataclass
class PathParameter(PropertyType):
    dataset_parameter: DslValue[DatasetParameter] | None = None
    path_parameter_name: DslValue[str] | None = None


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    bucket_owner: DslValue[str] | None = None
    key: DslValue[str] | None = None
