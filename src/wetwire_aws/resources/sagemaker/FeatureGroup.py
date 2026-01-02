"""PropertyTypes for AWS::SageMaker::FeatureGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataCatalogConfig(PropertyType):
    catalog: str | None = None
    database: str | None = None
    table_name: str | None = None


@dataclass
class FeatureDefinition(PropertyType):
    feature_name: str | None = None
    feature_type: str | None = None


@dataclass
class OfflineStoreConfig(PropertyType):
    s3_storage_config: S3StorageConfig | None = None
    data_catalog_config: DataCatalogConfig | None = None
    disable_glue_table_creation: bool | None = None
    table_format: str | None = None


@dataclass
class OnlineStoreConfig(PropertyType):
    enable_online_store: bool | None = None
    security_config: OnlineStoreSecurityConfig | None = None
    storage_type: str | None = None
    ttl_duration: TtlDuration | None = None


@dataclass
class OnlineStoreSecurityConfig(PropertyType):
    kms_key_id: str | None = None


@dataclass
class S3StorageConfig(PropertyType):
    s3_uri: str | None = None
    kms_key_id: str | None = None


@dataclass
class ThroughputConfig(PropertyType):
    throughput_mode: str | None = None
    provisioned_read_capacity_units: int | None = None
    provisioned_write_capacity_units: int | None = None


@dataclass
class TtlDuration(PropertyType):
    unit: str | None = None
    value: int | None = None
