"""PropertyTypes for AWS::Timestream::ScheduledQuery."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DimensionMapping(PropertyType):
    dimension_value_type: str | None = None
    name: str | None = None


@dataclass
class ErrorReportConfiguration(PropertyType):
    s3_configuration: S3Configuration | None = None


@dataclass
class MixedMeasureMapping(PropertyType):
    measure_value_type: str | None = None
    measure_name: str | None = None
    multi_measure_attribute_mappings: list[MultiMeasureAttributeMapping] = field(
        default_factory=list
    )
    source_column: str | None = None
    target_measure_name: str | None = None


@dataclass
class MultiMeasureAttributeMapping(PropertyType):
    measure_value_type: str | None = None
    source_column: str | None = None
    target_multi_measure_attribute_name: str | None = None


@dataclass
class MultiMeasureMappings(PropertyType):
    multi_measure_attribute_mappings: list[MultiMeasureAttributeMapping] = field(
        default_factory=list
    )
    target_multi_measure_name: str | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    sns_configuration: SnsConfiguration | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_name: str | None = None
    encryption_option: str | None = None
    object_key_prefix: str | None = None


@dataclass
class ScheduleConfiguration(PropertyType):
    schedule_expression: str | None = None


@dataclass
class SnsConfiguration(PropertyType):
    topic_arn: str | None = None


@dataclass
class TargetConfiguration(PropertyType):
    timestream_configuration: TimestreamConfiguration | None = None


@dataclass
class TimestreamConfiguration(PropertyType):
    database_name: str | None = None
    dimension_mappings: list[DimensionMapping] = field(default_factory=list)
    table_name: str | None = None
    time_column: str | None = None
    measure_name_column: str | None = None
    mixed_measure_mappings: list[MixedMeasureMapping] = field(default_factory=list)
    multi_measure_mappings: MultiMeasureMappings | None = None
