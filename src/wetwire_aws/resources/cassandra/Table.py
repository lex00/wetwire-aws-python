"""PropertyTypes for AWS::Cassandra::Table."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AutoScalingSetting(PropertyType):
    auto_scaling_disabled: bool | None = None
    maximum_units: int | None = None
    minimum_units: int | None = None
    scaling_policy: ScalingPolicy | None = None


@dataclass
class AutoScalingSpecification(PropertyType):
    read_capacity_auto_scaling: AutoScalingSetting | None = None
    write_capacity_auto_scaling: AutoScalingSetting | None = None


@dataclass
class BillingMode(PropertyType):
    mode: str | None = None
    provisioned_throughput: ProvisionedThroughput | None = None


@dataclass
class CdcSpecification(PropertyType):
    status: str | None = None
    tags: list[Tag] = field(default_factory=list)
    view_type: str | None = None


@dataclass
class ClusteringKeyColumn(PropertyType):
    column: Column | None = None
    order_by: str | None = None


@dataclass
class Column(PropertyType):
    column_name: str | None = None
    column_type: str | None = None


@dataclass
class EncryptionSpecification(PropertyType):
    encryption_type: str | None = None
    kms_key_identifier: str | None = None


@dataclass
class ProvisionedThroughput(PropertyType):
    read_capacity_units: int | None = None
    write_capacity_units: int | None = None


@dataclass
class ReplicaSpecification(PropertyType):
    region: str | None = None
    read_capacity_auto_scaling: AutoScalingSetting | None = None
    read_capacity_units: int | None = None


@dataclass
class ScalingPolicy(PropertyType):
    target_tracking_scaling_policy_configuration: (
        TargetTrackingScalingPolicyConfiguration | None
    ) = None


@dataclass
class TargetTrackingScalingPolicyConfiguration(PropertyType):
    target_value: int | None = None
    disable_scale_in: bool | None = None
    scale_in_cooldown: int | None = None
    scale_out_cooldown: int | None = None


@dataclass
class WarmThroughput(PropertyType):
    read_units_per_second: int | None = None
    write_units_per_second: int | None = None
