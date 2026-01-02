"""PropertyTypes for AWS::IoTFleetWise::Campaign."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CollectionScheme(PropertyType):
    condition_based_collection_scheme: ConditionBasedCollectionScheme | None = None
    time_based_collection_scheme: TimeBasedCollectionScheme | None = None


@dataclass
class ConditionBasedCollectionScheme(PropertyType):
    expression: str | None = None
    condition_language_version: int | None = None
    minimum_trigger_interval_ms: float | None = None
    trigger_mode: str | None = None


@dataclass
class ConditionBasedSignalFetchConfig(PropertyType):
    condition_expression: str | None = None
    trigger_mode: str | None = None


@dataclass
class DataDestinationConfig(PropertyType):
    mqtt_topic_config: MqttTopicConfig | None = None
    s3_config: S3Config | None = None
    timestream_config: TimestreamConfig | None = None


@dataclass
class DataPartition(PropertyType):
    id: str | None = None
    storage_options: DataPartitionStorageOptions | None = None
    upload_options: DataPartitionUploadOptions | None = None


@dataclass
class DataPartitionStorageOptions(PropertyType):
    maximum_size: StorageMaximumSize | None = None
    minimum_time_to_live: StorageMinimumTimeToLive | None = None
    storage_location: str | None = None


@dataclass
class DataPartitionUploadOptions(PropertyType):
    expression: str | None = None
    condition_language_version: int | None = None


@dataclass
class MqttTopicConfig(PropertyType):
    execution_role_arn: str | None = None
    mqtt_topic_arn: str | None = None


@dataclass
class S3Config(PropertyType):
    bucket_arn: str | None = None
    data_format: str | None = None
    prefix: str | None = None
    storage_compression_format: str | None = None


@dataclass
class SignalFetchConfig(PropertyType):
    condition_based: ConditionBasedSignalFetchConfig | None = None
    time_based: TimeBasedSignalFetchConfig | None = None


@dataclass
class SignalFetchInformation(PropertyType):
    actions: list[String] = field(default_factory=list)
    fully_qualified_name: str | None = None
    signal_fetch_config: SignalFetchConfig | None = None
    condition_language_version: float | None = None


@dataclass
class SignalInformation(PropertyType):
    name: str | None = None
    data_partition_id: str | None = None
    max_sample_count: float | None = None
    minimum_sampling_interval_ms: float | None = None


@dataclass
class StorageMaximumSize(PropertyType):
    unit: str | None = None
    value: int | None = None


@dataclass
class StorageMinimumTimeToLive(PropertyType):
    unit: str | None = None
    value: int | None = None


@dataclass
class TimeBasedCollectionScheme(PropertyType):
    period_ms: float | None = None


@dataclass
class TimeBasedSignalFetchConfig(PropertyType):
    execution_frequency_ms: float | None = None


@dataclass
class TimestreamConfig(PropertyType):
    execution_role_arn: str | None = None
    timestream_table_arn: str | None = None
