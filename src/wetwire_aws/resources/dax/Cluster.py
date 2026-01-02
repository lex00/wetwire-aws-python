"""PropertyTypes for AWS::DAX::Cluster."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SSESpecification(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "sse_enabled": "SSEEnabled",
    }

    sse_enabled: bool | None = None
