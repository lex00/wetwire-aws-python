"""PropertyTypes for AWS::VpcLattice::DomainVerification."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class TxtMethodConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "name",
        "value": "value",
    }

    name: str | None = None
    value: str | None = None
