"""PropertyTypes for AWS::ODB::CloudVmCluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DataCollectionOptions(PropertyType):
    is_diagnostics_events_enabled: DslValue[bool] | None = None
    is_health_monitoring_enabled: DslValue[bool] | None = None
    is_incident_logs_enabled: DslValue[bool] | None = None


@dataclass
class DbNode(PropertyType):
    db_server_id: DslValue[str] | None = None
    backup_ip_id: DslValue[str] | None = None
    backup_vnic2_id: DslValue[str] | None = None
    cpu_core_count: DslValue[int] | None = None
    db_node_arn: DslValue[str] | None = None
    db_node_id: DslValue[str] | None = None
    db_node_storage_size_in_g_bs: DslValue[int] | None = None
    db_system_id: DslValue[str] | None = None
    host_ip_id: DslValue[str] | None = None
    hostname: DslValue[str] | None = None
    memory_size_in_g_bs: DslValue[int] | None = None
    ocid: DslValue[str] | None = None
    status: DslValue[str] | None = None
    tags: list[DslValue[Tag]] = field(default_factory=list)
    vnic2_id: DslValue[str] | None = None
    vnic_id: DslValue[str] | None = None
