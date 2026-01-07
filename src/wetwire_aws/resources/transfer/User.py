"""PropertyTypes for AWS::Transfer::User."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class HomeDirectoryMapEntry(PropertyType):
    entry: DslValue[str] | None = None
    target: DslValue[str] | None = None
    type_: DslValue[str] | None = None


@dataclass
class PosixProfile(PropertyType):
    gid: DslValue[float] | None = None
    uid: DslValue[float] | None = None
    secondary_gids: list[DslValue[float]] = field(default_factory=list)
