"""PropertyTypes for AWS::Cassandra::Type."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Field(PropertyType):
    field_name: str | None = None
    field_type: str | None = None
