"""PropertyTypes for AWS::GlobalAccelerator::CrossAccountAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Resource(PropertyType):
    cidr: str | None = None
    endpoint_id: str | None = None
    region: str | None = None
