"""PropertyTypes for AWS::PCAConnectorAD::Connector."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class VpcInformation(PropertyType):
    security_group_ids: list[String] = field(default_factory=list)
    ip_address_type: str | None = None
