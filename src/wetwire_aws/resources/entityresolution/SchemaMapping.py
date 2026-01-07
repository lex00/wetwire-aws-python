"""PropertyTypes for AWS::EntityResolution::SchemaMapping."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SchemaInputAttribute(PropertyType):
    field_name: DslValue[str] | None = None
    type_: DslValue[str] | None = None
    group_name: DslValue[str] | None = None
    hashed: DslValue[bool] | None = None
    match_key: DslValue[str] | None = None
    sub_type: DslValue[str] | None = None
