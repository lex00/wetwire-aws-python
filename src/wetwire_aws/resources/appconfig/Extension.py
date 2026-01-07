"""PropertyTypes for AWS::AppConfig::Extension."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Parameter(PropertyType):
    required: DslValue[bool] | None = None
    description: DslValue[str] | None = None
    dynamic: DslValue[bool] | None = None
