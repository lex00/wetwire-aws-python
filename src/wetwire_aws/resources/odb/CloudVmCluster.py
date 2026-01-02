"""PropertyTypes for AWS::ODB::CloudVmCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DataCollectionOptions(PropertyType):
    is_diagnostics_events_enabled: bool | None = None
    is_health_monitoring_enabled: bool | None = None
    is_incident_logs_enabled: bool | None = None


@dataclass
class DbNode(PropertyType):
    db_server_id: str | None = None
    backup_ip_id: str | None = None
    backup_vnic2_id: str | None = None
    cpu_core_count: int | None = None
    db_node_arn: str | None = None
    db_node_id: str | None = None
    db_node_storage_size_in_g_bs: int | None = None
    db_system_id: str | None = None
    host_ip_id: str | None = None
    hostname: str | None = None
    memory_size_in_g_bs: int | None = None
    ocid: str | None = None
    status: str | None = None
    tags: list[Tag] = field(default_factory=list)
    vnic2_id: str | None = None
    vnic_id: str | None = None
