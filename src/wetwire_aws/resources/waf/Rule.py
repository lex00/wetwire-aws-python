"""PropertyTypes for AWS::WAF::Rule."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class Predicate(PropertyType):
    data_id: str | None = None
    negated: bool | None = None
    type_: str | None = None
