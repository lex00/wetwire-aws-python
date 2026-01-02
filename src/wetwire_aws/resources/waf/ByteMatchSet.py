"""PropertyTypes for AWS::WAF::ByteMatchSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class ByteMatchTuple(PropertyType):
    field_to_match: FieldToMatch | None = None
    positional_constraint: str | None = None
    text_transformation: str | None = None
    target_string: str | None = None
    target_string_base64: str | None = None


@dataclass
class FieldToMatch(PropertyType):
    type_: str | None = None
    data: str | None = None
