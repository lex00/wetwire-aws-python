"""PropertyTypes for AWS::EntityResolution::SchemaMapping."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SchemaInputAttribute(PropertyType):
    field_name: str | None = None
    type_: str | None = None
    group_name: str | None = None
    hashed: bool | None = None
    match_key: str | None = None
    sub_type: str | None = None
