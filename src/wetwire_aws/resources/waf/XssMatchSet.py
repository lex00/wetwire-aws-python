"""PropertyTypes for AWS::WAF::XssMatchSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class FieldToMatch(PropertyType):
    type_: str | None = None
    data: str | None = None


@dataclass
class XssMatchTuple(PropertyType):
    field_to_match: FieldToMatch | None = None
    text_transformation: str | None = None
