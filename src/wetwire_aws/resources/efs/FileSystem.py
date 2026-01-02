"""PropertyTypes for AWS::EFS::FileSystem."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class BackupPolicy(PropertyType):
    status: str | None = None


@dataclass
class ElasticFileSystemTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class FileSystemProtection(PropertyType):
    replication_overwrite_protection: str | None = None


@dataclass
class LifecyclePolicy(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "transition_to_ia": "TransitionToIA",
    }

    transition_to_archive: str | None = None
    transition_to_ia: str | None = None
    transition_to_primary_storage_class: str | None = None


@dataclass
class ReplicationConfiguration(PropertyType):
    destinations: list[ReplicationDestination] = field(default_factory=list)


@dataclass
class ReplicationDestination(PropertyType):
    availability_zone_name: str | None = None
    file_system_id: str | None = None
    kms_key_id: str | None = None
    region: str | None = None
    role_arn: str | None = None
    status: str | None = None
    status_message: str | None = None
