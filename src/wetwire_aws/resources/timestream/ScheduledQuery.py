"""PropertyTypes for AWS::Timestream::ScheduledQuery."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DimensionMapping(PropertyType):
    dimension_value_type: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class ErrorReportConfiguration(PropertyType):
    s3_configuration: DslValue[S3Configuration] | None = None


@dataclass
class MixedMeasureMapping(PropertyType):
    measure_value_type: DslValue[str] | None = None
    measure_name: DslValue[str] | None = None
    multi_measure_attribute_mappings: list[DslValue[MultiMeasureAttributeMapping]] = (
        field(default_factory=list)
    )
    source_column: DslValue[str] | None = None
    target_measure_name: DslValue[str] | None = None


@dataclass
class MultiMeasureAttributeMapping(PropertyType):
    measure_value_type: DslValue[str] | None = None
    source_column: DslValue[str] | None = None
    target_multi_measure_attribute_name: DslValue[str] | None = None


@dataclass
class MultiMeasureMappings(PropertyType):
    multi_measure_attribute_mappings: list[DslValue[MultiMeasureAttributeMapping]] = (
        field(default_factory=list)
    )
    target_multi_measure_name: DslValue[str] | None = None


@dataclass
class NotificationConfiguration(PropertyType):
    sns_configuration: DslValue[SnsConfiguration] | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_name: DslValue[str] | None = None
    encryption_option: DslValue[str] | None = None
    object_key_prefix: DslValue[str] | None = None


@dataclass
class ScheduleConfiguration(PropertyType):
    schedule_expression: DslValue[str] | None = None


@dataclass
class SnsConfiguration(PropertyType):
    topic_arn: DslValue[str] | None = None


@dataclass
class TargetConfiguration(PropertyType):
    timestream_configuration: DslValue[TimestreamConfiguration] | None = None


@dataclass
class TimestreamConfiguration(PropertyType):
    database_name: DslValue[str] | None = None
    dimension_mappings: list[DslValue[DimensionMapping]] = field(default_factory=list)
    table_name: DslValue[str] | None = None
    time_column: DslValue[str] | None = None
    measure_name_column: DslValue[str] | None = None
    mixed_measure_mappings: list[DslValue[MixedMeasureMapping]] = field(
        default_factory=list
    )
    multi_measure_mappings: DslValue[MultiMeasureMappings] | None = None
