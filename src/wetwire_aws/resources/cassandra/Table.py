"""PropertyTypes for AWS::Cassandra::Table."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AutoScalingSetting(PropertyType):
    auto_scaling_disabled: DslValue[bool] | None = None
    maximum_units: DslValue[int] | None = None
    minimum_units: DslValue[int] | None = None
    scaling_policy: DslValue[ScalingPolicy] | None = None


@dataclass
class AutoScalingSpecification(PropertyType):
    read_capacity_auto_scaling: DslValue[AutoScalingSetting] | None = None
    write_capacity_auto_scaling: DslValue[AutoScalingSetting] | None = None


@dataclass
class BillingMode(PropertyType):
    mode: DslValue[str] | None = None
    provisioned_throughput: DslValue[ProvisionedThroughput] | None = None


@dataclass
class CdcSpecification(PropertyType):
    status: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
    view_type: DslValue[str] | None = None


@dataclass
class ClusteringKeyColumn(PropertyType):
    column: DslValue[Column] | None = None
    order_by: DslValue[str] | None = None


@dataclass
class Column(PropertyType):
    column_name: DslValue[str] | None = None
    column_type: DslValue[str] | None = None


@dataclass
class EncryptionSpecification(PropertyType):
    encryption_type: DslValue[str] | None = None
    kms_key_identifier: DslValue[str] | None = None


@dataclass
class ProvisionedThroughput(PropertyType):
    read_capacity_units: DslValue[int] | None = None
    write_capacity_units: DslValue[int] | None = None


@dataclass
class ReplicaSpecification(PropertyType):
    region: DslValue[str] | None = None
    read_capacity_auto_scaling: DslValue[AutoScalingSetting] | None = None
    read_capacity_units: DslValue[int] | None = None


@dataclass
class ScalingPolicy(PropertyType):
    target_tracking_scaling_policy_configuration: (
        DslValue[TargetTrackingScalingPolicyConfiguration] | None
    ) = None


@dataclass
class TargetTrackingScalingPolicyConfiguration(PropertyType):
    target_value: DslValue[int] | None = None
    disable_scale_in: DslValue[bool] | None = None
    scale_in_cooldown: DslValue[int] | None = None
    scale_out_cooldown: DslValue[int] | None = None


@dataclass
class WarmThroughput(PropertyType):
    read_units_per_second: DslValue[int] | None = None
    write_units_per_second: DslValue[int] | None = None
