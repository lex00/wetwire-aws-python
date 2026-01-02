"""PropertyTypes for AWS::Logs::DeliveryDestination."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class DestinationPolicy(PropertyType):
    delivery_destination_name: str | None = None
    delivery_destination_policy: dict[str, Any] | None = None
