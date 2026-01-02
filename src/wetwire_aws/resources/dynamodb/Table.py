"""PropertyTypes for AWS::DynamoDB::Table."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeDefinition(PropertyType):
    attribute_name: str | None = None
    attribute_type: str | None = None


@dataclass
class ContributorInsightsSpecification(PropertyType):
    enabled: bool | None = None
    mode: str | None = None


@dataclass
class Csv(PropertyType):
    delimiter: str | None = None
    header_list: list[String] = field(default_factory=list)


@dataclass
class GlobalSecondaryIndex(PropertyType):
    index_name: str | None = None
    key_schema: list[KeySchema] = field(default_factory=list)
    projection: Projection | None = None
    contributor_insights_specification: ContributorInsightsSpecification | None = None
    on_demand_throughput: OnDemandThroughput | None = None
    provisioned_throughput: ProvisionedThroughput | None = None
    warm_throughput: WarmThroughput | None = None


@dataclass
class ImportSourceSpecification(PropertyType):
    input_format: str | None = None
    s3_bucket_source: S3BucketSource | None = None
    input_compression_type: str | None = None
    input_format_options: InputFormatOptions | None = None


@dataclass
class InputFormatOptions(PropertyType):
    csv: Csv | None = None


@dataclass
class KeySchema(PropertyType):
    attribute_name: str | None = None
    key_type: str | None = None


@dataclass
class KinesisStreamSpecification(PropertyType):
    stream_arn: str | None = None
    approximate_creation_date_time_precision: str | None = None


@dataclass
class LocalSecondaryIndex(PropertyType):
    index_name: str | None = None
    key_schema: list[KeySchema] = field(default_factory=list)
    projection: Projection | None = None


@dataclass
class OnDemandThroughput(PropertyType):
    max_read_request_units: int | None = None
    max_write_request_units: int | None = None


@dataclass
class PointInTimeRecoverySpecification(PropertyType):
    point_in_time_recovery_enabled: bool | None = None
    recovery_period_in_days: int | None = None


@dataclass
class Projection(PropertyType):
    non_key_attributes: list[String] = field(default_factory=list)
    projection_type: str | None = None


@dataclass
class ProvisionedThroughput(PropertyType):
    read_capacity_units: int | None = None
    write_capacity_units: int | None = None


@dataclass
class ResourcePolicy(PropertyType):
    policy_document: dict[str, Any] | None = None


@dataclass
class S3BucketSource(PropertyType):
    s3_bucket: str | None = None
    s3_bucket_owner: str | None = None
    s3_key_prefix: str | None = None


@dataclass
class SSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyId",
        "sse_enabled": "SSEEnabled",
        "sse_type": "SSEType",
    }

    sse_enabled: bool | None = None
    kms_master_key_id: str | None = None
    sse_type: str | None = None


@dataclass
class StreamSpecification(PropertyType):
    stream_view_type: str | None = None
    resource_policy: ResourcePolicy | None = None


@dataclass
class TimeToLiveSpecification(PropertyType):
    enabled: bool | None = None
    attribute_name: str | None = None


@dataclass
class WarmThroughput(PropertyType):
    read_units_per_second: int | None = None
    write_units_per_second: int | None = None
