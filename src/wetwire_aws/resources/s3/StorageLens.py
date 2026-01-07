"""PropertyTypes for AWS::S3::StorageLens."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccountLevel(PropertyType):
    bucket_level: DslValue[BucketLevel] | None = None
    activity_metrics: DslValue[ActivityMetrics] | None = None
    advanced_cost_optimization_metrics: (
        DslValue[AdvancedCostOptimizationMetrics] | None
    ) = None
    advanced_data_protection_metrics: DslValue[AdvancedDataProtectionMetrics] | None = (
        None
    )
    advanced_performance_metrics: DslValue[AdvancedPerformanceMetrics] | None = None
    detailed_status_codes_metrics: DslValue[DetailedStatusCodesMetrics] | None = None
    storage_lens_group_level: DslValue[StorageLensGroupLevel] | None = None


@dataclass
class ActivityMetrics(PropertyType):
    is_enabled: DslValue[bool] | None = None


@dataclass
class AdvancedCostOptimizationMetrics(PropertyType):
    is_enabled: DslValue[bool] | None = None


@dataclass
class AdvancedDataProtectionMetrics(PropertyType):
    is_enabled: DslValue[bool] | None = None


@dataclass
class AdvancedPerformanceMetrics(PropertyType):
    is_enabled: DslValue[bool] | None = None


@dataclass
class AwsOrg(PropertyType):
    arn: DslValue[str] | None = None


@dataclass
class BucketLevel(PropertyType):
    activity_metrics: DslValue[ActivityMetrics] | None = None
    advanced_cost_optimization_metrics: (
        DslValue[AdvancedCostOptimizationMetrics] | None
    ) = None
    advanced_data_protection_metrics: DslValue[AdvancedDataProtectionMetrics] | None = (
        None
    )
    advanced_performance_metrics: DslValue[AdvancedPerformanceMetrics] | None = None
    detailed_status_codes_metrics: DslValue[DetailedStatusCodesMetrics] | None = None
    prefix_level: DslValue[PrefixLevel] | None = None


@dataclass
class BucketsAndRegions(PropertyType):
    buckets: list[DslValue[str]] = field(default_factory=list)
    regions: list[DslValue[str]] = field(default_factory=list)


@dataclass
class CloudWatchMetrics(PropertyType):
    is_enabled: DslValue[bool] | None = None


@dataclass
class DataExport(PropertyType):
    cloud_watch_metrics: DslValue[CloudWatchMetrics] | None = None
    s3_bucket_destination: DslValue[S3BucketDestination] | None = None
    storage_lens_table_destination: DslValue[StorageLensTableDestination] | None = None


@dataclass
class DetailedStatusCodesMetrics(PropertyType):
    is_enabled: DslValue[bool] | None = None


@dataclass
class Encryption(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ssekms": "SSEKMS",
        "sses3": "SSES3",
    }

    ssekms: DslValue[SSEKMS] | None = None
    sses3: DslValue[dict[str, Any]] | None = None


@dataclass
class PrefixLevel(PropertyType):
    storage_metrics: DslValue[PrefixLevelStorageMetrics] | None = None


@dataclass
class PrefixLevelStorageMetrics(PropertyType):
    is_enabled: DslValue[bool] | None = None
    selection_criteria: DslValue[SelectionCriteria] | None = None


@dataclass
class S3BucketDestination(PropertyType):
    account_id: DslValue[str] | None = None
    arn: DslValue[str] | None = None
    format: DslValue[str] | None = None
    output_schema_version: DslValue[str] | None = None
    encryption: DslValue[Encryption] | None = None
    prefix: DslValue[str] | None = None


@dataclass
class SSEKMS(PropertyType):
    key_id: DslValue[str] | None = None


@dataclass
class SelectionCriteria(PropertyType):
    delimiter: DslValue[str] | None = None
    max_depth: DslValue[int] | None = None
    min_storage_bytes_percentage: DslValue[float] | None = None


@dataclass
class StorageLensConfiguration(PropertyType):
    account_level: DslValue[AccountLevel] | None = None
    id: DslValue[str] | None = None
    is_enabled: DslValue[bool] | None = None
    aws_org: DslValue[AwsOrg] | None = None
    data_export: DslValue[DataExport] | None = None
    exclude: DslValue[BucketsAndRegions] | None = None
    expanded_prefixes_data_export: (
        DslValue[StorageLensExpandedPrefixesDataExport] | None
    ) = None
    include: DslValue[BucketsAndRegions] | None = None
    prefix_delimiter: DslValue[str] | None = None
    storage_lens_arn: DslValue[str] | None = None


@dataclass
class StorageLensExpandedPrefixesDataExport(PropertyType):
    s3_bucket_destination: DslValue[S3BucketDestination] | None = None
    storage_lens_table_destination: DslValue[StorageLensTableDestination] | None = None


@dataclass
class StorageLensGroupLevel(PropertyType):
    storage_lens_group_selection_criteria: (
        DslValue[StorageLensGroupSelectionCriteria] | None
    ) = None


@dataclass
class StorageLensGroupSelectionCriteria(PropertyType):
    exclude: list[DslValue[str]] = field(default_factory=list)
    include: list[DslValue[str]] = field(default_factory=list)


@dataclass
class StorageLensTableDestination(PropertyType):
    is_enabled: DslValue[bool] | None = None
    encryption: DslValue[Encryption] | None = None
