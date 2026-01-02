"""PropertyTypes for AWS::EC2::PrefixList."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Entry(PropertyType):
    cidr: str | None = None
    description: str | None = None
