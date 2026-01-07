"""PropertyTypes for AWS::EFS::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class AccessPointTag(PropertyType):
    key: DslValue[str] | None = None
    value: DslValue[str] | None = None


@dataclass
class CreationInfo(PropertyType):
    owner_gid: DslValue[str] | None = None
    owner_uid: DslValue[str] | None = None
    permissions: DslValue[str] | None = None


@dataclass
class PosixUser(PropertyType):
    gid: DslValue[str] | None = None
    uid: DslValue[str] | None = None
    secondary_gids: list[DslValue[str]] = field(default_factory=list)


@dataclass
class RootDirectory(PropertyType):
    creation_info: DslValue[CreationInfo] | None = None
    path: DslValue[str] | None = None
