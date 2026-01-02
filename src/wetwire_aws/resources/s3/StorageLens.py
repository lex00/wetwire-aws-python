"""PropertyTypes for AWS::S3::StorageLens."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccountLevel(PropertyType):
    bucket_level: BucketLevel | None = None
    activity_metrics: ActivityMetrics | None = None
    advanced_cost_optimization_metrics: AdvancedCostOptimizationMetrics | None = None
    advanced_data_protection_metrics: AdvancedDataProtectionMetrics | None = None
    advanced_performance_metrics: AdvancedPerformanceMetrics | None = None
    detailed_status_codes_metrics: DetailedStatusCodesMetrics | None = None
    storage_lens_group_level: StorageLensGroupLevel | None = None


@dataclass
class ActivityMetrics(PropertyType):
    is_enabled: bool | None = None


@dataclass
class AdvancedCostOptimizationMetrics(PropertyType):
    is_enabled: bool | None = None


@dataclass
class AdvancedDataProtectionMetrics(PropertyType):
    is_enabled: bool | None = None


@dataclass
class AdvancedPerformanceMetrics(PropertyType):
    is_enabled: bool | None = None


@dataclass
class AwsOrg(PropertyType):
    arn: str | None = None


@dataclass
class BucketLevel(PropertyType):
    activity_metrics: ActivityMetrics | None = None
    advanced_cost_optimization_metrics: AdvancedCostOptimizationMetrics | None = None
    advanced_data_protection_metrics: AdvancedDataProtectionMetrics | None = None
    advanced_performance_metrics: AdvancedPerformanceMetrics | None = None
    detailed_status_codes_metrics: DetailedStatusCodesMetrics | None = None
    prefix_level: PrefixLevel | None = None


@dataclass
class BucketsAndRegions(PropertyType):
    buckets: list[String] = field(default_factory=list)
    regions: list[String] = field(default_factory=list)


@dataclass
class CloudWatchMetrics(PropertyType):
    is_enabled: bool | None = None


@dataclass
class DataExport(PropertyType):
    cloud_watch_metrics: CloudWatchMetrics | None = None
    s3_bucket_destination: S3BucketDestination | None = None
    storage_lens_table_destination: StorageLensTableDestination | None = None


@dataclass
class DetailedStatusCodesMetrics(PropertyType):
    is_enabled: bool | None = None


@dataclass
class Encryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ssekms": "SSEKMS",
        "sses3": "SSES3",
    }

    ssekms: SSEKMS | None = None
    sses3: dict[str, Any] | None = None


@dataclass
class PrefixLevel(PropertyType):
    storage_metrics: PrefixLevelStorageMetrics | None = None


@dataclass
class PrefixLevelStorageMetrics(PropertyType):
    is_enabled: bool | None = None
    selection_criteria: SelectionCriteria | None = None


@dataclass
class S3BucketDestination(PropertyType):
    account_id: str | None = None
    arn: str | None = None
    format: str | None = None
    output_schema_version: str | None = None
    encryption: Encryption | None = None
    prefix: str | None = None


@dataclass
class SSEKMS(PropertyType):
    key_id: str | None = None


@dataclass
class SelectionCriteria(PropertyType):
    delimiter: str | None = None
    max_depth: int | None = None
    min_storage_bytes_percentage: float | None = None


@dataclass
class StorageLensConfiguration(PropertyType):
    account_level: AccountLevel | None = None
    id: str | None = None
    is_enabled: bool | None = None
    aws_org: AwsOrg | None = None
    data_export: DataExport | None = None
    exclude: BucketsAndRegions | None = None
    expanded_prefixes_data_export: StorageLensExpandedPrefixesDataExport | None = None
    include: BucketsAndRegions | None = None
    prefix_delimiter: str | None = None
    storage_lens_arn: str | None = None


@dataclass
class StorageLensExpandedPrefixesDataExport(PropertyType):
    s3_bucket_destination: S3BucketDestination | None = None
    storage_lens_table_destination: StorageLensTableDestination | None = None


@dataclass
class StorageLensGroupLevel(PropertyType):
    storage_lens_group_selection_criteria: StorageLensGroupSelectionCriteria | None = (
        None
    )


@dataclass
class StorageLensGroupSelectionCriteria(PropertyType):
    exclude: list[String] = field(default_factory=list)
    include: list[String] = field(default_factory=list)


@dataclass
class StorageLensTableDestination(PropertyType):
    is_enabled: bool | None = None
    encryption: Encryption | None = None
