"""PropertyTypes for AWS::WorkSpacesWeb::IpAccessSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IpRule(PropertyType):
    ip_range: str | None = None
    description: str | None = None
