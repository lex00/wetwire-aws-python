"""PropertyTypes for AWS::Glue::Schema."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Registry(PropertyType):
    arn: str | None = None
    name: str | None = None


@dataclass
class SchemaVersion(PropertyType):
    is_latest: bool | None = None
    version_number: int | None = None
