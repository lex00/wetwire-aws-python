"""PropertyTypes for AWS::Transfer::User."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class HomeDirectoryMapEntry(PropertyType):
    entry: str | None = None
    target: str | None = None
    type_: str | None = None


@dataclass
class PosixProfile(PropertyType):
    gid: float | None = None
    uid: float | None = None
    secondary_gids: list[Double] = field(default_factory=list)
