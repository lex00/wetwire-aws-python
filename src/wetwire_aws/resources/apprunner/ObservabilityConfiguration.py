"""PropertyTypes for AWS::AppRunner::ObservabilityConfiguration."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class TraceConfiguration(PropertyType):
    vendor: str | None = None
