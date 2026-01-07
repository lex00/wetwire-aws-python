"""PropertyTypes for AWS::IVSChat::Room."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag
from wetwire_aws.typing import DslValue


@dataclass
class MessageReviewHandler(PropertyType):
    fallback_result: DslValue[str] | None = None
    uri: DslValue[str] | None = None
