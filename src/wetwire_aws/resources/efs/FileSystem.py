"""PropertyTypes for AWS::EFS::FileSystem."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class BackupPolicy(PropertyType):
    status: DslValue[str] | None = None


@dataclass
class ElasticFileSystemTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class FileSystemProtection(PropertyType):
    replication_overwrite_protection: DslValue[str] | None = None


@dataclass
class LifecyclePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transition_to_ia": "TransitionToIA",
    }

    transition_to_archive: DslValue[str] | None = None
    transition_to_ia: DslValue[str] | None = None
    transition_to_primary_storage_class: DslValue[str] | None = None


@dataclass
class ReplicationConfiguration(PropertyType):
    destinations: list[DslValue[ReplicationDestination]] = field(default_factory=list)


@dataclass
class ReplicationDestination(PropertyType):
    availability_zone_name: DslValue[str] | None = None
    file_system_id: DslValue[str] | None = None
    kms_key_id: DslValue[str] | None = None
    region: DslValue[str] | None = None
    role_arn: DslValue[str] | None = None
    status: DslValue[str] | None = None
    status_message: DslValue[str] | None = None
