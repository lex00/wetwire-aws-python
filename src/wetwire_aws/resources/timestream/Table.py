"""PropertyTypes for AWS::Timestream::Table."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MagneticStoreRejectedDataLocation(PropertyType):
    s3_configuration: S3Configuration | None = None


@dataclass
class MagneticStoreWriteProperties(PropertyType):
    enable_magnetic_store_writes: bool | None = None
    magnetic_store_rejected_data_location: MagneticStoreRejectedDataLocation | None = (
        None
    )


@dataclass
class PartitionKey(PropertyType):
    type_: str | None = None
    enforcement_in_record: str | None = None
    name: str | None = None


@dataclass
class RetentionProperties(PropertyType):
    magnetic_store_retention_period_in_days: str | None = None
    memory_store_retention_period_in_hours: str | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_name: str | None = None
    encryption_option: str | None = None
    kms_key_id: str | None = None
    object_key_prefix: str | None = None


@dataclass
class Schema(PropertyType):
    composite_partition_key: list[PartitionKey] = field(default_factory=list)
