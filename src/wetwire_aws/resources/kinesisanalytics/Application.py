"""PropertyTypes for AWS::KinesisAnalytics::Application."""

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
class Input(PropertyType):
    input_schema: DslValue[InputSchema] | None = None
    name_prefix: DslValue[str] | None = None
    input_parallelism: DslValue[InputParallelism] | None = None
    input_processing_configuration: DslValue[InputProcessingConfiguration] | None = None
    kinesis_firehose_input: DslValue[KinesisFirehoseInput] | None = None
    kinesis_streams_input: DslValue[KinesisStreamsInput] | None = None


@dataclass
class InputLambdaProcessor(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class InputParallelism(PropertyType):
    count: DslValue[int] | None = None


@dataclass
class InputProcessingConfiguration(PropertyType):
    input_lambda_processor: DslValue[InputLambdaProcessor] | None = None


@dataclass
class InputSchema(PropertyType):
    record_columns: list[DslValue[RecordColumn]] = field(default_factory=list)
    record_format: DslValue[RecordFormat] | None = None
    record_encoding: DslValue[str] | None = None


@dataclass
class JSONMappingParameters(PropertyType):
    record_row_path: DslValue[str] | None = None


@dataclass
class KinesisFirehoseInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


@dataclass
class KinesisStreamsInput(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
        "role_arn": "RoleARN",
    }

    resource_arn: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None


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
