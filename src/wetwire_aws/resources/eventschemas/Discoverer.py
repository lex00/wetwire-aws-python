"""PropertyTypes for AWS::EventSchemas::Discoverer."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, ClassVar

from wetwire_aws.base import PropertyType, Tag


@dataclass
class TagsEntry(PropertyType):
    key: str | None = None
    value: str | None = None
