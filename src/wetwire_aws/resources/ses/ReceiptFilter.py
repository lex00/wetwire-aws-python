"""PropertyTypes for AWS::SES::ReceiptFilter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Filter(PropertyType):
    ip_filter: IpFilter | None = None
    name: str | None = None


@dataclass
class IpFilter(PropertyType):
    cidr: str | None = None
    policy: str | None = None
