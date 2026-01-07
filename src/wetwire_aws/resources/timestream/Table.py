"""PropertyTypes for AWS::Timestream::Table."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MagneticStoreRejectedDataLocation(PropertyType):
    s3_configuration: DslValue[S3Configuration] | None = None


@dataclass
class MagneticStoreWriteProperties(PropertyType):
    enable_magnetic_store_writes: DslValue[bool] | None = None
    magnetic_store_rejected_data_location: (
        DslValue[MagneticStoreRejectedDataLocation] | None
    ) = None


@dataclass
class PartitionKey(PropertyType):
    type_: DslValue[str] | None = None
    enforcement_in_record: DslValue[str] | None = None
    name: DslValue[str] | None = None


@dataclass
class RetentionProperties(PropertyType):
    magnetic_store_retention_period_in_days: DslValue[str] | None = None
    memory_store_retention_period_in_hours: DslValue[str] | None = None


@dataclass
class S3Configuration(PropertyType):
    bucket_name: DslValue[str] | None = None
    encryption_option: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
    object_key_prefix: DslValue[str] | None = None


@dataclass
class Schema(PropertyType):
    composite_partition_key: list[DslValue[PartitionKey]] = field(default_factory=list)
