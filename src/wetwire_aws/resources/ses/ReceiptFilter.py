"""PropertyTypes for AWS::SES::ReceiptFilter."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Filter(PropertyType):
    ip_filter: DslValue[IpFilter] | None = None
    name: DslValue[str] | None = None


@dataclass
class IpFilter(PropertyType):
    cidr: DslValue[str] | None = None
    policy: DslValue[str] | None = None
