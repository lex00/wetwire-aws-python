"""PropertyTypes for AWS::DataBrew::Job."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AllowedStatistics(PropertyType):
    statistics: list[String] = field(default_factory=list)


@dataclass
class ColumnSelector(PropertyType):
    name: str | None = None
    regex: str | None = None


@dataclass
class ColumnStatisticsConfiguration(PropertyType):
    statistics: StatisticsConfiguration | None = None
    selectors: list[ColumnSelector] = field(default_factory=list)


@dataclass
class CsvOutputOptions(PropertyType):
    delimiter: str | None = None


@dataclass
class DataCatalogOutput(PropertyType):
    database_name: str | None = None
    table_name: str | None = None
    catalog_id: str | None = None
    database_options: DatabaseTableOutputOptions | None = None
    overwrite: bool | None = None
    s3_options: S3TableOutputOptions | None = None


@dataclass
class DatabaseOutput(PropertyType):
    database_options: DatabaseTableOutputOptions | None = None
    glue_connection_name: str | None = None
    database_output_mode: str | None = None


@dataclass
class DatabaseTableOutputOptions(PropertyType):
    table_name: str | None = None
    temp_directory: S3Location | None = None


@dataclass
class EntityDetectorConfiguration(PropertyType):
    entity_types: list[String] = field(default_factory=list)
    allowed_statistics: AllowedStatistics | None = None


@dataclass
class JobSample(PropertyType):
    mode: str | None = None
    size: int | None = None


@dataclass
class Output(PropertyType):
    location: S3Location | None = None
    compression_format: str | None = None
    format: str | None = None
    format_options: OutputFormatOptions | None = None
    max_output_files: int | None = None
    overwrite: bool | None = None
    partition_columns: list[String] = field(default_factory=list)


@dataclass
class OutputFormatOptions(PropertyType):
    csv: CsvOutputOptions | None = None


@dataclass
class OutputLocation(PropertyType):
    bucket: str | None = None
    bucket_owner: str | None = None
    key: str | None = None


@dataclass
class ProfileConfiguration(PropertyType):
    column_statistics_configurations: list[ColumnStatisticsConfiguration] = field(
        default_factory=list
    )
    dataset_statistics_configuration: StatisticsConfiguration | None = None
    entity_detector_configuration: EntityDetectorConfiguration | None = None
    profile_columns: list[ColumnSelector] = field(default_factory=list)


@dataclass
class Recipe(PropertyType):
    name: str | None = None
    version: str | None = None


@dataclass
class S3Location(PropertyType):
    bucket: str | None = None
    bucket_owner: str | None = None
    key: str | None = None


@dataclass
class S3TableOutputOptions(PropertyType):
    location: S3Location | None = None


@dataclass
class StatisticOverride(PropertyType):
    parameters: dict[str, String] = field(default_factory=dict)
    statistic: str | None = None


@dataclass
class StatisticsConfiguration(PropertyType):
    included_statistics: list[String] = field(default_factory=list)
    overrides: list[StatisticOverride] = field(default_factory=list)


@dataclass
class ValidationConfiguration(PropertyType):
    ruleset_arn: str | None = None
    validation_mode: str | None = None
