"""PropertyTypes for AWS::IoTAnalytics::Datastore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Column(PropertyType):
    name: str | None = None
    type_: str | None = None


@dataclass
class CustomerManagedS3(PropertyType):
    bucket: str | None = None
    role_arn: str | None = None
    key_prefix: str | None = None


@dataclass
class CustomerManagedS3Storage(PropertyType):
    bucket: str | None = None
    key_prefix: str | None = None


@dataclass
class DatastorePartition(PropertyType):
    partition: Partition | None = None
    timestamp_partition: TimestampPartition | None = None


@dataclass
class DatastorePartitions(PropertyType):
    partitions: list[DatastorePartition] = field(default_factory=list)


@dataclass
class DatastoreStorage(PropertyType):
    customer_managed_s3: CustomerManagedS3 | None = None
    iot_site_wise_multi_layer_storage: IotSiteWiseMultiLayerStorage | None = None
    service_managed_s3: dict[str, Any] | None = None


@dataclass
class FileFormatConfiguration(PropertyType):
    json_configuration: dict[str, Any] | None = None
    parquet_configuration: ParquetConfiguration | None = None


@dataclass
class IotSiteWiseMultiLayerStorage(PropertyType):
    customer_managed_s3_storage: CustomerManagedS3Storage | None = None


@dataclass
class ParquetConfiguration(PropertyType):
    schema_definition: SchemaDefinition | None = None


@dataclass
class Partition(PropertyType):
    attribute_name: str | None = None


@dataclass
class RetentionPeriod(PropertyType):
    number_of_days: int | None = None
    unlimited: bool | None = None


@dataclass
class SchemaDefinition(PropertyType):
    columns: list[Column] = field(default_factory=list)


@dataclass
class TimestampPartition(PropertyType):
    attribute_name: str | None = None
    timestamp_format: str | None = None
