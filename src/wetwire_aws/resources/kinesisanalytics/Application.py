"""PropertyTypes for AWS::KinesisAnalytics::Application."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CSVMappingParameters(PropertyType):
    record_column_delimiter: str | None = None
    record_row_delimiter: str | None = None


@dataclass
class Input(PropertyType):
    input_schema: InputSchema | None = None
    name_prefix: str | None = None
    input_parallelism: InputParallelism | None = None
    input_processing_configuration: InputProcessingConfiguration | None = None
    kinesis_firehose_input: KinesisFirehoseInput | None = None
    kinesis_streams_input: KinesisStreamsInput | None = None


@dataclass
class InputLambdaProcessor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: str | None = None
    role_arn: str | None = None


@dataclass
class InputParallelism(PropertyType):
    count: int | None = None


@dataclass
class InputProcessingConfiguration(PropertyType):
    input_lambda_processor: InputLambdaProcessor | None = None


@dataclass
class InputSchema(PropertyType):
    record_columns: list[RecordColumn] = field(default_factory=list)
    record_format: RecordFormat | None = None
    record_encoding: str | None = None


@dataclass
class JSONMappingParameters(PropertyType):
    record_row_path: str | None = None


@dataclass
class KinesisFirehoseInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: str | None = None
    role_arn: str | None = None


@dataclass
class KinesisStreamsInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: str | None = None
    role_arn: str | None = None


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
