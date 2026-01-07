"""PropertyTypes for AWS::CloudFront::KeyGroup."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class KeyGroupConfig(PropertyType):
    items: list[DslValue[str]] = field(default_factory=list)
    name: DslValue[str] | None = None
    comment: DslValue[str] | None = None
