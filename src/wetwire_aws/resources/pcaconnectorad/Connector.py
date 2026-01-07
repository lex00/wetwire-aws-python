"""PropertyTypes for AWS::PCAConnectorAD::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class VpcInformation(PropertyType):
    security_group_ids: list[DslValue[str]] = field(default_factory=list)
    ip_address_type: DslValue[str] | None = None
