"""PropertyTypes for AWS::DataSync::LocationFSxONTAP."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class NFS(PropertyType):
    mount_options: DslValue[NfsMountOptions] | None = None


@dataclass
class NfsMountOptions(PropertyType):
    version: DslValue[str] | None = None


@dataclass
class Protocol(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nfs": "NFS",
        "smb": "SMB",
    }

    nfs: DslValue[NFS] | None = None
    smb: DslValue[SMB] | None = None


@dataclass
class SMB(PropertyType):
    mount_options: DslValue[SmbMountOptions] | None = None
    password: DslValue[str] | None = None
    user: DslValue[str] | None = None
    domain: DslValue[str] | None = None


@dataclass
class SmbMountOptions(PropertyType):
    version: DslValue[str] | None = None
