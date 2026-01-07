"""PropertyTypes for AWS::DynamoDB::Table."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AttributeDefinition(PropertyType):
    attribute_name: DslValue[str] | None = None
    attribute_type: DslValue[str] | None = None


@dataclass
class ContributorInsightsSpecification(PropertyType):
    enabled: DslValue[bool] | None = None
    mode: DslValue[str] | None = None


@dataclass
class Csv(PropertyType):
    delimiter: DslValue[str] | None = None
    header_list: list[DslValue[str]] = field(default_factory=list)


@dataclass
class GlobalSecondaryIndex(PropertyType):
    index_name: DslValue[str] | None = None
    key_schema: list[DslValue[KeySchema]] = field(default_factory=list)
    projection: DslValue[Projection] | None = None
    contributor_insights_specification: (
        DslValue[ContributorInsightsSpecification] | None
    ) = None
    on_demand_throughput: DslValue[OnDemandThroughput] | None = None
    provisioned_throughput: DslValue[ProvisionedThroughput] | None = None
    warm_throughput: DslValue[WarmThroughput] | None = None


@dataclass
class ImportSourceSpecification(PropertyType):
    input_format: DslValue[str] | None = None
    s3_bucket_source: DslValue[S3BucketSource] | None = None
    input_compression_type: DslValue[str] | None = None
    input_format_options: DslValue[InputFormatOptions] | None = None


@dataclass
class InputFormatOptions(PropertyType):
    csv: DslValue[Csv] | None = None


@dataclass
class KeySchema(PropertyType):
    attribute_name: DslValue[str] | None = None
    key_type: DslValue[str] | None = None


@dataclass
class KinesisStreamSpecification(PropertyType):
    stream_arn: DslValue[str] | None = None
    approximate_creation_date_time_precision: DslValue[str] | None = None


@dataclass
class LocalSecondaryIndex(PropertyType):
    index_name: DslValue[str] | None = None
    key_schema: list[DslValue[KeySchema]] = field(default_factory=list)
    projection: DslValue[Projection] | None = None


@dataclass
class OnDemandThroughput(PropertyType):
    max_read_request_units: DslValue[int] | None = None
    max_write_request_units: DslValue[int] | None = None


@dataclass
class PointInTimeRecoverySpecification(PropertyType):
    point_in_time_recovery_enabled: DslValue[bool] | None = None
    recovery_period_in_days: DslValue[int] | None = None


@dataclass
class Projection(PropertyType):
    non_key_attributes: list[DslValue[str]] = field(default_factory=list)
    projection_type: DslValue[str] | None = None


@dataclass
class ProvisionedThroughput(PropertyType):
    read_capacity_units: DslValue[int] | None = None
    write_capacity_units: DslValue[int] | None = None


@dataclass
class ResourcePolicy(PropertyType):
    policy_document: DslValue[dict[str, Any]] | None = None


@dataclass
class S3BucketSource(PropertyType):
    s3_bucket: DslValue[str] | None = None
    s3_bucket_owner: DslValue[str] | None = None
    s3_key_prefix: DslValue[str] | None = None


@dataclass
class SSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyId",
        "sse_enabled": "SSEEnabled",
        "sse_type": "SSEType",
    }

    sse_enabled: DslValue[bool] | None = None
    kms_master_key_id: DslValue[str] | None = None
    sse_type: DslValue[str] | None = None


@dataclass
class StreamSpecification(PropertyType):
    stream_view_type: DslValue[str] | None = None
    resource_policy: DslValue[ResourcePolicy] | None = None


@dataclass
class TimeToLiveSpecification(PropertyType):
    enabled: DslValue[bool] | None = None
    attribute_name: DslValue[str] | None = None


@dataclass
class WarmThroughput(PropertyType):
    read_units_per_second: DslValue[int] | None = None
    write_units_per_second: DslValue[int] | None = None
