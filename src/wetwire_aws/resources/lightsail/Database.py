"""PropertyTypes for AWS::Lightsail::Database."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class RelationalDatabaseParameter(PropertyType):
    allowed_values: str | None = None
    apply_method: str | None = None
    apply_type: str | None = None
    data_type: str | None = None
    description: str | None = None
    is_modifiable: bool | None = None
    parameter_name: str | None = None
    parameter_value: str | None = None
