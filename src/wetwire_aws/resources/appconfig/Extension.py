"""PropertyTypes for AWS::AppConfig::Extension."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Parameter(PropertyType):
    required: bool | None = None
    description: str | None = None
    dynamic: bool | None = None
