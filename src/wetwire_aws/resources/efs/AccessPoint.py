"""PropertyTypes for AWS::EFS::AccessPoint."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AccessPointTag(PropertyType):
    key: str | None = None
    value: str | None = None


@dataclass
class CreationInfo(PropertyType):
    owner_gid: str | None = None
    owner_uid: str | None = None
    permissions: str | None = None


@dataclass
class PosixUser(PropertyType):
    gid: str | None = None
    uid: str | None = None
    secondary_gids: list[String] = field(default_factory=list)


@dataclass
class RootDirectory(PropertyType):
    creation_info: CreationInfo | None = None
    path: str | None = None
