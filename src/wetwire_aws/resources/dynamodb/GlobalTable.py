"""PropertyTypes for AWS::DynamoDB::GlobalTable."""

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
class CapacityAutoScalingSettings(PropertyType):
    max_capacity: DslValue[int] | None = None
    min_capacity: DslValue[int] | None = None
    target_tracking_scaling_policy_configuration: (
        DslValue[TargetTrackingScalingPolicyConfiguration] | None
    ) = None
    seed_capacity: DslValue[int] | None = None


@dataclass
class ContributorInsightsSpecification(PropertyType):
    enabled: DslValue[bool] | None = None
    mode: DslValue[str] | None = None


@dataclass
class GlobalSecondaryIndex(PropertyType):
    index_name: DslValue[str] | None = None
    key_schema: list[DslValue[KeySchema]] = field(default_factory=list)
    projection: DslValue[Projection] | None = None
    warm_throughput: DslValue[WarmThroughput] | None = None
    write_on_demand_throughput_settings: (
        DslValue[WriteOnDemandThroughputSettings] | None
    ) = None
    write_provisioned_throughput_settings: (
        DslValue[WriteProvisionedThroughputSettings] | None
    ) = None


@dataclass
class GlobalTableWitness(PropertyType):
    region: DslValue[str] | None = None


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
class PointInTimeRecoverySpecification(PropertyType):
    point_in_time_recovery_enabled: DslValue[bool] | None = None
    recovery_period_in_days: DslValue[int] | None = None


@dataclass
class Projection(PropertyType):
    non_key_attributes: list[DslValue[str]] = field(default_factory=list)
    projection_type: DslValue[str] | None = None


@dataclass
class ReadOnDemandThroughputSettings(PropertyType):
    max_read_request_units: DslValue[int] | None = None


@dataclass
class ReadProvisionedThroughputSettings(PropertyType):
    read_capacity_auto_scaling_settings: (
        DslValue[CapacityAutoScalingSettings] | None
    ) = None
    read_capacity_units: DslValue[int] | None = None


@dataclass
class ReplicaGlobalSecondaryIndexSpecification(PropertyType):
    index_name: DslValue[str] | None = None
    contributor_insights_specification: (
        DslValue[ContributorInsightsSpecification] | None
    ) = None
    read_on_demand_throughput_settings: (
        DslValue[ReadOnDemandThroughputSettings] | None
    ) = None
    read_provisioned_throughput_settings: (
        DslValue[ReadProvisionedThroughputSettings] | None
    ) = None


@dataclass
class ReplicaSSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "kms_master_key_id": "KMSMasterKeyId",
    }

    kms_master_key_id: DslValue[str] | None = None


@dataclass
class ReplicaSpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_specification": "SSESpecification",
    }

    region: DslValue[str] | None = None
    contributor_insights_specification: (
        DslValue[ContributorInsightsSpecification] | None
    ) = None
    deletion_protection_enabled: DslValue[bool] | None = None
    global_secondary_indexes: list[
        DslValue[ReplicaGlobalSecondaryIndexSpecification]
    ] = field(default_factory=list)
    kinesis_stream_specification: DslValue[KinesisStreamSpecification] | None = None
    point_in_time_recovery_specification: (
        DslValue[PointInTimeRecoverySpecification] | None
    ) = None
    read_on_demand_throughput_settings: (
        DslValue[ReadOnDemandThroughputSettings] | None
    ) = None
    read_provisioned_throughput_settings: (
        DslValue[ReadProvisionedThroughputSettings] | None
    ) = None
    replica_stream_specification: DslValue[ReplicaStreamSpecification] | None = None
    resource_policy: DslValue[ResourcePolicy] | None = None
    sse_specification: DslValue[ReplicaSSESpecification] | None = None
    table_class: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)


@dataclass
class ReplicaStreamSpecification(PropertyType):
    resource_policy: DslValue[ResourcePolicy] | None = None


@dataclass
class ResourcePolicy(PropertyType):
    policy_document: DslValue[dict[str, Any]] | None = None


@dataclass
class SSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
        "sse_type": "SSEType",
    }

    sse_enabled: DslValue[bool] | None = None
    sse_type: DslValue[str] | None = None


@dataclass
class StreamSpecification(PropertyType):
    stream_view_type: DslValue[str] | None = None


@dataclass
class TargetTrackingScalingPolicyConfiguration(PropertyType):
    target_value: DslValue[float] | None = None
    disable_scale_in: DslValue[bool] | None = None
    scale_in_cooldown: DslValue[int] | None = None
    scale_out_cooldown: DslValue[int] | None = None


@dataclass
class TimeToLiveSpecification(PropertyType):
    enabled: DslValue[bool] | None = None
    attribute_name: DslValue[str] | None = None


@dataclass
class WarmThroughput(PropertyType):
    read_units_per_second: DslValue[int] | None = None
    write_units_per_second: DslValue[int] | None = None


@dataclass
class WriteOnDemandThroughputSettings(PropertyType):
    max_write_request_units: DslValue[int] | None = None


@dataclass
class WriteProvisionedThroughputSettings(PropertyType):
    write_capacity_auto_scaling_settings: (
        DslValue[CapacityAutoScalingSettings] | None
    ) = None
