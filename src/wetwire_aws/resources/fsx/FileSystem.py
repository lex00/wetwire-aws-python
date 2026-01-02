"""PropertyTypes for AWS::FSx::FileSystem."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuditLogConfiguration(PropertyType):
    file_access_audit_log_level: str | None = None
    file_share_access_audit_log_level: str | None = None
    audit_log_destination: str | None = None


@dataclass
class ClientConfigurations(PropertyType):
    clients: str | None = None
    options: list[String] = field(default_factory=list)


@dataclass
class DataReadCacheConfiguration(PropertyType):
    size_gi_b: int | None = None
    sizing_mode: str | None = None


@dataclass
class DiskIopsConfiguration(PropertyType):
    iops: int | None = None
    mode: str | None = None


@dataclass
class LustreConfiguration(PropertyType):
    auto_import_policy: str | None = None
    automatic_backup_retention_days: int | None = None
    copy_tags_to_backups: bool | None = None
    daily_automatic_backup_start_time: str | None = None
    data_compression_type: str | None = None
    data_read_cache_configuration: DataReadCacheConfiguration | None = None
    deployment_type: str | None = None
    drive_cache_type: str | None = None
    efa_enabled: bool | None = None
    export_path: str | None = None
    import_path: str | None = None
    imported_file_chunk_size: int | None = None
    metadata_configuration: MetadataConfiguration | None = None
    per_unit_storage_throughput: int | None = None
    throughput_capacity: int | None = None
    weekly_maintenance_start_time: str | None = None


@dataclass
class MetadataConfiguration(PropertyType):
    iops: int | None = None
    mode: str | None = None


@dataclass
class NfsExports(PropertyType):
    client_configurations: list[ClientConfigurations] = field(default_factory=list)


@dataclass
class OntapConfiguration(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "ha_pairs": "HAPairs",
        "throughput_capacity_per_ha_pair": "ThroughputCapacityPerHAPair",
    }

    deployment_type: str | None = None
    automatic_backup_retention_days: int | None = None
    daily_automatic_backup_start_time: str | None = None
    disk_iops_configuration: DiskIopsConfiguration | None = None
    endpoint_ip_address_range: str | None = None
    endpoint_ipv6_address_range: str | None = None
    fsx_admin_password: str | None = None
    ha_pairs: int | None = None
    preferred_subnet_id: str | None = None
    route_table_ids: list[String] = field(default_factory=list)
    throughput_capacity: int | None = None
    throughput_capacity_per_ha_pair: int | None = None
    weekly_maintenance_start_time: str | None = None


@dataclass
class OpenZFSConfiguration(PropertyType):
    deployment_type: str | None = None
    automatic_backup_retention_days: int | None = None
    copy_tags_to_backups: bool | None = None
    copy_tags_to_volumes: bool | None = None
    daily_automatic_backup_start_time: str | None = None
    disk_iops_configuration: DiskIopsConfiguration | None = None
    endpoint_ip_address_range: str | None = None
    endpoint_ipv6_address_range: str | None = None
    options: list[String] = field(default_factory=list)
    preferred_subnet_id: str | None = None
    read_cache_configuration: ReadCacheConfiguration | None = None
    root_volume_configuration: RootVolumeConfiguration | None = None
    route_table_ids: list[String] = field(default_factory=list)
    throughput_capacity: int | None = None
    weekly_maintenance_start_time: str | None = None


@dataclass
class ReadCacheConfiguration(PropertyType):
    size_gi_b: int | None = None
    sizing_mode: str | None = None


@dataclass
class RootVolumeConfiguration(PropertyType):
    copy_tags_to_snapshots: bool | None = None
    data_compression_type: str | None = None
    nfs_exports: list[NfsExports] = field(default_factory=list)
    read_only: bool | None = None
    record_size_ki_b: int | None = None
    user_and_group_quotas: list[UserAndGroupQuotas] = field(default_factory=list)


@dataclass
class SelfManagedActiveDirectoryConfiguration(PropertyType):
    dns_ips: list[String] = field(default_factory=list)
    domain_join_service_account_secret: str | None = None
    domain_name: str | None = None
    file_system_administrators_group: str | None = None
    organizational_unit_distinguished_name: str | None = None
    password: str | None = None
    user_name: str | None = None


@dataclass
class UserAndGroupQuotas(PropertyType):
    id: int | None = None
    storage_capacity_quota_gi_b: int | None = None
    type_: str | None = None


@dataclass
class WindowsConfiguration(PropertyType):
    throughput_capacity: int | None = None
    active_directory_id: str | None = None
    aliases: list[String] = field(default_factory=list)
    audit_log_configuration: AuditLogConfiguration | None = None
    automatic_backup_retention_days: int | None = None
    copy_tags_to_backups: bool | None = None
    daily_automatic_backup_start_time: str | None = None
    deployment_type: str | None = None
    disk_iops_configuration: DiskIopsConfiguration | None = None
    preferred_subnet_id: str | None = None
    self_managed_active_directory_configuration: (
        SelfManagedActiveDirectoryConfiguration | None
    ) = None
    weekly_maintenance_start_time: str | None = None
