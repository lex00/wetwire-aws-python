"""PropertyTypes for AWS::Lambda::Url."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Cors(PropertyType):
    allow_credentials: bool | None = None
    allow_headers: list[String] = field(default_factory=list)
    allow_methods: list[String] = field(default_factory=list)
    allow_origins: list[String] = field(default_factory=list)
    expose_headers: list[String] = field(default_factory=list)
    max_age: int | None = None
