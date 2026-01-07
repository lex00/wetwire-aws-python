"""PropertyTypes for AWS::SageMaker::FeatureGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataCatalogConfig(PropertyType):
    catalog: DslValue[str] | None = None
    database: DslValue[str] | None = None
    table_name: DslValue[str] | None = None


@dataclass
class FeatureDefinition(PropertyType):
    feature_name: DslValue[str] | None = None
    feature_type: DslValue[str] | None = None


@dataclass
class OfflineStoreConfig(PropertyType):
    s3_storage_config: DslValue[S3StorageConfig] | None = None
    data_catalog_config: DslValue[DataCatalogConfig] | None = None
    disable_glue_table_creation: DslValue[bool] | None = None
    table_format: DslValue[str] | None = None


@dataclass
class OnlineStoreConfig(PropertyType):
    enable_online_store: DslValue[bool] | None = None
    security_config: DslValue[OnlineStoreSecurityConfig] | None = None
    storage_type: DslValue[str] | None = None
    ttl_duration: DslValue[TtlDuration] | None = None


@dataclass
class OnlineStoreSecurityConfig(PropertyType):
    kms_key_id: DslValue[str] | None = None


@dataclass
class S3StorageConfig(PropertyType):
    s3_uri: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None


@dataclass
class ThroughputConfig(PropertyType):
    throughput_mode: DslValue[str] | None = None
    provisioned_read_capacity_units: DslValue[int] | None = None
    provisioned_write_capacity_units: DslValue[int] | None = None


@dataclass
class TtlDuration(PropertyType):
    unit: DslValue[str] | None = None
    value: DslValue[int] | None = None
