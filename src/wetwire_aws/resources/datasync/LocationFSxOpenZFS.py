"""PropertyTypes for AWS::DataSync::LocationFSxOpenZFS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MountOptions(PropertyType):
    version: DslValue[str] | None = None


@dataclass
class NFS(PropertyType):
    mount_options: DslValue[MountOptions] | None = None


@dataclass
class Protocol(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "nfs": "NFS",
    }

    nfs: DslValue[NFS] | None = None
