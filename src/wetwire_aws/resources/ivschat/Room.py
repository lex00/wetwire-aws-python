"""PropertyTypes for AWS::IVSChat::Room."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class MessageReviewHandler(PropertyType):
    fallback_result: str | None = None
    uri: str | None = None
