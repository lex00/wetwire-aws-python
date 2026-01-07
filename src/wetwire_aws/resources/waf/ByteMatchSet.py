"""PropertyTypes for AWS::WAF::ByteMatchSet."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class ByteMatchTuple(PropertyType):
    field_to_match: DslValue[FieldToMatch] | None = None
    positional_constraint: DslValue[str] | None = None
    text_transformation: DslValue[str] | None = None
    target_string: DslValue[str] | None = None
    target_string_base64: DslValue[str] | None = None


@dataclass
class FieldToMatch(PropertyType):
    type_: DslValue[str] | None = None
    data: DslValue[str] | None = None
