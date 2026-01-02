"""PropertyTypes for AWS::FSx::Volume."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AggregateConfiguration(PropertyType):
    aggregates: list[String] = field(default_factory=list)
    constituents_per_aggregate: int | None = None


@dataclass
class AutocommitPeriod(PropertyType):
    type_: str | None = None
    value: int | None = None


@dataclass
class ClientConfigurations(PropertyType):
    clients: str | None = None
    options: list[String] = field(default_factory=list)


@dataclass
class NfsExports(PropertyType):
    client_configurations: list[ClientConfigurations] = field(default_factory=list)


@dataclass
class OntapConfiguration(PropertyType):
    storage_virtual_machine_id: str | None = None
    aggregate_configuration: AggregateConfiguration | None = None
    copy_tags_to_backups: str | None = None
    junction_path: str | None = None
    ontap_volume_type: str | None = None
    security_style: str | None = None
    size_in_bytes: str | None = None
    size_in_megabytes: str | None = None
    snaplock_configuration: SnaplockConfiguration | None = None
    snapshot_policy: str | None = None
    storage_efficiency_enabled: str | None = None
    tiering_policy: TieringPolicy | None = None
    volume_style: str | None = None


@dataclass
class OpenZFSConfiguration(PropertyType):
    parent_volume_id: str | None = None
    copy_tags_to_snapshots: bool | None = None
    data_compression_type: str | None = None
    nfs_exports: list[NfsExports] = field(default_factory=list)
    options: list[String] = field(default_factory=list)
    origin_snapshot: OriginSnapshot | None = None
    read_only: bool | None = None
    record_size_ki_b: int | None = None
    storage_capacity_quota_gi_b: int | None = None
    storage_capacity_reservation_gi_b: int | None = None
    user_and_group_quotas: list[UserAndGroupQuotas] = field(default_factory=list)


@dataclass
class OriginSnapshot(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "snapshot_arn": "SnapshotARN",
    }

    copy_strategy: str | None = None
    snapshot_arn: str | None = None


@dataclass
class RetentionPeriod(PropertyType):
    type_: str | None = None
    value: int | None = None


@dataclass
class SnaplockConfiguration(PropertyType):
    snaplock_type: str | None = None
    audit_log_volume: str | None = None
    autocommit_period: AutocommitPeriod | None = None
    privileged_delete: str | None = None
    retention_period: SnaplockRetentionPeriod | None = None
    volume_append_mode_enabled: str | None = None


@dataclass
class SnaplockRetentionPeriod(PropertyType):
    default_retention: RetentionPeriod | None = None
    maximum_retention: RetentionPeriod | None = None
    minimum_retention: RetentionPeriod | None = None


@dataclass
class TieringPolicy(PropertyType):
    cooling_period: int | None = None
    name: str | None = None


@dataclass
class UserAndGroupQuotas(PropertyType):
    id: int | None = None
    storage_capacity_quota_gi_b: int | None = None
    type_: str | None = None
