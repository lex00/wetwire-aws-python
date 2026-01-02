"""PropertyTypes for AWS::FSx::S3AccessPointAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FileSystemGID(PropertyType):
    gid: float | None = None


@dataclass
class OntapFileSystemIdentity(PropertyType):
    type_: str | None = None
    unix_user: OntapUnixFileSystemUser | None = None
    windows_user: OntapWindowsFileSystemUser | None = None


@dataclass
class OntapUnixFileSystemUser(PropertyType):
    name: str | None = None


@dataclass
class OntapWindowsFileSystemUser(PropertyType):
    name: str | None = None


@dataclass
class OpenZFSFileSystemIdentity(PropertyType):
    posix_user: OpenZFSPosixFileSystemUser | None = None
    type_: str | None = None


@dataclass
class OpenZFSPosixFileSystemUser(PropertyType):
    gid: float | None = None
    uid: float | None = None
    secondary_gids: list[FileSystemGID] = field(default_factory=list)


@dataclass
class S3AccessPoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    alias: str | None = None
    policy: dict[str, Any] | None = None
    resource_arn: str | None = None
    vpc_configuration: S3AccessPointVpcConfiguration | None = None


@dataclass
class S3AccessPointOntapConfiguration(PropertyType):
    file_system_identity: OntapFileSystemIdentity | None = None
    volume_id: str | None = None


@dataclass
class S3AccessPointOpenZFSConfiguration(PropertyType):
    file_system_identity: OpenZFSFileSystemIdentity | None = None
    volume_id: str | None = None


@dataclass
class S3AccessPointVpcConfiguration(PropertyType):
    vpc_id: str | None = None
