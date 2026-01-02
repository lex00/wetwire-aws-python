"""PropertyTypes for AWS::EC2::TransitGatewayPeeringAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class PeeringAttachmentStatus(PropertyType):
    code: str | None = None
    message: str | None = None
