"""PropertyTypes for AWS::FSx::S3AccessPointAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class FileSystemGID(PropertyType):
    gid: DslValue[float] | None = None


@dataclass
class OntapFileSystemIdentity(PropertyType):
    type_: DslValue[str] | None = None
    unix_user: DslValue[OntapUnixFileSystemUser] | None = None
    windows_user: DslValue[OntapWindowsFileSystemUser] | None = None


@dataclass
class OntapUnixFileSystemUser(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class OntapWindowsFileSystemUser(PropertyType):
    name: DslValue[str] | None = None


@dataclass
class OpenZFSFileSystemIdentity(PropertyType):
    posix_user: DslValue[OpenZFSPosixFileSystemUser] | None = None
    type_: DslValue[str] | None = None


@dataclass
class OpenZFSPosixFileSystemUser(PropertyType):
    gid: DslValue[float] | None = None
    uid: DslValue[float] | None = None
    secondary_gids: list[DslValue[FileSystemGID]] = field(default_factory=list)


@dataclass
class S3AccessPoint(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "resource_arn": "ResourceARN",
    }

    alias: DslValue[str] | None = None
    policy: DslValue[dict[str, Any]] | None = None
    resource_arn: DslValue[str] | None = None
    vpc_configuration: DslValue[S3AccessPointVpcConfiguration] | None = None


@dataclass
class S3AccessPointOntapConfiguration(PropertyType):
    file_system_identity: DslValue[OntapFileSystemIdentity] | None = None
    volume_id: DslValue[str] | None = None


@dataclass
class S3AccessPointOpenZFSConfiguration(PropertyType):
    file_system_identity: DslValue[OpenZFSFileSystemIdentity] | None = None
    volume_id: DslValue[str] | None = None


@dataclass
class S3AccessPointVpcConfiguration(PropertyType):
    vpc_id: DslValue[str] | None = None
