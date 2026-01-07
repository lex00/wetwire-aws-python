"""PropertyTypes for AWS::VpcLattice::ServiceNetwork."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class SharingConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "enabled": "enabled",
    }

    enabled: DslValue[bool] | None = None
