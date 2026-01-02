"""PropertyTypes for AWS::ECS::ClusterCapacityProviderAssociations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class CapacityProviderStrategy(PropertyType):
    capacity_provider: str | None = None
    base: int | None = None
    weight: int | None = None
