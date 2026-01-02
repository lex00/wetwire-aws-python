"""PropertyTypes for AWS::VpcLattice::ServiceNetwork."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class SharingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "enabled",
    }

    enabled: bool | None = None
