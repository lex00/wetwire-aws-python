"""PropertyTypes for AWS::VpcLattice::DomainVerification."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class TxtMethodConfig(PropertyType):
    _property_mappings: ClassVar[dict[str, str]] = {
        "name": "name",
        "value": "value",
    }

    name: DslValue[str] | None = None
    value: DslValue[str] | None = None
