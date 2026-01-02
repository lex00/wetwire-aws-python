"""PropertyTypes for AWS::WAFRegional::IPSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class IPSetDescriptor(PropertyType):
    type_: str | None = None
    value: str | None = None
