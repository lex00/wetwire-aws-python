"""PropertyTypes for AWS::IoTAnalytics::Datastore."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Column(PropertyType):
    name: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class CustomerManagedS3(PropertyType):
    bucket: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    key_prefix: DslValue[str] | None = None


@dataclass
class CustomerManagedS3Storage(PropertyType):
    bucket: DslValue[str] | None = None
    key_prefix: DslValue[str] | None = None


@dataclass
class DatastorePartition(PropertyType):
    partition: DslValue[Partition] | None = None
    timestamp_partition: DslValue[TimestampPartition] | None = None


@dataclass
class DatastorePartitions(PropertyType):
    partitions: list[DslValue[DatastorePartition]] = field(default_factory=list)


@dataclass
class DatastoreStorage(PropertyType):
    customer_managed_s3: DslValue[CustomerManagedS3] | None = None
    iot_site_wise_multi_layer_storage: DslValue[IotSiteWiseMultiLayerStorage] | None = (
        None
    )
    service_managed_s3: DslValue[dict[str, Any]] | None = None


@dataclass
class FileFormatConfiguration(PropertyType):
    json_configuration: DslValue[dict[str, Any]] | None = None
    parquet_configuration: DslValue[ParquetConfiguration] | None = None


@dataclass
class IotSiteWiseMultiLayerStorage(PropertyType):
    customer_managed_s3_storage: DslValue[CustomerManagedS3Storage] | None = None


@dataclass
class ParquetConfiguration(PropertyType):
    schema_definition: DslValue[SchemaDefinition] | None = None


@dataclass
class Partition(PropertyType):
    attribute_name: DslValue[str] | None = None


@dataclass
class RetentionPeriod(PropertyType):
    number_of_days: DslValue[int] | None = None
    unlimited: DslValue[bool] | None = None


@dataclass
class SchemaDefinition(PropertyType):
    columns: list[DslValue[Column]] = field(default_factory=list)


@dataclass
class TimestampPartition(PropertyType):
    attribute_name: DslValue[str] | None = None
    timestamp_format: DslValue[str] | None = None
