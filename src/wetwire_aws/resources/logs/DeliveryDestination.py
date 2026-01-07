"""PropertyTypes for AWS::Logs::DeliveryDestination."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class DestinationPolicy(PropertyType):
    delivery_destination_name: DslValue[str] | None = None
    delivery_destination_policy: DslValue[dict[str, Any]] | None = None
