"""PropertyTypes for AWS::ElastiCache::User."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class AuthenticationMode(PropertyType):
    type_: str | None = None
    passwords: list[String] = field(default_factory=list)
