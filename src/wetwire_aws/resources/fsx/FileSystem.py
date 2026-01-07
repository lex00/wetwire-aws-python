"""PropertyTypes for AWS::FSx::FileSystem."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AuditLogConfiguration(PropertyType):
    file_access_audit_log_level: DslValue[str] | None = None
    file_share_access_audit_log_level: DslValue[str] | None = None
    audit_log_destination: DslValue[str] | None = None


@dataclass
class ClientConfigurations(PropertyType):
    clients: DslValue[str] | None = None
    options: list[DslValue[str]] = field(default_factory=list)


@dataclass
class DataReadCacheConfiguration(PropertyType):
    size_gi_b: DslValue[int] | None = None
    sizing_mode: DslValue[str] | None = None


@dataclass
class DiskIopsConfiguration(PropertyType):
    iops: DslValue[int] | None = None
    mode: DslValue[str] | None = None


@dataclass
class LustreConfiguration(PropertyType):
    auto_import_policy: DslValue[str] | None = None
    automatic_backup_retention_days: DslValue[int] | None = None
    copy_tags_to_backups: DslValue[bool] | None = None
    daily_automatic_backup_start_time: DslValue[str] | None = None
    data_compression_type: DslValue[str] | None = None
    data_read_cache_configuration: DslValue[DataReadCacheConfiguration] | None = None
    deployment_type: DslValue[str] | None = None
    drive_cache_type: DslValue[str] | None = None
    efa_enabled: DslValue[bool] | None = None
    export_path: DslValue[str] | None = None
    import_path: DslValue[str] | None = None
    imported_file_chunk_size: DslValue[int] | None = None
    metadata_configuration: DslValue[MetadataConfiguration] | None = None
    per_unit_storage_throughput: DslValue[int] | None = None
    throughput_capacity: DslValue[int] | None = None
    weekly_maintenance_start_time: DslValue[str] | None = None


@dataclass
class MetadataConfiguration(PropertyType):
    iops: DslValue[int] | None = None
    mode: DslValue[str] | None = None


@dataclass
class NfsExports(PropertyType):
    client_configurations: list[DslValue[ClientConfigurations]] = field(
        default_factory=list
    )


@dataclass
class OntapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ha_pairs": "HAPairs",
        "throughput_capacity_per_ha_pair": "ThroughputCapacityPerHAPair",
    }

    deployment_type: DslValue[str] | None = None
    automatic_backup_retention_days: DslValue[int] | None = None
    daily_automatic_backup_start_time: DslValue[str] | None = None
    disk_iops_configuration: DslValue[DiskIopsConfiguration] | None = None
    endpoint_ip_address_range: DslValue[str] | None = None
    endpoint_ipv6_address_range: DslValue[str] | None = None
    fsx_admin_password: DslValue[str] | None = None
    ha_pairs: DslValue[int] | None = None
    preferred_subnet_id: DslValue[str] | None = None
    route_table_ids: list[DslValue[str]] = field(default_factory=list)
    throughput_capacity: DslValue[int] | None = None
    throughput_capacity_per_ha_pair: DslValue[int] | None = None
    weekly_maintenance_start_time: DslValue[str] | None = None


@dataclass
class OpenZFSConfiguration(PropertyType):
    deployment_type: DslValue[str] | None = None
    automatic_backup_retention_days: DslValue[int] | None = None
    copy_tags_to_backups: DslValue[bool] | None = None
    copy_tags_to_volumes: DslValue[bool] | None = None
    daily_automatic_backup_start_time: DslValue[str] | None = None
    disk_iops_configuration: DslValue[DiskIopsConfiguration] | None = None
    endpoint_ip_address_range: DslValue[str] | None = None
    endpoint_ipv6_address_range: DslValue[str] | None = None
    options: list[DslValue[str]] = field(default_factory=list)
    preferred_subnet_id: DslValue[str] | None = None
    read_cache_configuration: DslValue[ReadCacheConfiguration] | None = None
    root_volume_configuration: DslValue[RootVolumeConfiguration] | None = None
    route_table_ids: list[DslValue[str]] = field(default_factory=list)
    throughput_capacity: DslValue[int] | None = None
    weekly_maintenance_start_time: DslValue[str] | None = None


@dataclass
class ReadCacheConfiguration(PropertyType):
    size_gi_b: DslValue[int] | None = None
    sizing_mode: DslValue[str] | None = None


@dataclass
class RootVolumeConfiguration(PropertyType):
    copy_tags_to_snapshots: DslValue[bool] | None = None
    data_compression_type: DslValue[str] | None = None
    nfs_exports: list[DslValue[NfsExports]] = field(default_factory=list)
    read_only: DslValue[bool] | None = None
    record_size_ki_b: DslValue[int] | None = None
    user_and_group_quotas: list[DslValue[UserAndGroupQuotas]] = field(
        default_factory=list
    )


@dataclass
class SelfManagedActiveDirectoryConfiguration(PropertyType):
    dns_ips: list[DslValue[str]] = field(default_factory=list)
    domain_join_service_account_secret: DslValue[str] | None = None
    domain_name: DslValue[str] | None = None
    file_system_administrators_group: DslValue[str] | None = None
    organizational_unit_distinguished_name: DslValue[str] | None = None
    password: DslValue[str] | None = None
    user_name: DslValue[str] | None = None


@dataclass
class UserAndGroupQuotas(PropertyType):
    id: DslValue[int] | None = None
    storage_capacity_quota_gi_b: DslValue[int] | None = None
    type_: DslValue[str] | None = None


@dataclass
class WindowsConfiguration(PropertyType):
    throughput_capacity: DslValue[int] | None = None
    active_directory_id: DslValue[str] | None = None
    aliases: list[DslValue[str]] = field(default_factory=list)
    audit_log_configuration: DslValue[AuditLogConfiguration] | None = None
    automatic_backup_retention_days: DslValue[int] | None = None
    copy_tags_to_backups: DslValue[bool] | None = None
    daily_automatic_backup_start_time: DslValue[str] | None = None
    deployment_type: DslValue[str] | None = None
    disk_iops_configuration: DslValue[DiskIopsConfiguration] | None = None
    preferred_subnet_id: DslValue[str] | None = None
    self_managed_active_directory_configuration: (
        DslValue[SelfManagedActiveDirectoryConfiguration] | None
    ) = None
    weekly_maintenance_start_time: DslValue[str] | None = None
