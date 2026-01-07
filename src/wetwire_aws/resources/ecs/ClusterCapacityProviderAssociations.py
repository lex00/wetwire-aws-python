"""PropertyTypes for AWS::ECS::ClusterCapacityProviderAssociations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class CapacityProviderStrategy(PropertyType):
    capacity_provider: DslValue[str] | None = None
    base: DslValue[int] | None = None
    weight: DslValue[int] | None = None
