"""PropertyTypes for AWS::WAFRegional::IPSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class IPSetDescriptor(PropertyType):
    type_: DslValue[str] | None = None
    value: DslValue[str] | None = None
