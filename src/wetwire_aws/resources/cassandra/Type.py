"""PropertyTypes for AWS::Cassandra::Type."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Field(PropertyType):
    field_name: DslValue[str] | None = None
    field_type: DslValue[str] | None = None
