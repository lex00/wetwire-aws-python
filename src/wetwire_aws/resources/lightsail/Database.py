"""PropertyTypes for AWS::Lightsail::Database."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class RelationalDatabaseParameter(PropertyType):
    allowed_values: DslValue[str] | None = None
    apply_method: DslValue[str] | None = None
    apply_type: DslValue[str] | None = None
    data_type: DslValue[str] | None = None
    description: DslValue[str] | None = None
    is_modifiable: DslValue[bool] | None = None
    parameter_name: DslValue[str] | None = None
    parameter_value: DslValue[str] | None = None
