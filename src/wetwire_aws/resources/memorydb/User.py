"""PropertyTypes for AWS::MemoryDB::User."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthenticationMode(PropertyType):
    passwords: list[String] = field(default_factory=list)
    type_: str | None = None
