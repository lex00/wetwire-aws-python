"""PropertyTypes for AWS::EC2::TransitGatewayPeeringAttachment."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class PeeringAttachmentStatus(PropertyType):
    code: DslValue[str] | None = None
    message: DslValue[str] | None = None
