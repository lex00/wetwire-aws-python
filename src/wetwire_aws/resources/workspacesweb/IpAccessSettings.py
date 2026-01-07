"""PropertyTypes for AWS::WorkSpacesWeb::IpAccessSettings."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IpRule(PropertyType):
    ip_range: DslValue[str] | None = None
    description: DslValue[str] | None = None
