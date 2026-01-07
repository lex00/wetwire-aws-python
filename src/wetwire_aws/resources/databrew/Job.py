"""PropertyTypes for AWS::DataBrew::Job."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AllowedStatistics(PropertyType):
    statistics: list[DslValue[str]] = field(default_factory=list)


@dataclass
class ColumnSelector(PropertyType):
    name: DslValue[str] | None = None
    regex: DslValue[str] | None = None


@dataclass
class ColumnStatisticsConfiguration(PropertyType):
    statistics: DslValue[StatisticsConfiguration] | None = None
    selectors: list[DslValue[ColumnSelector]] = field(default_factory=list)


@dataclass
class CsvOutputOptions(PropertyType):
    delimiter: DslValue[str] | None = None


@dataclass
class DataCatalogOutput(PropertyType):
    database_name: DslValue[str] | None = None
    table_name: DslValue[str] | None = None
    catalog_id: DslValue[str] | None = None
    database_options: DslValue[DatabaseTableOutputOptions] | None = None
    overwrite: DslValue[bool] | None = None
    s3_options: DslValue[S3TableOutputOptions] | None = None


@dataclass
class DatabaseOutput(PropertyType):
    database_options: DslValue[DatabaseTableOutputOptions] | None = None
    glue_connection_name: DslValue[str] | None = None
    database_output_mode: DslValue[str] | None = None


@dataclass
class DatabaseTableOutputOptions(PropertyType):
    table_name: DslValue[str] | None = None
    temp_directory: DslValue[S3Location] | None = None


@dataclass
class EntityDetectorConfiguration(PropertyType):
    entity_types: list[DslValue[str]] = field(default_factory=list)
    allowed_statistics: DslValue[AllowedStatistics] | None = None


@dataclass
class JobSample(PropertyType):
    mode: DslValue[str] | None = None
    size: DslValue[int] | None = None


@dataclass
class Output(PropertyType):
    location: DslValue[S3Location] | None = None
    compression_format: DslValue[str] | None = None
    format: DslValue[str] | None = None
    format_options: DslValue[OutputFormatOptions] | None = None
    max_output_files: DslValue[int] | None = None
    overwrite: DslValue[bool] | None = None
    partition_columns: list[DslValue[str]] = field(default_factory=list)


@dataclass
class OutputFormatOptions(PropertyType):
    csv: DslValue[CsvOutputOptions] | None = None


@dataclass
class OutputLocation(PropertyType):
    bucket: DslValue[str] | None = None
    bucket_owner: DslValue[str] | None = None
    key: DslValue[str] | None = None


@dataclass
class ProfileConfiguration(PropertyType):
    column_statistics_configurations: list[DslValue[ColumnStatisticsConfiguration]] = (
        field(default_factory=list)
    )
    dataset_statistics_configuration: DslValue[StatisticsConfiguration] | None = None
    entity_detector_configuration: DslValue[EntityDetectorConfiguration] | None = None
    profile_columns: list[DslValue[ColumnSelector]] = field(default_factory=list)


@dataclass
class Recipe(PropertyType):
    name: DslValue[str] | None = None
    version: DslValue[str] | None = None


@dataclass
class S3Location(PropertyType):
    bucket: DslValue[str] | None = None
    bucket_owner: DslValue[str] | None = None
    key: DslValue[str] | None = None


@dataclass
class S3TableOutputOptions(PropertyType):
    location: DslValue[S3Location] | None = None


@dataclass
class StatisticOverride(PropertyType):
    parameters: dict[str, DslValue[str]] = field(default_factory=dict)
    statistic: DslValue[str] | None = None


@dataclass
class StatisticsConfiguration(PropertyType):
    included_statistics: list[DslValue[str]] = field(default_factory=list)
    overrides: list[DslValue[StatisticOverride]] = field(default_factory=list)


@dataclass
class ValidationConfiguration(PropertyType):
    ruleset_arn: DslValue[str] | None = None
    validation_mode: DslValue[str] | None = None
