"""PropertyTypes for AWS::DataSync::LocationFSxONTAP."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class NFS(PropertyType):
    mount_options: NfsMountOptions | None = None


@dataclass
class NfsMountOptions(PropertyType):
    version: str | None = None


@dataclass
class Protocol(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nfs": "NFS",
        "smb": "SMB",
    }

    nfs: NFS | None = None
    smb: SMB | None = None


@dataclass
class SMB(PropertyType):
    mount_options: SmbMountOptions | None = None
    password: str | None = None
    user: str | None = None
    domain: str | None = None


@dataclass
class SmbMountOptions(PropertyType):
    version: str | None = None
