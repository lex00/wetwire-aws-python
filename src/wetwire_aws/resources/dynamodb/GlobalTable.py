"""PropertyTypes for AWS::DynamoDB::GlobalTable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AttributeDefinition(PropertyType):
    attribute_name: str | None = None
    attribute_type: str | None = None


@dataclass
class CapacityAutoScalingSettings(PropertyType):
    max_capacity: int | None = None
    min_capacity: int | None = None
    target_tracking_scaling_policy_configuration: (
        TargetTrackingScalingPolicyConfiguration | None
    ) = None
    seed_capacity: int | None = None


@dataclass
class ContributorInsightsSpecification(PropertyType):
    enabled: bool | None = None
    mode: str | None = None


@dataclass
class GlobalSecondaryIndex(PropertyType):
    index_name: str | None = None
    key_schema: list[KeySchema] = field(default_factory=list)
    projection: Projection | None = None
    warm_throughput: WarmThroughput | None = None
    write_on_demand_throughput_settings: WriteOnDemandThroughputSettings | None = None
    write_provisioned_throughput_settings: WriteProvisionedThroughputSettings | None = (
        None
    )


@dataclass
class GlobalTableWitness(PropertyType):
    region: str | None = None


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
class PointInTimeRecoverySpecification(PropertyType):
    point_in_time_recovery_enabled: bool | None = None
    recovery_period_in_days: int | None = None


@dataclass
class Projection(PropertyType):
    non_key_attributes: list[String] = field(default_factory=list)
    projection_type: str | None = None


@dataclass
class ReadOnDemandThroughputSettings(PropertyType):
    max_read_request_units: int | None = None


@dataclass
class ReadProvisionedThroughputSettings(PropertyType):
    read_capacity_auto_scaling_settings: CapacityAutoScalingSettings | None = None
    read_capacity_units: int | None = None


@dataclass
class ReplicaGlobalSecondaryIndexSpecification(PropertyType):
    index_name: str | None = None
    contributor_insights_specification: ContributorInsightsSpecification | None = None
    read_on_demand_throughput_settings: ReadOnDemandThroughputSettings | None = None
    read_provisioned_throughput_settings: ReadProvisionedThroughputSettings | None = (
        None
    )


@dataclass
class ReplicaSSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyId",
    }

    kms_master_key_id: str | None = None


@dataclass
class ReplicaSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_specification": "SSESpecification",
    }

    region: str | None = None
    contributor_insights_specification: ContributorInsightsSpecification | None = None
    deletion_protection_enabled: bool | None = None
    global_secondary_indexes: list[ReplicaGlobalSecondaryIndexSpecification] = field(
        default_factory=list
    )
    kinesis_stream_specification: KinesisStreamSpecification | None = None
    point_in_time_recovery_specification: PointInTimeRecoverySpecification | None = None
    read_on_demand_throughput_settings: ReadOnDemandThroughputSettings | None = None
    read_provisioned_throughput_settings: ReadProvisionedThroughputSettings | None = (
        None
    )
    replica_stream_specification: ReplicaStreamSpecification | None = None
    resource_policy: ResourcePolicy | None = None
    sse_specification: ReplicaSSESpecification | None = None
    table_class: str | None = None
    tags: list[Tag] = field(default_factory=list)


@dataclass
class ReplicaStreamSpecification(PropertyType):
    resource_policy: ResourcePolicy | None = None


@dataclass
class ResourcePolicy(PropertyType):
    policy_document: dict[str, Any] | None = None


@dataclass
class SSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
        "sse_type": "SSEType",
    }

    sse_enabled: bool | None = None
    sse_type: str | None = None


@dataclass
class StreamSpecification(PropertyType):
    stream_view_type: str | None = None


@dataclass
class TargetTrackingScalingPolicyConfiguration(PropertyType):
    target_value: float | None = None
    disable_scale_in: bool | None = None
    scale_in_cooldown: int | None = None
    scale_out_cooldown: int | None = None


@dataclass
class TimeToLiveSpecification(PropertyType):
    enabled: bool | None = None
    attribute_name: str | None = None


@dataclass
class WarmThroughput(PropertyType):
    read_units_per_second: int | None = None
    write_units_per_second: int | None = None


@dataclass
class WriteOnDemandThroughputSettings(PropertyType):
    max_write_request_units: int | None = None


@dataclass
class WriteProvisionedThroughputSettings(PropertyType):
    write_capacity_auto_scaling_settings: CapacityAutoScalingSettings | None = None
