"""PropertyTypes for AWS::EC2::PrefixList."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class Entry(PropertyType):
    cidr: DslValue[str] | None = None
    description: DslValue[str] | None = None
