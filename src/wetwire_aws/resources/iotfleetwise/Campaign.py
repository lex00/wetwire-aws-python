"""PropertyTypes for AWS::IoTFleetWise::Campaign."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CollectionScheme(PropertyType):
    condition_based_collection_scheme: (
        DslValue[ConditionBasedCollectionScheme] | None
    ) = None
    time_based_collection_scheme: DslValue[TimeBasedCollectionScheme] | None = None


@dataclass
class ConditionBasedCollectionScheme(PropertyType):
    expression: DslValue[str] | None = None
    condition_language_version: DslValue[int] | None = None
    minimum_trigger_interval_ms: DslValue[float] | None = None
    trigger_mode: DslValue[str] | None = None


@dataclass
class ConditionBasedSignalFetchConfig(PropertyType):
    condition_expression: DslValue[str] | None = None
    trigger_mode: DslValue[str] | None = None


@dataclass
class DataDestinationConfig(PropertyType):
    mqtt_topic_config: DslValue[MqttTopicConfig] | None = None
    s3_config: DslValue[S3Config] | None = None
    timestream_config: DslValue[TimestreamConfig] | None = None


@dataclass
class DataPartition(PropertyType):
    id: DslValue[str] | None = None
    storage_options: DslValue[DataPartitionStorageOptions] | None = None
    upload_options: DslValue[DataPartitionUploadOptions] | None = None


@dataclass
class DataPartitionStorageOptions(PropertyType):
    maximum_size: DslValue[StorageMaximumSize] | None = None
    minimum_time_to_live: DslValue[StorageMinimumTimeToLive] | None = None
    storage_location: DslValue[str] | None = None


@dataclass
class DataPartitionUploadOptions(PropertyType):
    expression: DslValue[str] | None = None
    condition_language_version: DslValue[int] | None = None


@dataclass
class MqttTopicConfig(PropertyType):
    execution_role_arn: DslValue[str] | None = None
    mqtt_topic_arn: DslValue[str] | None = None


@dataclass
class S3Config(PropertyType):
    bucket_arn: DslValue[str] | None = None
    data_format: DslValue[str] | None = None
    prefix: DslValue[str] | None = None
    storage_compression_format: DslValue[str] | None = None


@dataclass
class SignalFetchConfig(PropertyType):
    condition_based: DslValue[ConditionBasedSignalFetchConfig] | None = None
    time_based: DslValue[TimeBasedSignalFetchConfig] | None = None


@dataclass
class SignalFetchInformation(PropertyType):
    actions: list[DslValue[str]] = field(default_factory=list)
    fully_qualified_name: DslValue[str] | None = None
    signal_fetch_config: DslValue[SignalFetchConfig] | None = None
    condition_language_version: DslValue[float] | None = None


@dataclass
class SignalInformation(PropertyType):
    name: DslValue[str] | None = None
    data_partition_id: DslValue[str] | None = None
    max_sample_count: DslValue[float] | None = None
    minimum_sampling_interval_ms: DslValue[float] | None = None


@dataclass
class StorageMaximumSize(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class StorageMinimumTimeToLive(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class TimeBasedCollectionScheme(PropertyType):
    period_ms: DslValue[float] | None = None


@dataclass
class TimeBasedSignalFetchConfig(PropertyType):
    execution_frequency_ms: DslValue[float] | None = None


@dataclass
class TimestreamConfig(PropertyType):
    execution_role_arn: DslValue[str] | None = None
    timestream_table_arn: DslValue[str] | None = None
