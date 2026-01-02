"""PropertyTypes for AWS::DataSync::LocationFSxOpenZFS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MountOptions(PropertyType):
    version: str | None = None


@dataclass
class NFS(PropertyType):
    mount_options: MountOptions | None = None


@dataclass
class Protocol(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nfs": "NFS",
    }

    nfs: NFS | None = None
