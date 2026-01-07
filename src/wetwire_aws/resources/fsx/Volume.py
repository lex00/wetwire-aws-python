"""PropertyTypes for AWS::FSx::Volume."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AggregateConfiguration(PropertyType):
    aggregates: list[DslValue[str]] = field(default_factory=list)
    constituents_per_aggregate: DslValue[int] | None = None


@dataclass
class AutocommitPeriod(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class ClientConfigurations(PropertyType):
    clients: DslValue[str] | None = None
    options: list[DslValue[str]] = field(default_factory=list)


@dataclass
class NfsExports(PropertyType):
    client_configurations: list[DslValue[ClientConfigurations]] = field(
        default_factory=list
    )


@dataclass
class OntapConfiguration(PropertyType):
    storage_virtual_machine_id: DslValue[str] | None = None
    aggregate_configuration: DslValue[AggregateConfiguration] | None = None
    copy_tags_to_backups: DslValue[str] | None = None
    junction_path: DslValue[str] | None = None
    ontap_volume_type: DslValue[str] | None = None
    security_style: DslValue[str] | None = None
    size_in_bytes: DslValue[str] | None = None
    size_in_megabytes: DslValue[str] | None = None
    snaplock_configuration: DslValue[SnaplockConfiguration] | None = None
    snapshot_policy: DslValue[str] | None = None
    storage_efficiency_enabled: DslValue[str] | None = None
    tiering_policy: DslValue[TieringPolicy] | None = None
    volume_style: DslValue[str] | None = None


@dataclass
class OpenZFSConfiguration(PropertyType):
    parent_volume_id: DslValue[str] | None = None
    copy_tags_to_snapshots: DslValue[bool] | None = None
    data_compression_type: DslValue[str] | None = None
    nfs_exports: list[DslValue[NfsExports]] = field(default_factory=list)
    options: list[DslValue[str]] = field(default_factory=list)
    origin_snapshot: DslValue[OriginSnapshot] | None = None
    read_only: DslValue[bool] | None = None
    record_size_ki_b: DslValue[int] | None = None
    storage_capacity_quota_gi_b: DslValue[int] | None = None
    storage_capacity_reservation_gi_b: DslValue[int] | None = None
    user_and_group_quotas: list[DslValue[UserAndGroupQuotas]] = field(
        default_factory=list
    )


@dataclass
class OriginSnapshot(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_arn": "SnapshotARN",
    }

    copy_strategy: DslValue[str] | None = None
    snapshot_arn: DslValue[str] | None = None


@dataclass
class RetentionPeriod(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[int] | None = None


@dataclass
class SnaplockConfiguration(PropertyType):
    snaplock_type: DslValue[str] | None = None
    audit_log_volume: DslValue[str] | None = None
    autocommit_period: DslValue[AutocommitPeriod] | None = None
    privileged_delete: DslValue[str] | None = None
    retention_period: DslValue[SnaplockRetentionPeriod] | None = None
    volume_append_mode_enabled: DslValue[str] | None = None


@dataclass
class SnaplockRetentionPeriod(PropertyType):
    default_retention: DslValue[RetentionPeriod] | None = None
    maximum_retention: DslValue[RetentionPeriod] | None = None
    minimum_retention: DslValue[RetentionPeriod] | None = None


@dataclass
class TieringPolicy(PropertyType):
    cooling_period: DslValue[int] | None = None
    name: DslValue[str] | None = None


@dataclass
class UserAndGroupQuotas(PropertyType):
    id: DslValue[int] | None = None
    storage_capacity_quota_gi_b: DslValue[int] | None = None
    type_: DslValue[str] | None = None
